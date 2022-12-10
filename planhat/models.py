'''Python Module that houses all model frameworks'''
from planhat.api.framework import Model

assets = Model(
    model_endpoint='assets',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#assets'
)

campaings = Model(
    model_endpoint='campaings',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#campaigns'
)

churns = Model(
    model_endpoint='churn',
    required_fields=['companyId','value'],
    model_docs='https://docs.planhat.com/#churn'
)

companies = Model(
    model_endpoint='companies',
    required_fields=['name'],
    model_docs='https://docs.planhat.com/#companies'
)

conversations = Model(
    model_endpoint='conversations',
    required_fields=['companyId'],
    model_docs='https://docs.planhat.com/#conversations'
)

custom_fields = Model(
    model_endpoint='customfields',
    required_fields=['name','type','parent','isHidden'],
    model_docs='https://docs.planhat.com/#customfields'
)

end_users = Model(
    model_endpoint='endusers',
    required_fields=['email','companyId'],
    model_docs='https://docs.planhat.com/#endusers'
)

invoices = Model(
    model_endpoint='invoices',
    required_fields=['currency','cId'],
    model_docs='https://docs.planhat.com/#invoices'
)

issues = Model(
    model_endpoint='issues',
    required_fields=['title','sourceId','archived'],
    model_docs='https://docs.planhat.com/#issues'
)

licenses = Model(
    model_endpoint='licenses',
    required_fields=['_currency','companyId','fromDate','value'],
    model_docs='https://docs.planhat.com/#licenses'
)

notes = Model(
    model_endpoint='conversations',
    required_fields=['companyId','type'],
    model_docs='https://docs.planhat.com/#notes'
)

nps = Model(
    model_endpoint='nps',
    required_fields=['email','campaignId','score'],
    model_docs='https://docs.planhat.com/#nps'
)

opportunities = Model(
    model_endpoint='opportunities',
    required_fields=['companyId'],
    model_docs='https://docs.planhat.com/#opportunities'
)

objectives = Model(
    model_endpoint='objectives',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#objectives'
)

projects = Model(
    model_endpoint='projects',
    required_fields=['name','companyId','currency'],
    model_docs='https://docs.planhat.com/#projects'
)

sales = Model(
    model_endpoint='sales',
    required_fields=['_currency','companyId','salesDate','value'],
    model_docs='https://docs.planhat.com/#sales'
)

tasks = Model(
    model_endpoint='tasks',
    required_fields=['mainType','companyId'],
    model_docs='https://docs.planhat.com/#tasks'
)

tickets = Model(
    model_endpoint='tickets',
    required_fields=['comapnyId','sourceId','email'],
    model_docs='https://docs.planhat.com/#tickets'
)

users = Model(
    model_endpoint='users',
    required_fields=['email','nickName','firstName','lastName'],
    model_docs='https://docs.planhat.com/#users'
)

workspaces = Model(
    model_endpoint='workspaces',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#workspaces'
)
