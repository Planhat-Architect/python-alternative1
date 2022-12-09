'''
Python module to bulk upload assets (risks/ctas) to planhat. 

How to run: 
python -m planhat.assets.cta_upload file_path_to_json
'''

import sys
import json

from planhat.api import make_request
from planhat.helper.multi_threading import multi_threaded_req



def upload_assets(assets_json : str):
    '''
    Upload assets (risks/ctas) from JSON file in the main directory

    Args:
    assets_json: str - Filepath to JSON file for uplaoding 

    Ex. Obj: 
    {
        "name": "Implementation issue with SFDC",
        "companyId": "633de61b9ecb7b351fc04c5c",
        "sourceId": "",
        "createdAt": "2021-11-15",
        "custom": {
            "Risk Owner": "team.member@test.com",
            "GS Upload": true,
            "Status": "New",
            "Due Date": "2022-01-14",
            "Priority": "Medium",
            "Comments": "..."
        }
    }
    '''

    # get json obj from filepath
    json_obj = open(assets_json)
    # upload to planhat and store results
    res = make_request.put('assets', json_obj)
    # print results
    print(res)

# run upload function with file path arg from cli 
upload_assets(sys.argv[1])