import os
import json

import fastapi
from fastapi.responses import JSONResponse
from bot_capabilities.ApiImgDreamStudio import ApiImgDreamStudio
from bot_capabilities.ApiBlipReplicate import ApiBlipReplicate
from bot_capabilities.ApiSegEverythingReplicate import ApiSegEverythingReplicate
from bot_capabilities.EkoInsightBot import EkoInsightBot
from bot_capabilities.ApiWatsonX import ApiWatsonX
app = fastapi.FastAPI()

def load_config():
    CONFIG_ENV=os.getenv("CONFIG_ENV","qa-local")
    print(f"CONFIG_ENV {CONFIG_ENV} LOADED")
    return json.load(open(f"config/{CONFIG_ENV}/{CONFIG_ENV}.json"))

config_data=load_config()


img_identifier=ApiBlipReplicate(dry_run=False)
mask_provider=ApiSegEverythingReplicate(dry_run=False)
prompt_provider=ApiWatsonX(dry_run=False)
img_provider=ApiImgDreamStudio(dry_run=False)

ekoinsightbot=EkoInsightBot(prompt_provider,img_provider,img_identifier,mask_provider)

print("###### EkoInsightBot READY##########")

input_dir=config_data['input_paths']['imgs']

uploaded_image_filepath= None 

@app.post("/feed")
async def identify_image(file: fastapi.UploadFile,language: str = "English"):
    print("upload detected")
    global uploaded_image_filepath  # Declare the global variable

    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
        raise fastapi.HTTPException(status_code=400, detail="Only image files (jpg, jpeg, png, gif) are allowed.")

    filename=file.filename.lower()
    if '/' in filename:
        filename=filename.split('/')[1]

    print(f"filename : {filename}")
    print(f"input_dir : {input_dir}")

    score_reaction_dict = ekoinsightbot.feed(img_filename=filename,img_path=input_dir,language=language)

    print(score_reaction_dict)
    return JSONResponse(content=score_reaction_dict, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, workers=10)


