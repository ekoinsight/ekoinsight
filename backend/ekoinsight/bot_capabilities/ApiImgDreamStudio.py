import os
import warnings
from PIL import Image,ImageOps
import io
from torchvision.transforms import GaussianBlur
from BotCapabilities.ApiDreamStudio import ApiDreamStudio
from BotCapabilities.BotClass import BotClass
import cv2
import numpy as np

class ApiImgDreamStudio(ApiDreamStudio):
    def __init__(self, dry_run=False):
        super().__init__(dry_run=dry_run)
        # https://dreamstudio.com/api/
        
        # Set the engine to use for generation.
        self.max_width = 512
        self.max_height = 512
        self.acceptable_ratios = {
            (21, 9),
            (16, 9),
            (3, 2),
            (5, 4),
            (1, 1),
            (4, 5),
            (2, 3),
            (9, 16),
            (9, 21),
        }


        #https://dreamstudio.com/api/
        from stability_sdk import client
        import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


        self.engine=self.config["img_dreamstudio"]['engines']['generation_engine']
        self.api=client.StabilityInference(
            key=self.api_key,
            verbose=True, # Print debug messages.
            engine=self.engine #not sure why python puts it in a tuple...
            )
        self.generation=generation

        import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


    def get_accepted_dimensions(self,width,height):
        # Initialize a list to store valid combinations
        valid_combinations = []

        # Iterate through all possible height and width combinations
        for each_height in range(64, height+1, 64):
            for each_width in range(64, width+1, 64):
                # Calculate the ratio of height to width for the current combination
                ratio = each_height / each_width
                
                # Check if the calculated ratio matches any of the accepted ratios
                if any(abs(ratio - (r[0] / r[1])) < 0.01 for r in self.acceptable_ratios):
                    valid_combinations.append((each_width, each_height))

        return valid_combinations

    def resize_image_64(self, img):

        img_copy=img
        width, height = img.size

        # Calculate new dimensions while maintaining proportions
        ratio = max(self.max_width / width, self.max_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)

        #only going for 512*512
        img = img.resize((new_width, new_height), Image.BILINEAR)

        #these all fit the accepted ratios and are divisible by 64
        valid_dimensions=self.get_accepted_dimensions(width=img.width,height=img.height)

        best_difference=999999
        for width, height in valid_dimensions:
            difference = abs(img.width - width) + abs(img.height - height)
            if difference < best_difference:
                best_match = (width, height)
                best_difference = difference

        #print(f"best_match {best_match}")
        img = img.resize(best_match, Image.BILINEAR)

        return img

    def save_img(self, resps,img_filename):
        save_path=self.path + f"{img_filename.split('.')[0]}.png"
        for resp in resps:
            for artifact in resp.artifacts:
                if artifact.finish_reason == self.generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again."
                    )
                if artifact.type == self.generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    img.save(
                        save_path
                    )  # Save our generated images with their seed number as the filename.
        print(f"saved inpainted img at {save_path}")
        return save_path

    # def fetch_img(self, prompt, width=512, height=512):
        
    #     self.path = self.config["img_dreamstudio"]["output_paths"][
    #         "generation_save_path"
    #     ]

    #     if self.dry_run:
    #         return f"would have created a story with {self.provider_name} using prompt {prompt}"
    #     else:
    #         resps = self.api.generate(
    #             prompt=prompt, width=width, height=height, cfg_scale=9.0
    #         )

    #         return self.save_img(self, resps, prompt)


    def shrink_img(self,image,img_mask_pct=0.5):
        scale_factor = max(0.2,1-img_mask_pct)
        # Get the original image dimensions
        original_width, original_height = image.size

        # Calculate the new dimensions
        new_height = int(original_height * scale_factor)
        new_width = int(original_width * scale_factor)

        # Resize the image to the new dimensions
        resized_image = image.resize((new_width, new_height))

        # Create a black canvas (512x512)
        canvas = np.zeros((original_height, original_width, 3), dtype=np.uint8)

        # Calculate the position to place the resized image in the center
        y_offset = (original_height - new_height) // 2
        x_offset = (original_width - new_width) // 2

        # Paste the resized image onto the canvas
        canvas[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = resized_image

        return Image.fromarray(canvas)

    def fetch_inpaint_img(
        self,
        img_filename,
        img_path=None,
        mask_path=None,
        mask_type="",  #'except' type, shows only the item, everything else is black
        prompt="mountains of trash on the beach",
        img_mask_pct=0.5
    ):

        self.path = self.config["img_dreamstudio"]["output_paths"]["inpaint_save_path"]

        prompt= [
            self.generation.Prompt(text=prompt,parameters=self.generation.PromptParameters(weight=1)),
            self.generation.Prompt(text="painting, cartoon, fuzzy, blurry",parameters=self.generation.PromptParameters(weight=-1))]

        if img_path:
            self.img_input_dir=img_path

        if not mask_path:
            if mask_type == "except":
                mask_path = self.except_mask_output_dir
            else:
                mask_path = self.mask_output_dir

        img_path = self.img_input_dir + img_filename

        img = Image.open(img_path)
        mask_i = Image.open(mask_path)

        img = ImageOps.exif_transpose(img)
        mask_i = ImageOps.exif_transpose(mask_i)

        img = self.resize_image_64(img)
        mask_i = self.resize_image_64(mask_i)

        width, height = img.size
        mask_i_width, mask_i_height = mask_i.size

        # would need to have a max img size

        img = img.resize((min(width, mask_i_width), min(height, mask_i_height)))
        mask_i = mask_i.resize((min(width, mask_i_width), min(height, mask_i_height)))

        blur = GaussianBlur(5, 20)
        mask_i = blur(mask_i)


        #maybe shrink the image based off of how much space the mask takes 
        img=self.shrink_img(img,img_mask_pct)
        mask=self.shrink_img(mask_i,img_mask_pct)


        if self.dry_run:
            return f"would have created an inpaint img with with {self.provider_name}"
        else:
            resps = self.api.generate(
                prompt=prompt,
                init_image=img,
                mask_image=mask,
                start_schedule=1,
                # seed=1838510951,  # If attempting to transform an image that was previously generated with our API,
                # initial images benefit from having their own distinct seed rather than using the seed of the original image generation.
                steps=50,  # Amount of inference steps performed on image generation. Defaults to 30.
                # cfg_scale=8.0, # Influences how strongly your generation is guided to match your prompt.
                # Setting this value higher increases the strength in which it tries to match your prompt.
                # Defaults to 7.0 if not specified.
                #width=img.width,  # Generation width, if not included defaults to 512 or 1024 depending on the engine.
                #height=img.height,  # Generation height, if not included defaults to 512 or 1024 depending on the engine.
                width=512,  # Generation height, if not included defaults to 512 or 1024 depending on the engine.
                height=512,  # Generation height, if not included defaults to 512 or 1024 depending on the engine.
                # sampler=generation.SAMPLER_K_DPMPP_2M, # Choose which sampler we want to denoise our generation with.
                sampler=self.generation.SAMPLER_K_DPMPP_2S_ANCESTRAL,  # Choose which sampler we want to denoise our generation with.
                # Defaults to k_lms if not specified. Clip Guidance only supports ancestral samplers.
                # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
                guidance_preset=self.generation.GUIDANCE_PRESET_FAST_BLUE,
            )

            return self.save_img(resps, img_filename)
