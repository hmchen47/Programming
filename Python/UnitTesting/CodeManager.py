#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# CodeManager.py
"""
TODO: Break check into two pieces?
TODO: update() is still only in test mode; doesn't actually work yet.

Extracts, displays, checks and updates code examples in restructured text (.rst)
files.

You can just put in the codeMarker and the (indented) first line (containing the
file path) into your restructured text file, then run the update program to
automatically insert the rest of the file.
"""
import os, re, sys, shutil, inspect, difflib

restFiles = [os.path.join(d[0], f) for d in os.walk(".") if not "_test" in d[0]
             for f in d[2] if f.endswith(".rst")]

class Languages:
    "Strategy design pattern"

    class Python:
        codeMarker = "::\n\n"
        commentTag = "#"
        listings = re.compile("::\n\n( {4}#.*(?:\n+ {4}.*)*)")

    class Java:
        codeMarker = "..  code-block:: java\n\n"
        commentTag = "//"
        listings = \
            re.compile(".. *code-block:: *java\n\n( {4}//.*(?:\n+ {4}.*)*)")

def shift(listing):
    "Shift the listing left by 4 spaces"
    return [x[4:] if x.startswith("    ") else x for x in listing.splitlines()]

# TEST - makes duplicates of the rst files in a test directory to test update():
dirs = set([os.path.join("_test", os.path.dirname(f)) for f in restFiles])
if [os.makedirs(d) for d in dirs if not os.path.exists(d)]:
    [shutil.copy(f, os.path.join("_test", f)) for f in restFiles]
testFiles = [os.path.join(d[0], f) for d in os.walk("_test")
             for f in d[2] if f.endswith(".rst")]

class Commands:
    """
    Each static method can be called from the command line. Add a new static
    method here to add a new command to the program.
    """

    @staticmethod
    def display(language):
        """
        Print all the code listings in the .rst files.
        """
        for f in restFiles:
            listings = language.listings.findall(open(f).read())
            if not listings: continue
            print('=' * 60 + "\n" + f + "\n" + '=' * 60)
            for n, l in enumerate(listings):
                print("\n".join(shift(l)))
                if n < len(listings) - 1:
                    print('-' * 60)

    @staticmethod
    def extract(language):
        """
        Pull the code listings from the .rst files and write each listing into
        its own file. Will not overwrite if code files and .rst files disagree
        unless you say "extract -force".
        """
        force = len(sys.argv) == 3 and sys.argv[2] == '-force'
        paths = set()
        for listing in [shift(listing) for f in restFiles
                    for listing in language.listings.findall(open(f).read())]:
            path = listing[0][len(language.commentTag):].strip()
            if path in paths:
                print("ERROR: Duplicate file name: %s" % path)
                sys.exit(1)
            else:
                paths.add(path)
            path = os.path.join("..", "code", path)
            dirname = os.path.dirname(path)
            if dirname and not os.path.exists(dirname):
                os.makedirs(dirname)
            if os.path.exists(path) and not force:
                for i in difflib.ndiff(open(path).read().splitlines(), listing):
                    if i.startswith("+ ") or i.startswith("- "):
                        print("ERROR: Existing file different from .rst")
                        print("Use 'extract -force' to force overwrite")
                        Commands.check(language)
                        return
            file(path, 'w').write("\n".join(listing))

    @staticmethod
    def check(language):
        """
        Ensure that external code files exist and check which external files
        have changed from what's in the .rst files. Generate files in the
        _deltas subdirectory showing what has changed.
        """
        class Result: # Messenger
            def __init__(self, **kwargs):
                self.__dict__ = kwargs
        result = Result(missing = [], deltas = [])
        listings = [Result(code = shift(code), file = f)
                    for f in restFiles for code in
                    language.listings.findall(open(f).read())]
        paths = [os.path.normpath(os.path.join("..", "code", path)) for path in
                    [listing.code[0].strip()[len(language.commentTag):].strip()
                     for listing in listings]]
        if os.path.exists("_deltas"):
            shutil.rmtree("_deltas")
        for path, listing in zip(paths, listings):
            if not os.path.exists(path):
                result.missing.append(path)
            else:
                code = open(path).read().splitlines()
                for i in difflib.ndiff(listing.code, code):
                    if i.startswith("+ ") or i.startswith("- "):
                        d = difflib.HtmlDiff()
                        if not os.path.exists("_deltas"):
                            os.makedirs("_deltas")
                        html = os.path.join("_deltas",
                            os.path.basename(path).split('.')[0] + ".html")
                        open(html, 'w').write(
                            "<html><h1>Left: %s<br>Right: %s</h1>" %
                            (listing.file, path) +
                            d.make_file(listing.code, code))
                        result.deltas.append(Result(file = listing.file,
                            path = path, html = html, code = code))
                        break
        if result.missing:
            print("Missing %s files:\n%s" %
                  (language.__name__, "\n".join(result.missing)))
        for delta in result.deltas:
            print("%s changed in %s; see %s" %
                  (delta.file, delta.path, delta.html))
        return result

    @staticmethod
    def update(language): # Test until it is trustworthy
        """
        Refresh external code files into .rst files.
        """
        check_result = Commands.check(language)
        if check_result.missing:
            print(language.__name__, "update aborted")
            return
        changed = False
        def _update(matchobj):
            listing = shift(matchobj.group(1))
            path = listing[0].strip()[len(language.commentTag):].strip()
            filename = os.path.basename(path).split('.')[0]
            path = os.path.join("..", "code", path)
            code = open(path).read().splitlines()
            return language.codeMarker + \
                "\n".join([("    " + line).rstrip() for line in listing])
        for f in testFiles:
            updated = language.listings.sub(_update, open(f).read())
            open(f, 'w').write(updated)

if __name__ == "__main__":
    commands = dict(inspect.getmembers(Commands, inspect.isfunction))
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Command line options:\n")
        for name in commands:
            print(name + ": " + commands[name].__doc__)
    else:
        for language in inspect.getmembers(Languages, inspect.isclass):
            commands[sys.argv[1]](language[1])