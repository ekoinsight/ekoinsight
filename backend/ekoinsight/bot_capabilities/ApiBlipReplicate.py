import replicate
import os
from bot_capabilities.ApiReplicate import ApiReplicate
import spacy


class ApiBlipReplicate(ApiReplicate):
    #https://replicate.com/salesforce/blip/api#input-question
    def __init__(self,dry_run=False):
        super().__init__(dry_run=dry_run)
        #python -m spacy download en_core_web_sm
        self.nlp=spacy.load("en_core_web_sm")
        self.dry_run=dry_run

    def save_file(self,file_object, local_filename):
        with open(local_filename, 'wb') as f:
            f.write(file_object)


    def get_main_subject(self,sentence="The cat sat on the mat."):
        sentence=sentence.lower().replace("caption","").replace(":","").strip()
        doc = self.nlp(sentence)

        # Define a set of stopwords to filter out unimportant words
        stopwords = {"a", "an", "the", "in", "on", "at", "under", "near"}

        # Iterate through the tokens in the sentence
        for token in doc:
            # Check if the token is a noun and not in the stopwords set
            if token.pos_ == "NOUN" and token.text.lower() not in stopwords:
                # Find all tokens before the noun
                preceding_tokens = [t.text for t in doc[:token.i]]
                if preceding_tokens:
                    main_subject = " ".join(preceding_tokens) + " " + token.text
                else:
                    main_subject = token.text
                break

        return main_subject

    
    def api_fetch(self,img_path,
                  #sfx_string="salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746"
                  sfx_string="andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608"
                  ):
        response='Caption : can of kombucha on windowsill'
        if not self.dry_run:
            response = replicate.Client(api_token=self.api_key).run(
                sfx_string,
                input={"image": open(img_path, "rb"),
                    #"task":"image_captioning",
                    "question":"what is the object shown and what is it made of?",
                    "context":"""what is the object shown and what is it made of?
                    carboard box

                    what is the object shown and what is it made of?
                    aluminum can

                    what is the object shown and what is it made of?
                    plastic bag"""
                    }
            )

        #return self.get_main_subject(response)
        return response
    
    def execute(self,img_path):
        return self.api_fetch(img_path)