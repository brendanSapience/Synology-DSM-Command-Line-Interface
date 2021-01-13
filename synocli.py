##############################################################
#
# Author: Bren Sapience
# Date: Jan 2021
# Scope:
#
#
##############################################################
#!/usr/bin/env python3

import argparse
import sys
import logging
sys.path.insert(1, './logics')
sys.path.insert(1, './libs')
import AuthLogics
import NetworkLogics
import PackageLogics
import DSMLogics
import DataUtils

VERSION="0.0.1"
DEFAULT_DSM_VERSION = "7.0"
SupportedDSMVersions = ["7.0"]

logging.basicConfig(level=logging.ERROR)

#####
# General Parser
#####

parser = argparse.ArgumentParser()
parser.add_argument('-v','--version', action='version', version=VERSION)
parser.add_argument('-s','--session',type=str,default="", help='Session Name',dest="SESSIONNAME")
parser.add_argument('-f','--format',type=str,default="JSON", help='Output Format <JSON,CSV,DF>',dest="OUTPUTFORMAT")
subparsers = parser.add_subparsers()

#####
# AUTH Parser
# Authentication commands
# auth <login,logout,list>
#####

def login(args):
    if not args.LOGIN:
        parser.error('no login passed')
    if not args.PWD:
        parser.error('no password passed')
    if not args.URL:
        parser.error('no url passed')
    if not args.SESSIONNAME:
        args.SESSIONNAME = DataUtils.RandomSessionNameGenerator()
    AuthLogics.login(args.DSMVERSION,args.URL,args.LOGIN,args.PWD,args.SESSIONNAME)

def logout(args):
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    AuthLogics.logout(args.SESSIONNAME)

def listsessions(args):
    AuthLogics.listSessions()

auth_parser = subparsers.add_parser('auth')
auth_subparsers = auth_parser.add_subparsers()

# auth login
login_parser = auth_subparsers.add_parser('login')
login_parser.add_argument('-u','--user',type=str,default="", help='DSM Login', dest="LOGIN")
login_parser.add_argument('-p', '--pwd',type=str,default="", help='DSM Password', dest="PWD")
login_parser.add_argument('-r', '--url',type=str,default="", help='DSM URL',dest="URL")
login_parser.add_argument('-v', '--version',type=str,default=DEFAULT_DSM_VERSION, help='DSM Version',dest="DSMVERSION")
#login_parser.add_argument('-s', '--session',type=str,default="", help='Session Name',dest="SESSIONNAME")
login_parser.set_defaults(func=login)

# auth logout
login_parser = auth_subparsers.add_parser('logout')
#login_parser.add_argument('-s', '--session',type=str,default="", help='Session Name',dest="SESSIONNAME")
login_parser.set_defaults(func=logout)

# auth list
sesslist_parser = auth_subparsers.add_parser('list')
sesslist_parser.set_defaults(func=listsessions)

#####
# NETWORK Parser
# network <show>
#####

def network(args):
    network_show_supported_ops = ['OpenVPN','OpenVPNWithConf','L2TP','PPTP','PPPoE','Ethernet','Bond','CMS']
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    if args.NETWORKCONFITEM not in network_show_supported_ops:
        parser.error('Conf Item not supported.')
    NetworkLogics.get_network_info(args.NETWORKCONFITEM,args.SESSIONNAME,args.OUTPUTFORMAT)

# Network cxommands
network_parser = subparsers.add_parser('network')
network_subparsers = network_parser.add_subparsers()

# network show

network_show_parser = network_subparsers.add_parser('show')
network_show_parser.add_argument('--type','-t',type=str,default="OpenVPNWithConf", help='Network Conf Item <OpenVPN,OpenVPNWithConf,L2TP,PPTP,PPPoE,Ethernet,Bond,CMS>',dest="NETWORKCONFITEM")
network_show_parser.set_defaults(func=network)

#####
# PACKAGE Parser
# package <list,start,stop>
#####

def package_list(args):
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    PackageLogics.listPackages(args.OUTPUTFORMAT,args.SESSIONNAME)

def package_start(args):
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    if not args.PCKNAME:
        parser.error('no package name passed')
    PackageLogics.stopOrStartPackage(args.PCKNAME,"start",args.SESSIONNAME)

def package_stop(args):
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    if not args.PCKNAME:
        parser.error('no package name passed')
    PackageLogics.stopOrStartPackage(args.PCKNAME,"stop",args.SESSIONNAME)


# Package commands
package_parser = subparsers.add_parser('package')
package_subparsers = package_parser.add_subparsers()

# package list
package_list_parser = package_subparsers.add_parser('list')
#package_list_parser.add_argument('--session','-s',type=str,default="", help='Session Name',dest="SESSIONNAME")
package_list_parser.set_defaults(func=package_list)

# package start
package_start_parser = package_subparsers.add_parser('start')
#package_start_parser.add_argument('--session','-s',type=str,default="", help='Session Name',dest="SESSIONNAME")
package_start_parser.add_argument('--name','-n',type=str,default="", help='Package Name',dest="PCKNAME")
package_start_parser.set_defaults(func=package_start)

# package stop
package_stop_parser = package_subparsers.add_parser('stop')
#package_stop_parser.add_argument('--session','-s',type=str,default="", help='Session Name',dest="SESSIONNAME")
package_stop_parser.add_argument('--name','-n',type=str,default="", help='Package Name',dest="PCKNAME")
package_stop_parser.set_defaults(func=package_stop)


#####
# DSM Parser
# dsm <list,start,stop>
#####

def dsm_records_list(args):
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    DSMLogics.listTorrents(args.OUTPUTFORMAT,args.SESSIONNAME)


# Package commands
dsm_parser = subparsers.add_parser('dsm')
dsm_subparsers = dsm_parser.add_subparsers()

# package list
dsm_list_parser = dsm_subparsers.add_parser('list')
#package_list_parser.add_argument('--session','-s',type=str,default="", help='Session Name',dest="SESSIONNAME")
dsm_list_parser.set_defaults(func=dsm_records_list)


if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
