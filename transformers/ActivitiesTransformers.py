import json
import pandas as pd

def GetListAsCsv(jsonResults):

    out_df = pd.DataFrame(columns=['deviceName','automationName','jobName','jobFilePath','jobType','currentBotName',
    'startDateTime','endDateTime','command','jobExecutionStatus','progress','scheduleId','userId','deviceId','id',
    'currentLine','totalLines','jobId','tenantId','modifiedBy','createdBy','modifiedOn','deploymentId',
    'queueName','queueId','rdpEnabled','message','canManage','jobExecutionDetails','username','source'])

    ItemList = jsonResults['list']
    for item in ItemList:

        a1 = item['deviceName']
        a2 = item['automationName']
        a3 = item['jobName']
        a4 = item['jobFilePath']
        a5 = item['jobType']
        a6 = item['currentBotName']

        a7 = item['startDateTime']
        a8 = item['endDateTime']
        a9 = item['command']
        b1 = item['jobExecutionStatus']
        b2 = item['progress']
        b3 = item['scheduleId']
        b4 = item['userId']
        b5 = item['deviceId']
        b6 = item['id']

        b7 = item['currentLine']
        b8 = item['totalLines']
        b9 = item['jobId']
        c1 = item['tenantId']
        c2 = item['modifiedBy']
        c3 = item['createdBy']
        c4 = item['modifiedOn']
        c5 = item['deploymentId']

        c6 = item['queueName']
        c7 = item['queueId']
        c8 = item['rdpEnabled']
        c9 = "" #item['message']
        d1 = item['canManage']
        d2 = item['jobExecutionDetails']
        d3 = item['username']
        d4 = item['source']

        new_row = {'deviceName':a1,'automationName':a2,'jobName':a3,'jobFilePath':a4,'jobType':a5,'currentBotName':a6,
        'startDateTime':a7,'endDateTime':a8,'command':a9,'jobExecutionStatus':b1,'progress':b2,'scheduleId':b3,'userId':b4,'deviceId':b5,'id':b6,
        'currentLine':b7,'totalLines':b8,'jobId':b9,'tenantId':c1,'modifiedBy':c2,'createdBy':c3,'modifiedOn':c4,'deploymentId':c5,
        'queueName':c6,'queueId':c7,'rdpEnabled':c8,'message':c9,'canManage':d1,'jobExecutionDetails':d2,'username':d3,'source':d4}

        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)
