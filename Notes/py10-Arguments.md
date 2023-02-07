# Python, Parsing arguments with the packages `argparse` and `getopt`

Institute: SQLpac

Date: 2020-04-14

[Original](https://www.sqlpac.com/en/documents/python-parsing-arguments-packages-argparse-getopt.html)


## Introduction

- Prerequisite
  - creating a program `googleindex.py`: getting the indexing status for a given URL w/ 1 arghs
  - syntax: `python3 googleindex.py --address <url> [, --jsonauth <path to json auth file>]`
  - 1st arg: `--address` required
  - 2nd arg: `--jsonauth` optional
  - short options required: `python3 googleindex.py --a <url> [, --j <path to json auth file>]`


## The `sys.argv` Arrays

- Accessing args w/ system array
  - `sys.argv`:
    - the native system array for args
    - a public global variable
  - `sys.argv[0]`: the script name
  - code snippet

    ```python
    # arguments/googleindex01.py
    import sys

    print(f"Script name: {sys.argv[0]}")
    print(f"First argument: {sys.argv[1]}")
    print(f"Second argument: {sys.argv[2]}")
    ```

  - result

    ```shell
    $ python3 googleindex01.py test.html google.json
    Script name: googleindex01.py
    First argument: test.html
    Second argument: google.json
    ```


- Error handling of `sys.argv`
  - code snippet

    ```python
    # arguments/googleindex02.py
    import sys

    try:
        arg = sys.argv[2]
    except IndexError:
        raise SystemExit(f"Usage : {sys.argv[0]} url json")
    ```

  - results

    ```sh
    $ python3 googleindex02.py test.html google.json
    $ python3 googleindex02.py test.html
    Usage : googleindex02.py url json
    ```


- Libraries to handle CLI in Python
  - `sys.argv` array:
    - each string as an **argument**
    - becoming complex
  - [argparse](https://docs.python.org/3/library/argparse.html)
  - [getopt](https://docs.python.org/3/library/getopt.html)


## The `argparse` Package

- Initiating object of `argparse`
  - initiating instance: `parser`
  - program name property: `parser.prog`
  - code snippet

    ```python
    # arguments/googleindex03.py
    import argparse
    parse = argparse.ArgumentParser()
    print(parser.prog)
    ```

  - result

    ```shell
    $ python3 googleindex03.py
    googleindex03.py
    ```


- Adding arguments
  - method: `add_argument`
    - `required=true`: mandatory argument
    - `action="store_true | store_false"`:
      - a boolean constant value
      - not present: `False`
      - present: `True`
  - code snippet

    ```python
    # arguments/googleindex04.py
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--address", help="URL to be checked", required=True)
    parser.add_argument("--jsonauth", help="JSON Google Authentication file path")
    parser.add_argument("--verbosity", help="Verbosity", action="store_false")
    ```


- Adding default value for optional argument
  - code snippet

    ```python
    # arguments/googleindex05.py
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
    print(args.accumulate(args.integers))
    ```

  - results

    ```shell
    $ python3 googleindex05.py
    usage: googleindex05.py [-h] --address ADDRESS [--jsonauth JSONAUTH] [--verbosity]
    googleindex05.py: error: the following arguments are required: --address

    $ python3 googleindex05.py --help
    usage: googleindex05.py [-h] --address ADDRESS [--jsonauth JSONAUTH] [--verbosity]

    options:
      -h, --help           show this help message and exit
      --address ADDRESS    URL to be checked
      --jsonauth JSONAUTH  JSON Google Authentication file path
      --verbosity          Verbosity
    ```






## The `getopt` Package




## Conclusion







