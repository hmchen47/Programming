#!/usr/bin/env python3

import getopt
import sys


def usage():
    """print the comand line options of the program"""
    print(
        f"Usage : {sys.argv[0]} --address <url> --jsonauth <json auth file path> --year <year selected> --version --help"
    )
    exit()


address = False
jsonauth = "/home/sqlpac/google.json"
year = 2020
version = "1.0"

options, args = getopt.getopt(
    sys.argv[1:], "a:j:y:h:v", ["address=", "jsonauth=", "year=", "help", "version"]
)

for opt, arg in options:
    if opt in ("-a", "--address"):
        address = arg
    elif opt in ("-j", "--jsonauth"):
        jsonauth = arg
    elif opt in ("-y", "--year"):
        year = arg
    elif opt in ("-v", "--version"):
        print(version)
        exit()
    elif opt in ("-h", "--help"):
        usage()

if not address:
    print("Address required")
    usage()
