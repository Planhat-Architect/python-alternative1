# planhat-python-api
Python Planhat API Library for doing work with Planhat locally
[Planhat API Docs](https://docs.planhat.com/#introduction)

## Authentication
- Authentication details are found in the planhat/api/config file. 
- To authenticate. Import the Auth Class and pass your token as a string.
    - If you store secrets externally, then you can leverage this 
    - Can be connected with docker secrets as well if you write your own script to unpack them into string values 
    - Code example: 
```
from planhat.api.auth import AuthenticatePlanhat
# authenticate with API Key
AuthenticatePlanhat(
    API_KEY='string_value'
)
# once authenticated, import the models module
from planhat import models
```

## Access different models via the Models Module

### Methods 
- Create: create a record 
- Update: Update based on Id
- Get by Id: Get record by Id
- Get all: Query a list of the model 
- Delete: Delete a record by Id
- Bulk Upsert: Upload a list of records 
- Open Model Docs: Opens the documentation at the section of the model you're working with

#### Disclaimer: 
- This library was written by me, an end user of planhat, so there is no warranty with the use of this code as stated in the licensing.
