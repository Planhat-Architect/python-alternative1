'''Python Module that houses all model frameworks'''
from planhat.api.framework import Model

asset = Model(
    model_endpoint='assets',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#assets'
)

campaign = Model(
    model_endpoint='campaings',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#campaigns'
)

churn = Model(
    model_endpoint='churn',
    required_fields=['companyId','value'],
    model_docs='https://docs.planhat.com/#churn'
)

company = Model(
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

end_user = Model(
    model_endpoint='endusers',
    required_fields=['email','companyId'],
    model_docs='https://docs.planhat.com/#endusers'
)

invoice = Model(
    model_endpoint='invoices',
    required_fields=['currency','cId'],
    model_docs='https://docs.planhat.com/#invoices'
)

issue = Model(
    model_endpoint='issues',
    required_fields=['title','sourceId','archived'],
    model_docs='https://docs.planhat.com/#issues'
)

license = Model(
    model_endpoint='licenses',
    required_fields=['_currency','companyId','fromDate','value'],
    model_docs='https://docs.planhat.com/#licenses'
)

note = Model(
    model_endpoint='conversations',
    required_fields=['companyId','type'],
    model_docs='https://docs.planhat.com/#notes'
)

nps = Model(
    model_endpoint='nps',
    required_fields=['email','campaignId','score'],
    model_docs='https://docs.planhat.com/#nps'
)

opportuniy = Model(
    model_endpoint='opportunities',
    required_fields=['companyId'],
    model_docs='https://docs.planhat.com/#opportunities'
)

objective = Model(
    model_endpoint='objectives',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#objectives'
)

project = Model(
    model_endpoint='projects',
    required_fields=['name','companyId','currency'],
    model_docs='https://docs.planhat.com/#projects'
)

sale = Model(
    model_endpoint='sales',
    required_fields=['_currency','companyId','salesDate','value'],
    model_docs='https://docs.planhat.com/#sales'
)

task = Model(
    model_endpoint='tasks',
    required_fields=['mainType','companyId'],
    model_docs='https://docs.planhat.com/#tasks'
)

ticket = Model(
    model_endpoint='tickets',
    required_fields=['comapnyId','sourceId','email'],
    model_docs='https://docs.planhat.com/#tickets'
)

user = Model(
    model_endpoint='users',
    required_fields=['email','nickName','firstName','lastName'],
    model_docs='https://docs.planhat.com/#users'
)

workspaces = Model(
    model_endpoint='workspaces',
    required_fields=['name','companyId'],
    model_docs='https://docs.planhat.com/#workspaces'
)
