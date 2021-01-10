import json
import pandas as pd

def GetDeviceListAsCsv(jsonResults):
    #{'page': {'offset': 0, 'total': 1, 'totalFilter': 1}, 'list': [{'id': '1', 'type': 'ATTENDED_BOT_RUNNER', 'hostName': 'EC2AMAZ-4PFQG1I', 'userId': '', 'userName': '', 'status': 'CONNECTED',
    # 'poolName': '', 'fullyQualifiedHostName': '-', 'updatedBy': 'iqbot', 'updatedOn': '2019-11-18T05:35:39.154Z'}]}

    out_df = pd.DataFrame(columns=['id','type','hostName','userId','userName','status','poolName','fullyQualifiedHostName','updatedBy','updatedOn'])

    DeviceList = jsonResults['list']
    for device in DeviceList:
        ID = device['id']
        TYPE = device['type']
        HOST = device['hostName']
        USERID = device['userId']
        USERNAME = device['userName']
        STATUS = device['status']
        POOLNAME = device['poolName']
        FQDN = device['fullyQualifiedHostName']
        UPDATEDBY = device['updatedBy']
        UPDATEDON = device['updatedOn']

        new_row = {'id':ID,'type':TYPE,'hostName':HOST,'userId':USERID,'userName':USERNAME,'status':STATUS,'poolName':POOLNAME,'fullyQualifiedHostName':FQDN,'updatedBy':UPDATEDBY,'updatedOn':UPDATEDON}
        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)
