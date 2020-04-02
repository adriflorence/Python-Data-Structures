import os

# Find all files beneath 'path' with file name 'suffix'.
# There are no limit to the depth of the subdirectories can be.

# Args:
  # suffix(str): suffix if the file name to be found
  # path(str): path of the file system
def find_files(suffix, path):

  if not bool(path):
    return []

  def find(path, files):
    # os.listdir: returns a list containing the names of the entries in the directory given by 'path' 
    for entry in os.listdir(path):
      full_path = os.path.join(path, entry)
      print(full_path)

      if os.path.isdir(full_path):
        files = find(full_path, files)

      elif os.path.isfile(full_path) and (suffix is None or entry.endswith(suffix)):
        files.append(full_path)
      
      return files

    # Returns a list of paths
    return find(path, [])


def test(suffix, path):
  files = find_files(suffix, path)

print(test('.c', 'testdir'))