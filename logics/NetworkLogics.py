import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import StdResponses
import AuthResponses
import logging

logging.basicConfig(level=logging.ERROR)
logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)

def get_network_url(dsmversion, sid):
    ROOT = "/webapi/entry.cgi?"
    CgiModule=""
    UrlParameters=""
    Headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    if dsmversion=="7.0":
        CgiModule = "/webapi/auth.cgi?"
        composite=[
        {"api":"SYNO.Core.CMS.Info","method":"get","version":1,"additional":["gluster_role"]},
        {"api":"SYNO.Core.Network.Bond","method":"list","version":2},
        {"api":"SYNO.Core.Network.Ethernet","method":"list","version":2},
        {"api":"SYNO.Core.Network.PPPoE","method":"list","version":1},
        {"api":"SYNO.Core.Network.VPN.PPTP","method":"list","version":1,"additional":["status"]},
        {"api":"SYNO.Core.Network.VPN.OpenVPNWithConf","method":"list","version":1,"additional":["status"]},
        {"api":"SYNO.Core.Network.VPN.OpenVPN","method":"list","version":1,"additional":["status"]},
        {"api":"SYNO.Core.Network.VPN.L2TP","method":"list","version":1,"additional":["status"]}
        ]

        params = {
        "api":"SYNO.Entry.Request",
        "version":"1",
        "method":"request",
        "stopwhenerror":"false",
        "compound":composite,
        "_sid":sid
        }

    else:
        return False,UrlParameters,Headers

    EncodedURI = urllib.parse.urlencode(params).replace("%27","%22").replace("+%22","%22")
    UrlParameters = ROOT+EncodedURI
    return True,UrlParameters,Headers

def get_network_info(sessionname):

    url = DataUtils.GetUrl(sessionname)
    SID = DataUtils.GetAuthToken(sessionname)
    DSMVERSION = DataUtils.GetDSMVersion(sessionname)

    IsVersionSupported,URLParams,headers = get_network_url(DSMVERSION,SID)

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
