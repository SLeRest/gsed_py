#!/usr/bin/python

import sys
import os
import unittest
from optparse import OptionParser
from os import listdir

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
                    error_handler("Path doesn't exist: " + arg)
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
        if len(self.dirs) == 0:
            return
        dirs_tmp = []
        for dirs in self.dirs:
            parse_dir = [d for d in listdir(dirs)]
            for file in parse_dir:
                if os.path.isfile(file):
                    self.files.append(file)
                elif os.path.isdir(file):
                    if (self.options.flag_recursive == True and
                            (file[0] != '.' or self.options.flag_all == True)
                            and file != "." and file != ".."):
                        dirs_tmp.append(file)
        self.dirs = dirs_tmp
        for file in self.files:
            self.search_replace_files()
        if self.options.flag_recursive == True:
            self.search_replace_dirs()


    def search_replace_files(self):
        for files in self.files:
            with open(files, "r+") as f:
                content = f.read()
                content = content.replace(self.search, self.replace)
                f.seek(0)
                f.write(content)
                f.truncate()
                f.close()

    def search_replace(self):
        #        self.search_replace_files()
        self.search_replace_dirs()
        #self.process_dirs() TODO

def main():
    parser = OptionParser(usage="usage: %prog [options] search replace",
                          version="%prog 1.0")
    parser.add_option("-a", "--all",
                      action="store_true",
                      dest="flag_all",
                      default=False,
                      help="do not ignore entries starting with .")
    parser.add_option("-R", "--recursive",
                      action="store_true",
                      dest="flag_recursive",
                      default=False,
                      help="search and replace in files subdirectories recursively")
    # deal with infinite recursion TODO
    parser.add_option("-l", "--link",
                      action="store_true",
                      dest="flag_link",
                      default=False,
                      help="follow links")

    (options, args) = parser.parse_args()

    if len(args) < 2:
        parser.error("wrong number of arguments")
        sys.exit(1)

    gsed = Gsed(args, options)
    gsed.search_replace()
    sys.exit(0)
    #gsed.print()
    #gsed.process()


if __name__ == '__main__':
    main()
