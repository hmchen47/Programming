#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--address", nargs=3, help="URL to be checked", required=True)
parser.add_argument(
    "-j",
    "--jsonauth",
    default="/home/sqlpac/google-auth.json",
    dest="jfile",
    help="JSON Google Authentication file path",
)
parser.add_argument("-y", "--year", type=int, default=2020, help="Year extraction")
parser.add_argument("-v", "--verbosity", help="Verbosity", action="store_false")

args = parser.parse_args()
print(args.address)
print(type(args.address))
