#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import requests
import sys
import signal

def SignalHandler(sig, frame):
    sys.stderr.write("\nCtrl-C detected, quitting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, SignalHandler)

requests.packages.urllib3.disable_warnings() 

def GetArguments():
    # Get some commandline arguments:
    argParser=argparse.ArgumentParser(description='Test an URL for a HTTP status code and echo the URL back to standard output if it matches a given status code.')
    argParser.add_argument('-e', '--echoredirect', help='Show which redirects have been found.', action="store_true")
    argParser.add_argument('-r', '--redirect', metavar="<enable | disable | both>", help='\'enable\' enables 301 redirects, \'disable\' disables 301 redirects, \'both\' tests for both (doubles the amount of queries!). Defaults to \'enable\')', default="enable")
    argParser.add_argument('-s', '--status', metavar="<status_code>", help='Only show URLs if this/these HTTP status code(s) are returned. Don\'t enter a code in 300 series as this code points to the destination. Separated status codes with a comma. Defaults to 200.')
    argParser.add_argument('-t', '--timeout', metavar="<seconds>", help='Defines the maximum time to wait before a connection times out. Defaults to 1 second.', default="1")
    return argParser

def GetHttpCode(sUrl, bRedirect):
    try:
        rHttp = requests.get(sUrl, timeout=int(lArgs.timeout), verify=False, allow_redirects=bRedirect)
        return rHttp
    except:
        return False
        pass

sArgParser=GetArguments()
lArgs=sArgParser.parse_args()

def main():
    if not lArgs.status:
        lStatus = ["200"]
    else:
        lStatus = lArgs.status.split(",")
    dResult = {}
    try:    # skip if binary values are given
        for strInput in sys.stdin:
            if len(strInput) > 8:   # len("https://") -> improve later on
                if lArgs.redirect == "enable" or lArgs.redirect == "both":
                    rHttp = GetHttpCode(strInput.strip(), True)
                    if str(rHttp.status_code) in lStatus:
                        if lArgs.echoredirect:
                            for resp in rHttp.history:
                                dResult[resp.url.strip()] = resp.url.strip()
                        else:
                            dResult[strInput.strip()] = strInput.strip()
                if lArgs.redirect == "disable" or lArgs.redirect == "both":
                    if str(GetHttpCode(strInput.strip(), False).status_code) in lStatus:
                        dResult[strInput.strip()] = strInput.strip()
    except UnicodeError:
        pass

    for x in sorted(dResult):
        print(x)
  
    
if __name__ == '__main__':
    main()  