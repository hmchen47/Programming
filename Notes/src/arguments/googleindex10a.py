#!/usr/bin/env python3

import argparse


def get_parser(h):
    """get arguments"""
    parser = argparse.ArgumentParser(add_help=h)

    parser.add_argument(
        "-a", "--address", nargs="*", help="URL to be checked", required=True
    )
    parser.add_argument(
        "-j",
        "--jsonauth",
        default="/home/sqlpac/google-auth.json",
        dest="jfile",
        help="JSON Google Authentication file path, default $HOME/google-auth.json",
    )

    return parser


if __name__ == "__main__":
    p = get_parser(h=True)
    args = p.parse_args()
