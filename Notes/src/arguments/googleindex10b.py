#!/usr/bin/env python3

import argparse

import googleindex10a


def main(p):
    """child parser to utilize parent's arguments"""
    child_parser = argparse.ArgumentParser(parents=[p], add_help=True)
    child_parser.add_argument("-l", "--lang", help="Language")
    args = child_parser.parse_args()


if __name__ == "__main__":
    p = googleindex10a.get_parser(h=False)
    main(p)
