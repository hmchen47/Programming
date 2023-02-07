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
  - `parse_args` method: get argument values
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
    print(args)
    print(args.address)
    print(args.jsonauth)
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

    $ python3 googleindex05.py --address test.html --jsonauth google.json
    Namespace(address='test.html', jsonauth='google.json', verbosity=True)
    test.html
    google.json
    ```


- The `dest` property
  - modified property name
  - code snippet

    ```python
    # arguments/googleindex06.py
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

    args = parser.parse_args()
    print(args)
    print(args.jfile)
    ```

  - result: 

    ```sh
    $ ./googleindex06.py --address test.html --jsonauth google.json
    Namespace(address='test.html', jfile='google.json', verbosity=True)
    google.json
    ```


- Specifying argument datatype
  - forcing a datatype when defining an argument
  - property to define datatype: `type=<datatype>`
  - code snippet

    ```pythonc
    import argparse

    parser = argparse.ArgumentParser()
    ...
    parser.add_argument("--year", type=int, default=2020, help="Year extraction")
    ...
    ```

  - result

    ```sh
    $ ./googleindex07.py --address test.html --jsonauth google.json
    Namespace(address='test.html', jfile='google.json', verbosity=True, year=2020)
    google.json
    ```


- Short and log arguments
  - syntax to combine long and short arguments: `add_argument('short-option', 'log-option', ...)`
  - code snippet

    ```python
    # arguments/googleindex08.py
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--address", help="URL to be checked", required=True)
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
    if args.year:
        print("Current year selected")
    ```

  - result

    ```sh
    $ ./googleindex08.py --address test.html --jsonauth google.json --year 2021
    Current year selected
    
    $ ./googleindex08.py --help
    usage: googleindex08.py [-h] -a ADDRESS [-j JFILE] [-y YEAR] [-v]

    options:
      -h, --help            show this help message and exit
      -a ADDRESS, --address ADDRESS
                            URL to be checked
      -j JFILE, --jsonauth JFILE
                            JSON Google Authentication file path
      -y YEAR, --year YEAR  Year extraction
      -v, --verbosity       Verbosity
    ```


- The `nargs` option
  - restreving multiple values for an arguments
    - syntax: `nargs=<int value>`
    - `nargs=*`: unspecified number of values
    - `nargs=n`" reading `n` number of values
  - example: `./googleindex.py --address url1.htm url2.html`
  - code snippet

    ```python
    # arguments/googleindex09.py
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-a", "--address", nargs="*", help="URL to be checked", required=True
    )
    ...

    args = parser.parse_args()
    print(args.address)
    print(type(args.address))
    ```

  - results

    ```sh
    # nargs="*"
    $ ./googleindex09.py --address utl1.html url2.html
    ['utl1.html', 'url2.html']
    <class 'list'>

    # nargs=3
    $ ./googleindex09.py --address url1.html url2.html
    usage: googleindex09.py [-h] -a ADDRESS ADDRESS ADDRESS [-j JFILE] [-y YEAR] [-v]
    googleindex09.py: error: argument -a/--address: expected 3 arguments
    ```


- Parent arguments
  - sharing same 'parent' arguments
  - just adding 'child' arguments
  - code snippets

    ```python
    # arguments/googleindex10a.py (parent script)
    import argparse

    def get_parser(h):
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

    # arguments/googleindex10a.py (child script)
    import argparse
    import googleindex10a

    def main(p):
        child_parsser = argparse.ArgumentParser(parents=[p], add_help=True)
        child_parser.add_argument("-l", "lang", help="Language")
        args = child_parser.parse_args()

    if __name__ == "__main__":
        p = googleindex10a.get_parser(h=False)
        main(p)
    ```

  - result

    ```sh
    $ ./googleindex10b.py --help
    usage: googleindex10b.py [-h] -a [ADDRESS ...] [-j JFILE] [-l LANG]

    options:
      -h, --help            show this help message and exit
      -a [ADDRESS ...], --address [ADDRESS ...]
                            URL to be checked
      -j JFILE, --jsonauth JFILE
                            JSON Google Authentication file path, default $HOME/google-auth.json
      -l LANG, --lang LANG  Language
    ```



## The `getopt` Package




## Conclusion







