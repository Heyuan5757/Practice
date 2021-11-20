from jira import JIRA
from collections import Counter
import plotly.graph_objects as go
import  plotly.offline as  of

def jira_authority(user, passwd):
    options = {"server": "https://jira.deeproute.ai/"}
    jira = JIRA(options, basic_auth=(user, passwd))
    return jira

user = 'yuanhe'
passwd = 'Jack616977'
jira = jira_authority(user, passwd)

jql ='''
project = OT AND (status = 规划中 AND (计划开始时间 < startOfDay(-1) OR 计划开始时间 is EMPTY) OR status = 处理中 AND (计划结束时间 < startOfDay(-1) OR 计划结束时间 is EMPTY) OR status = BACKLOG AND createdDate < -2d OR status = done AND status changed from 处理中 to DONE before startofday(-2)  OR status = Pause AND status changed from 处理中 to PAUSE before startOfDay(-15)  OR status = Canceled AND (status changed from 处理中 to Canceled before startofday(-2)  OR status changed from BACKLOG to Canceled before startofday(-2) )) AND level != Fleet-Only AND (component != 持续任务 OR component is EMPTY) AND type != Bug AND (reporter in (membersOf(TestGroup), membersOf(SafetyGroup), membersOf(MaintenanceGroup), membersOf(USsafetyGroup), muxuanwang, ChenTony) OR assignee in (membersOf(TestGroup), membersOf(SafetyGroup), membersOf(MaintenanceGroup), membersOf(USsafetyGroup), muxuanwang, ChenTony)) AND key != OT-1420 ORDER BY created DESC
'''

results = jira.search_issues(jql,maxResults=300)
ot_id = []
assignees={}
for issue in results:
    if  issue.fields.assignee.displayName not in assignees.keys():
         assignees[issue.fields.assignee.displayName]=[]
    assignees[issue.fields.assignee.displayName].append(issue.key)
    
print(assignees)



# Use `hole` to create a donut-like pie chart
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
# fig.show()
# of.plot(fig,filename="plotly_plot.html")