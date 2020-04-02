import os

# Find all files beneath 'path' with file name 'suffix'.
# There are no limit to the depth of the subdirectories can be.

# Args:
  # suffix(str): suffix if the file name to be found
  # path(str): path of the file system
def find_files(suffix, path):

  if not bool(path):
    return []

  output = []
  # os.listdir: returns a list containing the names of the entries in the directory given by 'path' 
  for entry in os.listdir(path):
    entry_path = os.path.join(path, entry) # concatenation of path components

    if os.path.isdir(entry_path):
      output += find_files(suffix, entry_path)

    elif os.path.isfile(entry_path) and entry.endswith(suffix):
      output.append(entry_path)
    
  return output


def test(suffix, path):
  files = find_files(suffix, path)
  if len(files) == 0:
    print('No files found.')
    return

  for path in files:
    print(path)

test('.c', './testdir')
