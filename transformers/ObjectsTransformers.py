import json
import pandas as pd

def GetObjectListAsCsv(jsonResults):
    #{'page': {'offset': 0, 'total': 1, 'totalFilter': 1}, 'list': [{'id': '1', 'type': 'ATTENDED_BOT_RUNNER', 'hostName': 'EC2AMAZ-4PFQG1I', 'userId': '', 'userName': '', 'status': 'CONNECTED',
    # 'poolName': '', 'fullyQualifiedHostName': '-', 'updatedBy': 'iqbot', 'updatedOn': '2019-11-18T05:35:39.154Z'}]}

    out_df = pd.DataFrame(columns=['id','parentId','name','path','type','desc'])

    DeviceList = jsonResults['list']
    for device in DeviceList:
        ID = device['id']
        PARENTID = device['parentId']
        NAME = device['name']
        PATH = device['path']
        DESCRIPTION = device['description']
        TYPE = device['type']

        new_row = {'id':ID,'parentId':PARENTID,'name':NAME,'path':PATH,'type':TYPE,'desc':DESCRIPTION}
        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)
