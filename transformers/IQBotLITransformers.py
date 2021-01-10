import json
import pandas as pd

def GetLIDetailAsCsv(jsonResults):

    out_df = pd.DataFrame(columns=['stagingTotalGroups','stagingTotalBots','stagingDocumentsUnclassified',
    'stagingSuccessFiles','stagingFailedFiles','stagingAccuracy','stagingTestedFiles',
    'stagingPageCount','stagingSTP','productionTotalGroups','productionTotalBots',
    'productionDocumentsUnclassified','productionSuccessFiles','productionReviewFiles','productionInvalidFiles',
    'productionAccuracy','productionProcessedFiles','productionTotalFiles','productionPageCount',
    'productionSTP','pendingForReview','stagingTestedFilesPercentage','productionProcessedFilesPercentage'
        ])

    item = jsonResults['data']

    a1 = item['stagingTotalGroups']
    a2 = item['stagingTotalBots']
    a3 = item['stagingDocumentsUnclassified']

    a4 = item['stagingSuccessFiles']
    a5 = item['stagingFailedFiles']
    a6 = item['stagingAccuracy']
    a7 = item['stagingTestedFiles']

    a8 = item['stagingPageCount']
    a9 = item['stagingSTP']
    b1 = item['productionTotalGroups']
    b2 = item['productionTotalBots']

    b3 = item['productionDocumentsUnclassified']
    b4 = item['productionSuccessFiles']
    b5 = item['productionReviewFiles']
    b6 = item['productionInvalidFiles']

    b7 = item['productionAccuracy']
    b8 = item['productionProcessedFiles']
    b9 = item['productionTotalFiles']
    c1 = item['productionPageCount']

    c2 = item['productionSTP']
    c3 = item['pendingForReview']
    c4 = item['stagingTestedFilesPercentage']
    c5 = item['productionProcessedFilesPercentage']

    new_row = {
            'stagingTotalGroups':a1,'stagingTotalBots':a2,'stagingDocumentsUnclassified':a3,
            'stagingSuccessFiles':a4,'stagingFailedFiles':a5,'stagingAccuracy':a6,'stagingTestedFiles':a7,
            'stagingPageCount':a8,'stagingSTP':a9,'productionTotalGroups':b1,'productionTotalBots':b2,
            'productionDocumentsUnclassified':b3,'productionSuccessFiles':b4,'productionReviewFiles':b5,'productionInvalidFiles':b6,
            'productionAccuracy':b7,'productionProcessedFiles':b8,'productionTotalFiles':b9,'productionPageCount':c1,
            'productionSTP':c2,'pendingForReview':c3,'stagingTestedFilesPercentage':c4,'productionProcessedFilesPercentage':c5,
    }
    out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)



def GetLIGroupListAsCsv(jsonResults):

    out_df = pd.DataFrame(columns=['id','name','fileCount',
    'productionTotalCount','productionSTPCount','productionUnprocessedCount','productionPageCount',
    'stagingTotalCount','stagingSTPCount','stagingUnprocessedCount','stagingPageCount',
        ])

    ItemList = jsonResults['data']['categories']
    for item in ItemList:
        a1 = item['id']
        a2 = item['name']
        a3 = item['fileCount']

        a4 = item['productionFileDetails']['totalCount']
        a5 = item['productionFileDetails']['totalSTPCount']
        a6 = item['productionFileDetails']['unprocessedCount']
        a7 = item['productionFileDetails']['pageCount']

        a8 = item['stagingFileDetails']['totalCount']
        a9 = item['stagingFileDetails']['totalSTPCount']
        b1 = item['stagingFileDetails']['unprocessedCount']
        b2 = item['stagingFileDetails']['pageCount']

        new_row = {
            'id':a1,'name':a2,'fileCount':a3,
            'productionTotalCount':a4,'productionSTPCount':a5,'productionUnprocessedCount':a6,'productionPageCount':a7,
            'stagingTotalCount':a8,'stagingSTPCount':a9,'stagingUnprocessedCount':b1,'stagingPageCount':b2
        }
        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)

def GetFileListPerStatusAsCsv(jsonResults):
    out = ''
    for item in jsonResults:
        if item:
            if out == '':
                out = item
            else:
                out = out + ',' + item
    return out
    
def GetLIFileListAsCsv(jsonResults):

    out_df = pd.DataFrame(columns=['fileId','projectId','fileName','fileLocation','fileSize','fileHeight','fileWidth',
        'format','processed','classificationId','uploadrequestId','layoutId','isProduction'])

    ItemList = jsonResults['data']
    for item in ItemList:
        a1 = item['fileId']
        a2 = item['projectId']
        a3 = item['fileName']
        a4 = item['fileLocation']
        a5 = item['fileSize']
        a6 = item['fileHeight']
        a7 = item['fileWidth']
        a8 = item['format']
        a9 = item['processed']
        b1 = item['classificationId']
        b2 = item['uploadrequestId']
        b3 = item['layoutId']
        b4 = item['isProduction']

        new_row = {
            'fileId':a1,'projectId':a2,'fileName':a3,'fileLocation':a4,'fileSize':a5,'fileHeight':a6,'fileWidth':a7,
            'format':a8,'processed':a9,'classificationId':b1,'uploadrequestId':b2,'layoutId':b3,'isProduction':b4
        }
        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)


def GetLIListAsCsv(jsonResults):

            #"ocrEngineDetails": [
            #    {
            #        "id": "3",
            #        "name": null,
            #        "engineType": "Abbyy"
            #    }
            #],

    out_df = pd.DataFrame(columns=['id','name','description','organizationId','projectTypeId','projectType','confidenceThreshold',
        'numberOfFiles','numberOfCategories','unprocessedFileCount','primaryLanguage','accuracyPercentage','visionBotCount',
        'currentTrainedPercentage','totalStagingPageCount','totalProductionPageCount','projectState','environment','updatedAt',
        'createdAt','ocrEngineID','ocrEngineType'])

    ItemList = jsonResults['data']
    for item in ItemList:
        a1 = item['id']
        a2 = item['name']
        a3 = item['description']
        a4 = item['organizationId']
        a5 = item['projectTypeId']
        a6 = item['projectType']
        a7 = item['confidenceThreshold']
        a8 = item['numberOfFiles']
        a9 = item['numberOfCategories']
        b1 = item['unprocessedFileCount']
        b2 = item['primaryLanguage']
        b3 = item['accuracyPercentage']
        b4 = item['visionBotCount']
        b5 = item['currentTrainedPercentage']
        b6 = item['totalStagingPageCount']
        b7 = item['totalProductionPageCount']
        b8 = item['projectState']
        b9 = item['environment']
        c1 = item['updatedAt']
        c2 = item['createdAt']
        c3 = item['ocrEngineDetails'][0]['id']
        c4 = item['ocrEngineDetails'][0]['engineType']


        new_row = {
            'id':a1,'name':a2,'description':a3,'organizationId':a4,'projectTypeId':a5,'projectType':a6,'confidenceThreshold':a7,
            'numberOfFiles':a8,'numberOfCategories':a9,'unprocessedFileCount':b1,'primaryLanguage':b2,'accuracyPercentage':b3,'visionBotCount':b4,
            'currentTrainedPercentage':b5,'totalStagingPageCount':b6,'totalProductionPageCount':b7,'projectState':b8,'environment':b9,'updatedAt':c1,
            'createdAt':c2,'ocrEngineID':c3,'ocrEngineType':c4
        }
        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)
