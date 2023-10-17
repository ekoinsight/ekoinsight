import os
from .ApiClass import ApiClass
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model

class ApiIbm(ApiClass):
    def __init__(self,API_NAME="IBM",dry_run=False):
        super().__init__(API_NAME,dry_run)
        #
        #self.project_id  = "88268c35-0f8c-4820-8827-74229ed70f3f"
        #
        self.project_id  = "6bbf8d78-5482-4226-99c3-0c71eae4d43c"

        ibm_credentials = { 
            "url"    : "https://us-south.ml.cloud.ibm.com", 
            "apikey" : self.api_key
        }      

        model_id    = ModelTypes.LLAMA_2_70B_CHAT
        gen_parms   = None
        space_id    = None
        verify      = False

        self.model = Model( model_id, ibm_credentials, gen_parms, self.project_id, space_id, verify )   
        

        super().__init__(API_NAME,dry_run)

    # def save_file(self,object_to_save, local_filename):
    #     pass

    # def api_fetch(self,input_text):
    #     pass