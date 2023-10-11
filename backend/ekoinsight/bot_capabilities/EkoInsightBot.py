

from .BotClass import BotClass
from templates import *
from utils import *
import time
from dotenv import load_dotenv

class EkoInsightBot(BotClass):
    def __init__(self,prompt_provider, img_provider,img_identifier,mask_provider,identified_object=None,sfx_provider=None):
        super().__init__()
        self.prompt_provider = prompt_provider
        self.img_provider = img_provider
        self.img_identifier = img_identifier
        self.mask_provider = mask_provider
        self.sfx_provider = sfx_provider
        self.img_filename=""
        self.img_input_dir=self.config['input_paths']['imgs']
        self.identified_object=identified_object
        self.identified_object_alt_language=identified_object
        self.pollution_prompt=""

    def feed(self,img_filename,img_path=None,language="English"):
        self.language=language
        self.prompt_provider.set_language(self.language)
        self.img_filename=img_filename

        score=0
        
        #VECTORSEARCH NEEDS TO BE IN ENGLISH, ARTICLES ARE IN ENGLISH
        if img_path:
            if not img_path.endswith("/"):
                img_path+="/"
            self.img_input_dir=img_path
        self.img_full_path=self.img_input_dir+self.img_filename

        start=time.time()
        self.identified_object=self.img_identifier.execute(img_path=self.img_full_path)

        print(f"img identified took {time.time()-start}s") #takes about 3 seconds

        start=time.time()
        rationale=self.prompt_provider.fetch_prompt(item=self.identified_object,prompt_template='tamagotchi_personality',max_tokens=1000, stop_sequences= ["END"])
        print(f"rationale generated : took {time.time()-start}s")

        if self.language!="English":
            rationale=self.prompt_provider.translate(rationale,self.language)
            
        #watsonx needs all the help it can get
        if score==0 or "score" in rationale:
            start_index = rationale.find("{")
            end_index = rationale.rfind("}") + 1
            dictionary_string = rationale[start_index:end_index]
            return eval(dictionary_string)
        else:
            return {"score":score,"rationale":rationale}


    def execute(self,img_filename,img_path=None,language="English"):
        self.language=language
        self.prompt_provider.set_language(self.language)
        self.img_filename=img_filename

        #VECTORSEARCH NEEDS TO BE IN ENGLISH, ARTICLES ARE IN ENGLISH
        if img_path:
            if not img_path.endswith("/"):
                img_path+="/"
            self.img_input_dir=img_path
        self.img_full_path=self.img_input_dir+self.img_filename

        start=time.time()
        self.identified_object=self.img_identifier.execute(img_path=self.img_full_path)
        if self.language!="English":
            self.identified_object_alt_language=self.prompt_provider.translate(self.identified_object,self.language)
            
        print(f"img identified : {self.identified_object_alt_language} : took {time.time()-start}s") #takes about 3 seconds

        start=time.time()
        mask_dict=self.mask_provider.execute(img_path=self.img_full_path)
        mask_path=mask_dict['mask_path']
        img_mask_pct=mask_dict['img_mask_pct']
        print(f"mask path provided : {mask_path} : took {time.time()-start}s")#takes about 33 seconds!

        start=time.time()
        self.pollution_prompt=self.prompt_provider.fetch_prompt(item=self.identified_object,prompt_template='pollution_prompt_template')
        full_pollution_prompt=f"{self.pollution_prompt} realistic, dirty pollution, dslr, soft lighting seen from above"
        #pollution_prompt+=" realistic, high definition, polluted"
        print(f"pollution_prompt generated : took {time.time()-start}s")
        print(f"pollution_prompt : {full_pollution_prompt}")

        start=time.time()
        inpaint_img_path=self.img_provider.fetch_inpaint_img(img_filename=img_filename,img_path=self.img_input_dir,mask_path=mask_path,prompt=full_pollution_prompt,img_mask_pct=img_mask_pct)
        print(f"inpaint_img_path produced : took {time.time()-start}s")
        print(f"inpaint_img_path : {inpaint_img_path}")


        ####EDUCATION PART
        #general education
        start=time.time()
        education_info=self.prompt_provider.fetch_prompt(item=self.identified_object_alt_language,prompt_template='educate_prompt_template',max_tokens=1000, stop_sequences= ["END"])
        print(f"education_info generated : took {time.time()-start}s")
        print(f"education_info : {education_info}")
        education_info=eval(education_info.split("= ")[1].replace("END",""))


        #from the vector database pinecone
        vectorsearch_info=None
        start=time.time()

        #the vector database is only in English
        if self.language=="English":
            item=education_info['likely_material_and_item']
        else:
            item=self.identified_object
        vectorsearch_info={'result':None,'source':None}
        try:
            query=f"what are interesting facts regarding {item}"
            vectorsearch_info=self.prompt_provider.fetch_using_index(query=query)
                
            print(f"vectorsearch_info query : took {time.time()-start}s")
            print(f"vectorsearch_info : {vectorsearch_info}")
        except Exception as e:
            print("FAILED vectorsearch_info")
            print(e)


        if vectorsearch_info['result'] and self.language!="English":
            vectorsearch_info['result']=self.prompt_provider.translate(vectorsearch_info['result'],self.language)

        return {"inpaint_img_path":inpaint_img_path,"education_info":education_info,"vectorsearch_info":vectorsearch_info,"pollution_prompt":self.pollution_prompt}

    def identify_img(self):
        self.img_identifier.identify_img(self.img_path)


    def fetch_img(self,prompt,style=None,size="256x256",dry_run=False,path=""):
        if self.img_provider:
            prompt+=f" no humans ,no humans,no humans,beautiful, highly detailed"
            if style:
                prompt+=f", {style}"
            #negative prompt
            prompt+=f" | disfigured:-1.0, ugly:-1.0, humans:-1.0, text:-1.0"
            img=self.img_provider.fetch_img(prompt,path=path)
            return img
        return []

    def fetch_sfx_object(self,input_text):
        #returns SFX object
        sfx_object=None
        if self.sfx_provider:
            sfx_object=self.sfx_provider.fetch_sfx(input_text)
        return sfx_object

