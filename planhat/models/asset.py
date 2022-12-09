'''Module for doing work with Planhat Assets

[Model Details:](https://docs.planhat.com/#assets)'''
import json

from planhat.api import make_request
from planhat.helpers import check_obj, id_endpoints

# Config 
asset_endpoint = '/assets'

def _asset_check(asset_obj):
    '''Returns True if object doesn't have all required fields'''
    # requied asset fields
    requied_fields = ['name','companyId']
    check_obj.not_okay(asset_obj, requied_fields)

def create_asset(asset_obj):
    '''Creates a planhat asset

    Parameters:
    - asset_obj : dict
        Dictionary object of asset details. See Model details for required fields
    '''
    # check for required fields
    _asset_check(asset_obj)
    # convert to json
    upload_json = json.dumps(asset_obj)
    # return response 
    return make_request.post(asset_endpoint, upload_json)

def update_asset(asset_obj : dict, identifier : str, id_type : str='_id'):
    '''Updates an existing asset based on an identifier
    
    Parameters:
    - asset_obj : dict
        - Dictionary of data to update the asset
    - identifier : str
        - Default planhat _id
    - id_type : str = '_id' # defaults to standard planhat Id
        - Custom Ids
            - id_type = 'sourceId'
            - id_type = 'externalId'
  '''
    # convert to json 
    upload_json = json.dumps(asset_obj)
    # identifier endpoint 
    id_endpoint = id_endpoints.get_id_endpoint(id_type)
    # return response 
    return make_request.put(
        endpoint=asset_endpoint +'/'+ id_endpoint + identifier[1],
        data=upload_json
    )

def get_asset_by_id(identifier : str, id_type : str='_id'):
    '''Get a specific asset by Id
    
    Parameters:
    - asset_obj : dict
        - Dictionary of data to update the asset
    - identifier : str
        - Default planhat _id
    '''
    # get id endpoint 
    id_endpoint = id_endpoints.get_id_endpoint(id_type)
    # return response
    return make_request.get(
        endpoint=asset_endpoint +'/'+ id_endpoint + identifier
    )

def get_assets():
    '''Get a list of all assets'''
    return make_request.get(endpoint=asset_endpoint)

def bulk_upsert_assets(upload_list : list):
    '''Upload a list of dictionaries (asset records)

    To create: The record must include a valid name and planhat companyId
    To update: The record must include one of the following keyables: _id, sourceId, and/or externalId
    
    Parameters:
    - upload_list : list
        - List of upload/update records'''
    # convert to json 
    upload_json = json.dumps(upload_list)
    # return resposne 
    return make_request.put(
        endpoint=asset_endpoint,
        data=upload_json
    )
