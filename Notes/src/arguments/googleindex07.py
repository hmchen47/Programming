#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--address", help="URL to be checked", required=True)
parser.add_argument(
    "--jsonauth",
    default="/home/sqlpac/google-auth.json",
    dest="jfile",
    help="JSON Google Authentication file path",
)
parser.add_argument("--verbosity", help="Verbosity", action="store_false")
parser.add_argument("--year", type=int, default=2020, help="Year extraction")

args = parser.parse_args()
print(args)
print(args.jfile)
