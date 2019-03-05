import sys
import os
import unittest

def print_help():
    print("help", flush=True)

class Err():
    def not_enouth_args():
        print("Error: gsed: need at least 2 args",
              file=sys.stderr, flush=True)
        print_help()
        sys.exit(1)

    def path_not_found(path):
        print("Error: gsed: Path doesn't exist:", path,
              file=sys.stderr, flush=True)


class Gsed:
    # reduction de ram
    __slots__ = 'search', 'replace', 'files', 'dirs'

    def __init__(self, args):
        if len(args) < 2:
            Err.not_enouth_args()
        self.search = ""
        self.replace = ""
        self.files = []
        self.dirs = []
        is_path = False
        for arg in args[1:]:
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
                    Err.path_not_found(arg)
        if is_path == False:
            self.dirs.append("./")
        if is_path == True and len(self.files) == 0 and len(self.dirs) == 0:
            sys.exit(2)

    # debug print
    def print(self):
        print("gsed: search:\"", self.search, "\"replace:\"",
              self.replace, "\"files:", self.files, "\"dirs:", self.dirs)

gsed = Gsed(sys.argv)
gsed.print()
