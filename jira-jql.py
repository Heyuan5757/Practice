from jira import JIRA
from collections import Counter
import plotly.graph_objects as go
import plotly.express as px
import  plotly.offline as  py
import numpy as np
import xlsxwriter
import pandas


def jira_authority(user, passwd):
    options = {"server": "https://jira.deeproute.ai/"}
    jira = JIRA(options, basic_auth=(user, passwd))
    return jira

user = 'simulationTest0'
passwd = '123456Qq.'
jira = jira_authority(user, passwd)

ob_id = []
reporter={}
point={}
date=['2021-10-18','2021-10-23','2021-10-28','2021-11-2','2021-11-7','2021-11-12','2021-11-17','2021-11-22','2021-11-27']

for num in range(0,len(date)-1):
    jql ='''
            project = OB AND createdDate >={date1}    and createdDate <= {date2} ORDER BY priority DESC, updated DESC
            '''.format(date1=date[num],date2=date[num+1])

    results = jira.search_issues(jql,maxResults=1500)
    for issue in results:
        if  issue.fields.reporter.displayName not in reporter.keys():
            reporter[issue.fields.reporter.displayName]=[]
            point[issue.fields.reporter.displayName]=[0,0,0,0]
        reporter[issue.fields.reporter.displayName].append(issue.key)
        if issue.fields.customfield_11410.value ==  '2':
            point[issue.fields.reporter.displayName][0] += 1
        elif issue.fields.customfield_11410.value == '1':
            point[issue.fields.reporter.displayName][1] += 1
        elif issue.fields.customfield_11410.value == '0':
            point[issue.fields.reporter.displayName][2] += 1    
        elif issue.fields.customfield_11410.value == '-1':
            point[issue.fields.reporter.displayName][3] += 1

jql ='''
    project = OB AND createdDate >= '2021-11-27'    ORDER BY priority DESC, updated DESC
    '''    
results = jira.search_issues(jql,maxResults=1500)

for issue in results:
    if  issue.fields.reporter.displayName not in reporter.keys():
        reporter[issue.fields.reporter.displayName]=[]
        point[issue.fields.reporter.displayName]=[0,0,0,0]
    reporter[issue.fields.reporter.displayName].append(issue.key)
    if issue.fields.customfield_11410.value ==  '2':
        point[issue.fields.reporter.displayName][0] += 1
    elif issue.fields.customfield_11410.value == '1':
        point[issue.fields.reporter.displayName][1] += 1
    elif issue.fields.customfield_11410.value == '0':
        point[issue.fields.reporter.displayName][2] += 1    
    elif issue.fields.customfield_11410.value == '-1':
        point[issue.fields.reporter.displayName][3] += 1

workbook = xlsxwriter.Workbook("/home/OB_point.xlsx")
table = workbook.add_worksheet('sheet')
x=0 
for name in point:
    table.write(x,0,name)
    for y in range(1,5):
         table.write(x,y,point[name][y-1])
    x += 1
    
# workbook.close()

data = { 'name' : [],
                    '2分' : [],
                    '1分' : [],
                    '0分' : [],
                    '-1分' : [],
                    '总个数' : []
    }
_index = []
_count = 0 
for num in point:
    data['name'].append(num)
    data['-1分'].append(point[num][3])
    data['0分'].append(point[num][2])
    data['2分'].append(point[num][0])
    data['1分'].append(point[num][1])
    data['总个数'].append(sum(point[num]))
    _count += 1
    _index.append(_count)
df =pandas.DataFrame(data,index=_index,columns=['name','-1分','0分','1分','2分','总个数'])




fig =px.bar(df.sort_values(by='总个数',ascending=False),x = "name",y = ['-1分','0分','1分','2分'] ,title="OB积极性统计",hover_data=['总个数'])
fig.show()



