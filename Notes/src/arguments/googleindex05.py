#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--address", help="URL to be checked", required=True)
parser.add_argument(
    "--jsonauth",
    default="/home/sqlpac/google-auth.json",
    help="JSON Google Authentication file path",
)
parser.add_argument("--verbosity", help="Verbosity", action="store_false")

args = parser.parse_args()
print(args)
print(args.address)
print(args.jsonauth)
# print(args.accumulate(args.integers))
