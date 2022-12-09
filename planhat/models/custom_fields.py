''''Methods for working with custom fields

[Custom Field Documentation](https://docs.planhat.com/#customfields)'''
import json

from planhat.api import make_request

# config 
custom_field_endpoint = 'customfields'

def create_field(field_obj):
    # convert field obj to json 
    field_json = json.dumps(field_obj)
    # create field 
    result = make_request.post(custom_field_endpoint, field_json)
    # return result 
    return {
        "fieldName":field_obj['name'], 
        "result":result
    }

def update_custom_field(_id : str, update_obj : dict):
    '''Updates a custom field
    
    Parameters:
    - _id : str
        - Planhat Id of the custom field to update
    - update_obj : dict
        - Dictionary of custom field attributes to update'''
    # convert update into json 
    update_json = json.dumps(update_obj)
    # return response 
    return make_request.put(custom_field_endpoint, update_json)

def get_custom_fields():
    '''Gets a list of all the custom fields'''
    return make_request.get(custom_field_endpoint)