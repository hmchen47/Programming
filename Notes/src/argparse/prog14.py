#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument(
    "-v", "--verbose", action="count", default=0, help="increase output verbosity"
)
args = parser.parse_args()
answer = args.square**2
if args.verbose >= 2:
    print(f"the square of {args.square} equals to {answer}")
elif args.verbose == 1:
    print(f"{args.square}^2 = {answer}")
else:
    print(answer)
