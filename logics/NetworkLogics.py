import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
sys.path.insert(1, './transformers')
import DataUtils
import StdResponses
import AuthResponses
import NetworkTransformers
import logging

# Deprecated
def get_network_url(dsmversion, sid):
    CgiModule = "/webapi/entry.cgi?"
    UrlParameters = ""
    Headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    if dsmversion=="7.0":
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
    UrlParameters = CgiModule+EncodedURI
    return True,UrlParameters,Headers

def get_network_url(networkconfitem,dsmversion,sid):
    CgiModule = "/webapi/entry.cgi?"
    UrlParameters = ""
    Headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    if dsmversion=="7.0":
        if(networkconfitem == "CMS"):
            params = {"api":"SYNO.Core.CMS.Info","method":"get","version":1,"additional":["gluster_role"],"_sid":sid}

        if(networkconfitem == "OpenVPNWithConf"):
            params = {"api":"SYNO.Core.Network.VPN.OpenVPNWithConf","method":"list","version":1,"additional":["status"],"_sid":sid}

        if(networkconfitem == "OpenVPN"):
            params = {"api":"SYNO.Core.Network.VPN.OpenVPN","method":"list","version":1,"additional":["status"],"_sid":sid}

        if(networkconfitem == "L2TP"):
            params = {"api":"SYNO.Core.Network.VPN.L2TP","method":"list","version":1,"additional":["status"],"_sid":sid}

        if(networkconfitem == "Bond"):
            params = {"api":"SYNO.Core.Network.Bond","method":"list","version":2,"_sid":sid}

        if(networkconfitem == "Ethernet"):
            params = {"api":"SYNO.Core.Network.Ethernet","method":"list","version":2,"_sid":sid}

        if(networkconfitem == "PPPoE"):
            params = {"api":"SYNO.Core.Network.PPPoE","method":"list","version":1,"_sid":sid}

        if(networkconfitem == "PPTP"):
            params = {"api":"SYNO.Core.Network.VPN.PPTP","method":"list","version":1,"additional":["status"],"_sid":sid}

    else:
        return False,UrlParameters,Headers

    EncodedURI = urllib.parse.urlencode(params).replace("%27","%22").replace("+%22","%22")
    UrlParameters = CgiModule+EncodedURI
    return True,UrlParameters,Headers


def get_network_info(networkconfitem,sessionname,outputFormat):

    url = DataUtils.GetUrl(sessionname)
    SID = DataUtils.GetAuthToken(sessionname)
    DSMVERSION = DataUtils.GetDSMVersion(sessionname)

    IsVersionSupported,URLParams,headers = get_network_url(networkconfitem,DSMVERSION,SID)

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
            aDF = NetworkTransformers.GetListAsCsv(json_object)
            print(aDF)
        elif (outputFormat == "CSV"):
            aDF = NetworkTransformers.GetListAsCsv(json_object)
            print(aDF.to_csv(index=False))
        else:
            json_formatted_str = json.dumps(json_object, indent=2)
            print(json_formatted_str)


        #DF = NetworkTransformers.GetListAsCsv(json_object)
        #print(DF)
