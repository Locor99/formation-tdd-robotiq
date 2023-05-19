#! /usr/bin/env python3

import sys
import os
import json

def list_files(directory):
    tree={}

    for filename in os.listdir(directory):
        size = os.path.getsize(directory + "/" + filename)
        tree[filename] = size

    print(json.dumps(tree))

def usage():
    print("Invalid usage!")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        list_files(sys.argv[1])
        sys.exit(0)
    else:
        usage()
        sys.exit(1)
