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

## Authentication

# From env 
# API_KEY = os.getenv('ph_api_key')

# From .txt
API_KEY = open('./planhat/api/api_key.txt').read().replace('\n','')

## API Setup

# Planhat base URL 
base_url = 'https://api.planhat.com/'

# request headers for Planhat API. Auth via Bearer token updated in planhat_api.config module
headers = {
    "content-type":"application/json",
    "Authorization":f"Bearer {API_KEY}",
}
