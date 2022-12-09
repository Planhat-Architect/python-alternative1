'''Python Module that houses all model frameworks'''
from planhat.api.framework import Model

assets = Model(
    model_endpoint='assets',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#assets'
)

companies = Model(
    model_endpoint='companies',
    required_fields=['name'],
    model_docs='https://docs.planhat.com/#companies'
)