'''Module to Authenticate the Planhat API'''
import os

class AuthenticatePlanhat:
    def __init__(self, API_KEY : str, service_account_name : str = None, service_account_id : str = None):
        # set API Key Value
        os.environ['PLANHAT_API_KEY'] = API_KEY
        self.SERVICE_ACCOUNT_NAME = service_account_name
        self.SERVICE_ACCOUNT_ID = service_account_id