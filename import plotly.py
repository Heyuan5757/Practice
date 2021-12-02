import plotly.graph_objs as go
from jira import JIRA
import pandas as pd
import datetime
from collections import Counter
from IPython.display import display, HTML

def jira_authority(user, passwd):
    options = {"server": "https://jira.deeproute.ai/"}
    jira = JIRA(options, basic_auth=(user, passwd))
    return jira


def deal_with_day(days):
    '''
    处理常用需要时间关系
    days:需要处理几天是时间内的数据
    '''
    today = datetime.datetime.today()
    lastweek = today - datetime.timedelta(days=days)
    today = today.strftime("%Y-%m-%d")
    lastweek = lastweek.strftime("%Y-%m-%d")
    return str(lastweek), str(today)



def deal_data(jql):
    '''
    jql: 需要传入查询的jql
    '''
    block_size = 1000
    block_num = 0
    allissues = []
    while True:
        start_idx = block_num*block_size
        issues = jira.search_issues(jql, start_idx, block_size)
        if len(issues) == 0:
            break
        block_num += 1
        for issue in issues:
            allissues.append(issue)

    issues = pd.DataFrame()
    for issue in allissues:
        d = {
            'key': issue.key,
            'assignee': issue.fields.assignee,
            'reporter': issue.fields.reporter,
            'created': issue.fields.created,
            'summary': issue.fields.summary,
            'priority': issue.fields.priority.name,
            'status': issue.fields.status.name,
        }

        issues = issues.append(d, ignore_index=True)
        issues['created'] = issues['created'].str.replace("T", " ")
        issues['created']=[x[:19] for x in issues['created']]
    display(HTML(issues.to_html()))
    return issues

def graph(jql):
    """
    任务闭环率的饼图
    """
    results = jira.search_issues(jql)
    status = []
    for issue in results:
        status.append(issue.fields.status.name)
    output = Counter(status)
    labels = list(output.keys())
    values = list(output.values())
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.show()

if __name__ == '__main__':
    user = 'simulationTest0'
    passwd = '123456Qq.'
    jira = jira_authority(user, passwd)
    lastweek, today = deal_with_day(30)
    jql = 'project = OB AND created >='+lastweek+'AND created <='+today+'ORDER BY priority DESC, updated DESC'
    #jql = 'project = OT AND created >= 2021-11-10 AND created < 2021-11-15 AND component = "grading&reproducible" ORDER BY created DESC'
    deal_data(jql)
    graph(jql)