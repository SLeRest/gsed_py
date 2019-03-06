#!/usr/bin/python

import sys
import os
import unittest
from optparse import OptionParser

def print_help():
    print("help", flush=True)

def error_handler(e):
    print("Error: gsed: ", e, file=sys.stderr, flush=True)

class Gsed:
    # reduction de ram
    __slots__ = 'search', 'replace', 'files', 'dirs', 'options'

    def __init__(self, args, options):
        self.search = ""
        self.replace = ""
        self.files = []
        self.dirs = []
        self.options = options
        is_path = False
        for arg in args:
            if len(self.search) == 0:
                self.search = arg
            elif len(self.replace) == 0:
                self.replace = arg
            else:
                is_path = True
                if os.path.isfile(arg):
                    self.files.append(arg)
                elif os.path.isdir(arg):
                    self.dirs.append(arg)
                else:
                    print("Error: gsed: Path doesn't exist:", path,
                          file=sys.stderr, flush=True)
        if is_path == False:
            self.dirs.append("./")
        if is_path == True and len(self.files) == 0 and len(self.dirs) == 0:
            sys.exit(2)

    # debug print
    def print(self):
        print("gsed: search:\"", self.search, "\"replace:\"",self.replace,"\"")
        print("files:\"", self.files, "\"dirs:", self.dirs)
        print("options:", self.options)


    def search_replace_dirs(self):
        for dirs in self.dirs:
            for root, dirs, files in os.walk(dirs, onerror=error_handler):
                print("root", root, "dirs", dirs, "files", files)

    def search_replace_file(self):
        for files in self.files:
            with open(files, "r+") as f:
                content = f.read()
                content = content.replace(self.search, self.replace)
                f.seek(0)
                f.write(content)
                f.truncate()
                f.close()

    def process(self):
        self.search_replace_files()
        self.search_replace_dirs()
        #self.process_dirs() TODO

def main():
    parser = OptionParser(usage="usage: %prog [options] search replace",
                          version="%prog 1.0")
    parser.add_option("-a", "--all",
                      action="store_true",
                      dest="all",
                      default=False,
                      help="do not ignore entries starting with .")
    parser.add_option("-R", "--recursive",
                      action="store_true",
                      dest="recursive",
                      default=False,
                      help="search and replace in files subdirectories recursively")
    # deal with infinite recursion TODO
    parser.add_option("-l", "--link",
                      action="store_true",
                      dest="link",
                      default=False,
                      help="follow links")

    (options, args) = parser.parse_args()

    if len(args) < 2:
        parser.error("wrong number of arguments")
    gsed = Gsed(args, options)
    gsed.process_dirs()
    #gsed.print()
    #gsed.process()


if __name__ == '__main__':
    main()
