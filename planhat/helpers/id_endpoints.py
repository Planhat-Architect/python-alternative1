'''Method to get proper Id endpoints'''

def get_id_endpoint(id_type):
    # convert to lower 
    id_type = id_type.lower()
    # check id type
    if id_type == '_id':
        return ''
    elif id_type == 'externalid':
        return 'extid-'
    elif id_type == 'sourceid':
        return 'srcid-'
    else:
        return ValueError('Incorrect id type')