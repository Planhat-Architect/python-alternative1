'''Module for checking upload object fidelity ie. if it has the required fields'''



def not_okay(obj : dict, fields : list):
    '''Checks whether or not an object has the correct required fields
    
    Parameters:
    - obj : dict
        - Upload object to be checked
    - fields : list
        - List of fields to check for
        
    Returns:
    - A bool for object fidelity'''

    if not all(field in obj for field in fields):
        raise KeyError('Please ensure all required fields are included')