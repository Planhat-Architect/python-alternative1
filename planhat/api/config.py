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


# for production get from docker secrets 
API_KEY = os.getenv('ph_api_key')