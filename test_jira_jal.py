from jira import JIRA
from numpy.core.shape_base import block
from numpy.lib.function_base import append
import datetime

def jira_authority(user,pwd):
    server = {"server": "https://jira.deeproute.ai/"}
    jira = JIRA(server , basic_auth = (user,pwd))
    return jira

def deal_with_months(months):
    monthstart ='2021-'+str(months)+'-1'
    monthdone='2021-'+str(months+1)+'-1'
    if months == 12:
        monthdone='2022-1-1'
    return monthstart,monthdone

def deal_with_day(days):
    today = datetime.datetime.today()
    lastweek = today - datetime.timedelta(days)
    today = today.isoformat()
    lastweek = lastweek.isoformat()
    return today[0:10],lastweek[0:10]

def search_issues(jql):
    block_num = 0
    block_size = 1000
    all_issues = []
    while True:
        start_num = block_num * block_size
        issues = jira.search_issues( jql , start_num , block_size )
        if len(issues) == 0 :
            break
        for issue in issues :
            all_issues.append(issue)
        block_num += 1
    return all_issues

if __name__=='__main__':
    user = 'simulationTest0'
    passwd = '123456Qq.'
    jira = jira_authority(user, passwd)
    monthstarter,monthdone = deal_with_months(11)
    today,lastweek = deal_with_day(20)
    jql='project = OB AND created >= '+monthstarter+' AND created <= '+monthdone+' ORDER BY priority DESC, updated DESC'
    jql='project = OB AND created >= '+lastweek+' AND created <= '+today+' ORDER BY priority DESC, updated DESC'
    all_issues=search_issues(jql)
    print(all_issues)
