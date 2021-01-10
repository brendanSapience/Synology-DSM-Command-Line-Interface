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
import PackagesTransformers
import logging

def get_package_list_url(dsmversion, sid):
    CgiModule = "/webapi/entry.cgi?"
    UrlParameters = ""
    Headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    if dsmversion=="7.0":

        additional=[
        #"description",
        #"description_enu",
        "status",
        "beta",
        #"distributor",
        #"distributor_url",
        #"maintainer",
        #"maintainer_url",
        #"dsm_apps",
        #"dsm_app_page",
        #"dsm_app_launch_name",
        #"report_beta_url",
        #"support_center",
        "startable",
        "installed_info",
        "support_url",
        "is_uninstall_pages",
        "install_type",
        "autoupdate",
        "silent_upgrade",
        "installing_progress",
        "ctl_uninstall",
        "updated_at"
        ]

        params = {
        "api":"SYNO.Core.Package",
        "version":"2",
        "method":"list",
        "additional":additional,
        "_sid":sid
        }
    else:
        return False,"",Headers

    EncodedURI = urllib.parse.urlencode(params).replace("%27","%22").replace("+%22","%22")
    UrlParameters = CgiModule+EncodedURI
    return True,UrlParameters,Headers

def listPackages(outputFormat,sessionname):
    OutputFormat = 0
    url = DataUtils.GetUrl(sessionname)
    SID = DataUtils.GetAuthToken(sessionname)
    DSMVERSION = DataUtils.GetDSMVersion(sessionname)

    IsVersionSupported,URLParams,headers = get_package_list_url(DSMVERSION,SID)

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
            aDF = PackagesTransformers.GetListAsCsv(json_object)
            print(aDF)
        elif (outputFormat == "CSV"):
            aDF = PackagesTransformers.GetListAsCsv(json_object)
            print(aDF.to_csv(index=False))
        else:
            json_formatted_str = json.dumps(json_object, indent=2)
            print(json_formatted_str)


def get_change_package_state_url(packageName,operation,dsmversion, sid):
    CgiModule = "/webapi/entry.cgi?"
    UrlParameters = ""
    Headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    if dsmversion=="7.0":

        params = {
        "id": "\""+packageName+"\"",
        "api":"SYNO.Core.Package.Control",
        "version":"1",
        "method":operation,
        "_sid":sid
        }
    else:
        return False,"",Headers

    EncodedURI = urllib.parse.urlencode(params).replace("%27","%22").replace("+%22","%22")
    UrlParameters = CgiModule+EncodedURI
    #print(UrlParameters)
    return True,UrlParameters,Headers

def stopOrStartPackage(packageName,operation,sessionname):
    url = DataUtils.GetUrl(sessionname)
    SID = DataUtils.GetAuthToken(sessionname)
    DSMVERSION = DataUtils.GetDSMVersion(sessionname)

    IsVersionSupported,URLParams,headers = get_change_package_state_url(packageName,operation,DSMVERSION,SID)

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
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
