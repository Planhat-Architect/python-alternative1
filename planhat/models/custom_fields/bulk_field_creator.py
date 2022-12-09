'''
Script to create custom fields in Planhat. 

Takes CSV input and creates field JSON object to upload to the Planhat API 

CSV Columns:
- isFeatured	
- parent	
- name	
- type	
- listValues	
- isHIdden

Docuemntation on Creating Custom Fields - https://docs.planhat.com/#post_customfield
'''

import json

import pandas as pd 

from planhat.models.custom_fields import field_creator
from planhat.helpers.multi_threading import multi_threaded_req




def import_fields(file_path):
    '''
    Function that imports and cleans up fields csv and converts to JSON upload object
    '''
    # get fields DataFrame 
    df = pd.read_csv(file_path)

    # break clause for if there's a list value field 
    if 'listValues' in df.columns:
        # convert listValues to list instead of str 
        df.listValues = df.listValues.str.split(',')
    
    # fill NaNs
    df = df.fillna('')
    # convert to dictionary 
    fields_dict = df.to_dict(orient='records')
    # return fields dict 
    return fields_dict

def upload_fields(fields_dict):
    # import fields bulk json 
    res = multi_threaded_req(field_creator.create_field, fields_dict)
    # unpack results 
    results_list = list(map(lambda x: x.result(), res))
    # print resutls 
    return results_list

def upload_inline(file_path):
    '''Function that uploads fields via CSV inline'''
    # get fields dictionary 
    fields_dict = import_fields(file_path)
    # upload fields and return results
    return upload_fields(fields_dict)


# Runs if executed from CLI
if __name__=='__main__':
    # get fields file path from input 
    file_path = input('Fields CSV file path: ')
    # get fields dictionary 
    fields_dict = import_fields(file_path)
    # upload fields 
    print(upload_fields(fields_dict))