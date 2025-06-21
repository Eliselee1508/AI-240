#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
# below code are according to the solution/copyspecial.py


def get_special_paths(dirname):
  result = []
  paths = os.listdir(dirname)  # list of paths in that dir
  for fname in paths:
    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result

# copy_to(paths, dir) given a list of paths, copies those files into the given directory
def copy_to(paths, to_dir):
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, fname))
  
# zip_to(paths, zipfile) given a list of paths, zips those files into the given zipfile
def zip_to(paths, zipfile):
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print("Command I'm going to do:" + cmd)
  (status, output) = subprocess.getstatusoutput(cmd)
  # If subprocess had a problem (status is non-zero),
  # print its output to stderr and exit.
  if status:
    sys.stderr.write(output)
    sys.exit(1)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  # Gather a list of the absolute paths of the special files in all the directories
  special_paths = []
  for dirname in args:
    special_paths.extend(get_special_paths(dirname))


  # If the "--todir dir" option is present at the start of the command line, do not print anything and instead copy the files to the given directory, creating it if necessary. Use the python module "shutil" for file copying.
  if todir:
    copy_to(special_paths, todir)
  elif tozip:
    zip_to(special_paths, tozip)
  else:
    for path in special_paths:
      print(path)

if __name__ == '__main__':
  main()
