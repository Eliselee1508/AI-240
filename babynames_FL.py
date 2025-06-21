#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """

  #create a list to store the list [year, name_and_rank, name_and_rank, ...]
  file_name = []

  # Extract all the text from the file and print it
  with open(filename, 'r') as file:
    text = file.read()
    print(text)

  # This part are according to the solution for this exercise
  # Find and extract the year and print it
    year_search = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_search:
      # NOT find a year, exit with an error message.
      sys.stderr.write('Couldn\'t find the year!\n')
      sys.exit(1)
    year = year_search.group(1)
    file_name.append(year)
    print(year)
  # Extract the names and rank numbers and print them
  # Get the names data into a dict and print it
  # Build the [year, 'name rank', ... ] list and print it
  # Fix main() to use the ExtractNames list
    name_search = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    names_dict = {}
    for rank in name_search:
      rank_num = rank[0]
      name1 = rank[1]
      name2 = rank[2]
      names_dict[name1] = rank_num
      names_dict[name2] = rank_num
    # Print the names and ranks
    for name in sorted(names_dict):
      file_name.append(f"{name} {names_dict[name]}")
      print(f"{name} {names_dict[name]}")
  # Return the list of names
  return file_name


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
   extract_names(filename)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)
    if summary:
      with open(filename + '.summary', 'w') as summary_file:
        for name in names:
          summary_file.write(name + '\n')
    else:
      for name in names:
        print(name)

if __name__ == '__main__':
  main()
