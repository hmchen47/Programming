#!/usr/bin/env python3

import sys

try:
    arg = sys.argv[2]
except IndexError:
    raise SystemExit(f"Usage : {sys.argv[0]} url json")
