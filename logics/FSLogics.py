import requests
import json
import sys
import os
import urllib.parse
import pandas as pd

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
sys.path.insert(1, './transformers')
import DataUtils
import StdResponses
import AuthResponses
import FSTransformers
import logging

def get_file_list_url(fspath, dsmversion, sid):
    CgiModule = "/webapi/entry.cgi?"
    UrlParameters = ""
    Headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    if dsmversion=="7.0":

        additional=["real_path","size","owner","time","perm","type","mount_point_type","description","indexed"]

        params = {
        "api":"SYNO.FileStation.List",
        "version":"2",
        "method":"list",
        "folder_path":fspath,
        "offset": 0,
        "limit": 1000,
        "sort_by": "size",
        "sort_direction": "ASC",
        "action": "list",
        "check_dir": "true",
        "filetype": "all",
        "additional":additional,
        "_sid":sid
        }
    else:
        return False,"",Headers

    EncodedURI = urllib.parse.urlencode(params).replace("%27","%22").replace("+%22","%22")
    UrlParameters = CgiModule+EncodedURI
    return True,UrlParameters,Headers

def listFiles(fspath,outputFormat,sessionname):
    OutputFormat = 0
    url = DataUtils.GetUrl(sessionname)
    SID = DataUtils.GetAuthToken(sessionname)
    DSMVERSION = DataUtils.GetDSMVersion(sessionname)

    IsVersionSupported,URLParams,headers = get_file_list_url(fspath,DSMVERSION,SID)

    if not IsVersionSupported:
        logging.debug("Unsupported DSM Version: {}".format(DSMVERSION))
        print("Unsupported DSM Version")
        exit(1)

    FULLURL = urllib.parse.urljoin(url, URLParams)

    response = requests.request("GET", FULLURL, data=None, headers=headers)
    isAPICallOK = StdResponses.processAPIResponse(response)
    if(not isAPICallOK):
        exit(99)
    else:
        json_object = json.loads(response.text)
        if (outputFormat == "DF"):
            #print(json_object)
            aDF = FSTransformers.GetListAsCsv(json_object)
            print(aDF)
        elif (outputFormat == "CSV"):
            #print(json_object)
            aDF = FSTransformers.GetListAsCsv(json_object)
            print(aDF.to_csv(index=False))
        else:
            #print(json_object)
            json_formatted_str = json.dumps(json_object, indent=2)
            print(json_formatted_str)
