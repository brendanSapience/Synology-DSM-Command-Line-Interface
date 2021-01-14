import json
import pandas as pd
import logging
import sys

sys.path.insert(1, './libs')
import ConvUtils

def GetListAsCsv(jsonResults):

    #myDF = pd.DataFrame(jsonResults['data']["task"])
    #myDF.pop('additional')
    #print(myDF)

    ItemList = jsonResults['data']['task']
    AllRows = []
    for item in ItemList:

        #print(item["additional"]["detail"])
        details = item["additional"]["detail"]

        id = item["id"]
        size = item["size"]
        status = item["status"]
        title = item["title"]
        type = item["type"]
        username = item["username"]

        completedTime = details['completed_time']
        connectedLeech = details['connected_leechers']
        connectedPeers = details['connected_peers']
        createdTime = details['created_time']
        dest = details['destination']
        startTime = details['started_time']

        transferItems = item["additional"]["transfer"]
        speedDownload = transferItems['speed_download']
        sizeDownloaded = transferItems['size_downloaded']
        speedUpload = transferItems['speed_upload']

        if(completedTime != 0):
            completedTime=ConvUtils.epoch_to_hr(completedTime)

        new_row = {
        'id':id,
        'size':ConvUtils.sizeof_fmt(size),
        'status':status,
        'title':title,
        'type':type,
        'username':username,
        'completedTime':completedTime,
        'Leech':connectedLeech,
        'Peers':connectedPeers,
        'Created':ConvUtils.epoch_to_hr(createdTime),
        'Dest':dest,
        'StartTime':ConvUtils.epoch_to_hr(startTime),
        'DLSpeed':ConvUtils.sizeof_fmt(speedDownload,"B/s"),
        'ULSpeed':ConvUtils.sizeof_fmt(speedUpload,"B/s"),
        'Downloaded':ConvUtils.sizeof_fmt(sizeDownloaded)
        }
        AllRows.append(new_row)

    myDFAdditional = pd.DataFrame(AllRows)

    return myDFAdditional
