import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import AuthResponses
import logging

logging.basicConfig(level=logging.ERROR)
logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)

def get_package_list_url(dsmversion, sid):
    ROOT = "/webapi/entry.cgi?"
    if dsmversion==7:

        additional=[
        "description",
        "description_enu",
        "beta",
        "distributor",
        "distributor_url",
        "maintainer",
        "maintainer_url",
        "dsm_apps",
        "dsm_app_page",
        "dsm_app_launch_name",
        "report_beta_url",
        "support_center",
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
        return False,""

    EncodedURI = urllib.parse.urlencode(params).replace("%27","%22").replace("+%22","%22")

    #EncodedURI = urllib.parse.quote(params)
    URLPARAMS = ROOT+EncodedURI
    return True,URLPARAMS

def get_package_list(sessionname):
    url = DataUtils.GetUrl(sessionname)
    SID = DataUtils.GetAuthToken(sessionname)
    DSMVERSION = DataUtils.GetDSMVersion(sessionname)
    #DSMVERSION=7
    VersionSupported,RES = get_package_list_url(DSMVERSION,SID)

    if not VersionSupported:
        logging.debug("Unsupported DSM Version: {}".format(DSMVERSION))
        print("Unsupported DSM Version")
        exit(1)

    URL = urllib.parse.urljoin(url, RES)
    #print(URL)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", URL, data=None, headers=headers)
    if(response.status_code != 200):
        logging.debug("DSM API Error: {}".format(response.status_code))
        print("API Error Code: "+str(response.status_code))
        exit(99)
    else:
        #print(response.text)
        json_object = json.loads(response.text)

        json_formatted_str = json.dumps(json_object, indent=2)

        print(json_formatted_str)

        isError,Code = AuthResponses.Process_Auth_Login_Response(response)
        if(not isError):
            print("OK!")
