import json

from planhat.api import make_request

def create_field(field_obj):
    # convert field obj to json 
    field_json = json.dumps(field_obj)
    # create field 
    result = make_request.post('customfields', field_json)
    # return result 
    return {
        "fieldName":field_obj['name'], 
        "result":result
    }