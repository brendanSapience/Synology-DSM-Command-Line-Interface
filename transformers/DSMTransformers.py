import json
import pandas as pd
import logging


def GetListAsCsv(jsonResults):

    myDF = pd.DataFrame(jsonResults['data']["task"])
    myDF.pop('additional')
    #print(myDF)

    ItemList = jsonResults['data']['task']
    AllRows = []
    for item in ItemList:

        #print(item["additional"]["detail"])
        details = item["additional"]["detail"]

        id = item["id"]
        completedTime = details['completed_time']
        connectedLeech = details['connected_leechers']
        connectedPeers = details['connected_peers']
        createdTime = details['created_time']
        dest = details['destination']
        startTime = details['started_time']

        transferItems = "0"
        speedDownload = "0"
        sizeDownloaded = "0"
        speedUpload = "0"

        if("transfer" in item["additional"]):
            transferItems = item["additional"]["transfer"]
            speedDownload = transferItems['speed_download']
            sizeDownloaded = transferItems['size_downloaded']
            speedUpload = transferItems['speed_upload']

        new_row = {'id':id,'completedTime':completedTime,'connectedLeech':connectedLeech,'connectedPeers':connectedPeers,'createdTime':createdTime,'dest':dest,'startTime':startTime,'speedDownload':speedDownload}
        AllRows.append(new_row)

    myDFAdditional = pd.DataFrame(AllRows)
    #print(myDFAdditional)

    FinalDF = pd.merge(myDF, myDFAdditional, on = "id", how = "inner")

    return FinalDF
