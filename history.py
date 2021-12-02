from jira import JIRA


def jira_authority(user,pwd):
    server = {"server": "https://jira.deeproute.ai/"}
    jira = JIRA(server , basic_auth = (user,pwd))
    return jira

user = 'simulationTest0'
passwd = '123456Qq.'
jira = jira_authority(user, passwd)
issue = jira.issue('OB-1000', expand='changelog')

changelog = issue.changelog

for history in changelog.histories:
    print('===================')
    print('author ', history.author)
    print('created ', history.created)
    print('id ', history.id)
    for item in history.items:
        print('field ', item.field)
        print('fieldtype ', item.fieldtype)
        # print('from ', item.from)
        print('fromString ', item.fromString)
        print('to ', item.to)
        print('toString ', item.toString)