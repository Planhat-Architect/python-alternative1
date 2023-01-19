'''Framework Module that houses the model class to create methods for each Planhat Model'''
import json
import webbrowser

from planhat.api import make_request
from planhat.helpers import check_obj, id_endpoints


# open URL to navigate to Model Docs
def open_url(url):
    return webbrowser.open(url)


class Model:
    '''A class that houses functions that work with each Planhat Module'''
    def __init__(self, model_endpoint : str, required_fields : list, model_docs : str):
        self.model_endpoint = model_endpoint
        self.required_fields = required_fields
        self.model_docs = model_docs

    def open_docs_page(self):
        open_url(self.model_docs)

    # field check helper function
    def _field_check(self, upload_obj):
        '''Returns True if object doesn't have all required fields'''
        # requied asset fields
        check_obj.not_okay(upload_obj, self.required_fields)

    ## Model Functions

    def create(self, upload_obj : dict):
        '''Creates a planhat asset

        Parameters:
        - upload_obj : dict
            Dictionary object of asset details. See Model details for required fields
        '''
        # check for required fields
        self._field_check(upload_obj)
        # convert to json
        upload_json = json.dumps(upload_obj)
        # return response 
        return make_request.post(self.model_endpoint, upload_json)

    def update(self, upload_obj : dict, identifier : str, id_type : str='_id'):
        '''Updates an existing asset based on an identifier
        
        Parameters:
        - upload_obj : dict
            - Dictionary of data to update the asset
        - identifier : str
            - Default planhat _id
        - id_type : str = '_id' # defaults to standard planhat Id
            - Custom Ids
                - id_type = 'sourceId'
                - id_type = 'externalId'
            - If custom field, only planhat _id will work
        '''
        # convert to json 
        upload_json = json.dumps(upload_obj)
        # identifier endpoint 
        id_endpoint = id_endpoints.get_id_endpoint(id_type)
        # return response 
        return make_request.put(
            endpoint=self.model_endpoint +'/'+ id_endpoint + identifier,
            data=upload_json
        )

    def get_by_id(self, identifier : str, id_type : str='_id'):
        '''Get a specific asset by Id
        
        Parameters:
        - upload_obj : dict
            - Dictionary of data to update the asset
        - identifier : str
            - Default planhat _id
        '''
        # get id endpoint 
        id_endpoint = id_endpoints.get_id_endpoint(id_type)
        # return response
        return make_request.get(
            endpoint=self.model_endpoint +'/'+ id_endpoint + identifier
        )

    def get_all(self, limit : int = 5000, **kwargs):
        '''Get a list of all assets
        
        Query Params:
        - limit : int
            - Limit of results to pull
        - kwargs:
            - Query parameters for get all. Query parameters arguments must have the same name as query params'''
        # set url params
        if len(kwargs.keys()) > 0:
            url_params = '&'.join([f'{key}={value}' for key, value in kwargs.items()])
        else:
            url_params = ''
        # get URL Params
        url_params = '?limit=' + str(limit) + url_params
        # return all
        return make_request.get(endpoint=self.model_endpoint + url_params)

    def bulk_upsert(self, upload_list : list):
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
            endpoint=self.model_endpoint,
            data=upload_json
        )

    def delete(self, _id : str):
        '''Deletes a custom field by Id

        Parameters:
        - _id : str
            - Planhat Id of the custom field to delete'''
        return make_request.delete(self.model_endpoint, _id)