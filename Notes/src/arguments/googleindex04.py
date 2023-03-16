#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--address", help="URL to be checked", required=True)
parser.add_argument("--jsonauth", help="JSON Google Authentication file path")
parser.add_argument("--verbosity", help="Verbosity", action="store_false")
