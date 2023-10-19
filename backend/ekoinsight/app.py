import os
import json

import fastapi
from fastapi.responses import JSONResponse
import flask
import werkzeug
from bot_capabilities.ApiImgDreamStudio import ApiImgDreamStudio
from bot_capabilities.ApiBlipReplicate import ApiBlipReplicate
from bot_capabilities.ApiChatGpt import ApiChatGpt
#from bot_capabilities.LocalMask import LocalMask
from bot_capabilities.ApiSegEverythingReplicate import ApiSegEverythingReplicate
from bot_capabilities.EkoInsightBot import EkoInsightBot
from bot_capabilities.ApiWatsonX import ApiWatsonX
app = fastapi.FastAPI()

@app.get("/")
async def hello_world():
    return {"omus?":"waldamus"}

def load_config():
    CONFIG_ENV=os.getenv("CONFIG_ENV","qa-local")
    print(f"CONFIG_ENV {CONFIG_ENV} LOADED")
    return json.load(open(f"config/{CONFIG_ENV}/{CONFIG_ENV}.json"))

config_data=load_config()


img_identifier=ApiBlipReplicate(dry_run=False)
mask_provider=ApiSegEverythingReplicate(dry_run=False)
#prompt_provider=ApiChatGpt(dry_run=False)
prompt_provider=ApiWatsonX(dry_run=False)
img_provider=ApiImgDreamStudio(dry_run=False)

#sfx_provider=ApiSfxReplicate(dry_run=False)

ekoinsightbot=EkoInsightBot(prompt_provider,img_provider,img_identifier,mask_provider)

print("###### EkoInsightBot READY##########")

input_dir=config_data['input_paths']['imgs']

uploaded_image_filepath= None  # Initialize a global variable
# language="french"

# for filename in sorted(os.listdir(os.path.dirname("inputs/imgs/"))):
#     if 'test' in filename:
#         print(filename)
#         answer=ekoinsightbot.feed(img_filename=filename,language=language)
#         print(answer)

@app.post("/feed/")
async def identify_image(file: fastapi.UploadFile,language: str = "English"):
    print("upload detected")
    global uploaded_image_filepath  # Declare the global variable

    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
        raise werkzeug.exceptions.HTTPException(status_code=400, detail="Only image files (jpg, jpeg, png, gif) are allowed.")

    filename=file.filename.lower()
    if '/' in filename:
        filename=filename.split('/')[1]

    print(f"filename : {filename}")
    print(f"input_dir : {input_dir}")
    filepath = os.path.join(input_dir, filename)

    with open(filepath, "wb") as image_file:
        image_file.write(file.file.read())

    score_reaction_dict = ekoinsightbot.feed(img_filename=filename,img_path=input_dir,language=language)
    #score_reaction_dict looks like {'score':5,'reaction':'great, another can...'}
    print(score_reaction_dict)
    return JSONResponse(content=score_reaction_dict, status_code=200)


# @app.post("/upload/")
# async def identify_image(file):
#     print("upload detected")
#     global uploaded_image_filepath  # Declare the global variable

#     if not file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
#         raise werkzeug.exceptions.HTTPException(status_code=400, detail="Only image files (jpg, jpeg, png, gif) are allowed.")

#     filename = f"uploaded_image_{os.urandom(4).hex()}.jpg"
#     filepath = os.path.join(input_dir, filename)

#     with open(filepath, "wb") as image_file:
#         image_file.write(file.file.read())

#     object_identification = img_identifier.execute(filepath)
#     print("image identified")
#     # uploaded_image_filepath = filepath
#     print(f"returning :{object_identification}")
#     # Create a JSONResponse with a 200 status code
#     return flask.JSONResponse(content= {"description": object_identification}, status_code=200)


# @app.post("/imagine/")
# async def imagine_image(identified_object: str):
#     print("imagine task detected")
#     global filepath  # Declare the global variable
#     if filepath is None:
#         raise HTTPException(status_code=400, detail="No uploaded image found. Please upload an image first.")

#     inpaint_path = ekoinsightbot.execute(filepath, identified_object=identified_object)

#     # Create a JSONResponse with a 200 status code
#     return JSONResponse(content={"inpaint_path": inpaint_path}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


