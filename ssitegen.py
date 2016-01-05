#!/usr/bin/env python
import os
import argparse
import sys
import shutil

EXEC_ROOT = os.path.dirname(__file__)
DIR_TEMPLATE_PATH = "data/source_dir"
OUTPUT_DIRNAME = "output"

parser = argparse.ArgumentParser(add_help=True, description="A simple static site generator")

parser.add_argument("-i", "--initialize", action="store", default=None, dest="dirname",
                    help="Initialize the directory structure inside DIRNAME")


def ensure_dir_exists(dirname, mode=0o755):
    """Creates a directory with the given name if doesn't already exist"""

    if not os.path.exists(dirname):
        os.mkdir(dirname, mode)

        
if __name__ == "__main__":
    args = parser.parse_args()
    if args.dirname:
        working_dir = args.dirname
        if os.path.exists(working_dir):
            # already exists, print error and exit
            err_msg = "Directory '{0}' already exists\n".format(working_dir)
            sys.stderr.write(err_msg)
            sys.exit(1)
        
        dir_template_loc = os.path.join(EXEC_ROOT, DIR_TEMPLATE_PATH)
        shutil.copytree(dir_template_loc, working_dir)
    else:
        # generate output directory
        ensure_dir_exists(OUTPUT_DIRNAME)

        # copy over static assets
        shutil.copytree('static', OUTPUT_DIRNAME + "/static")
        
