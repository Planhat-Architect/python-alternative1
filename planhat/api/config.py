'''
API Config 

Variables: 
- API_KEY: Planhat API Tokne/Key

Info: 
- Service Account Name: 
- AccountId: 
- Email: 

Getting API Key:
- Setting it as an ENV Variable 
    - export ph_api_key="" # for temp 
    - If running with docker, you can set this when creating the container
- You can of course change how you capture the API to whatever suits your implementation best
'''
import os


## API Setup

# Planhat base URL 
base_url = 'https://api.planhat.com/'

# request headers for Planhat API. Auth via Bearer token updated in planhat_api.config module
def get_headers():
    # Authentication
    API_KEY = os.environ['PLANHAT_API_KEY']
    return {
        "content-type":"application/json",
        "Authorization":f"Bearer {API_KEY}",
    }
