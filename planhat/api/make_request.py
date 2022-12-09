import sys
import json

import requests 
import pandas as pd

from planhat.api import config


# Planhat base URL 
base_url = 'https://api.planhat.com/'

# request headers for Planhat API. Auth via Bearer token updated in planhat_api.config module
headers = {
    "content-type":"application/json",
    "Authorization":f"Bearer {config.API_KEY}",
}

def error_hanlder(res):
    '''
    Function for returning error details when sending a request to the Planhat API 
    Params: res - request results object 
    '''

    status = res.status_code

    # iferror 
    if status != 200:
        # limit traceback response to non-verbose API error 
        sys.tracebacklimit = -1
        return f'A request error has occured - Status Code {status}: {res.text}'
    else:
        # else continue and return response 
        pass

def post(endpoint, data):
    '''
    Post request 

    Parmas: 
    endpont: str - endpoint string 
    data: Obj - Default: None Obj with payload data for put/post
    '''

    # break calause for empty payload 
    if data == None:
        return 'No Payload, please include POST Data'

    res = requests.post(
        url= base_url + endpoint,
        headers=headers,
        data=data,
        timeout=120
    )

    error_hanlder(res)

    return res 

def put(endpoint, data):
    '''
    Put request 

    Parmas: 
    endpont: str - endpoint string 
    data: Obj - Default: None Obj with payload data for put/post
    '''

    # break calause for empty payload 
    if data == None:
        return 'No Payload, please include PUT Data'

    res = requests.put(
        url= base_url + endpoint,
        headers=headers,
        data=data,
        timeout=120
    )

    error_hanlder(res)

    return res 

def get(endpoint, data=None):
    '''
    Gets data from the Planhat API 

    Params: 
    endpoint: str - endpoint string to get data from
    '''

    res = requests.get(
        url=base_url + endpoint,
        headers=headers,
        data=data,
        timeout=120
    )

    error_hanlder(res)

    return res

def delete(endpoint, _id):
    '''
    Delete a Planhat record

    Params:
    endoint: str - endpoint string of object/model todelete from 
    _id: str - record id to delete
    '''

    res = requests.delete(
        url=base_url + endpoint + '/' + _id,
        headers=headers,
        timeout=120
    )

    error_hanlder(res)

    return res

def response_to_df(res):
    '''
    Convert response to a DataFrame 

    Params: res - Planhat API response obj
        - Access ._content values and convert to DataFrame from records 
    '''
    # convert response to string and decode bytes 
    res_str = res.decode('utf-8')
    # convert string to json
    res_json = json.loads(res_str)
    # convert response to DataFrame 
    res_df = pd.json_normalize(res_json)
    # return repsonse DataFrame 
    return res_df