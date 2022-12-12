# planhat-python-api
Python Planhat API Library for doing work with Planhat locally
[Planhat API Docs](https://docs.planhat.com/#introduction)

## Authentication
- Authentication details are found in the planhat/api/config file. 
- Currenlty it's set to look for a secret.txt file, but you can update that however you'd like and things should work as long as you're sending a string value to the API_KEY variable.

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
