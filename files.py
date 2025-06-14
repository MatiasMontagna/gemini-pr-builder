import os
import tempfile

def read_file(path):
  if os.path.exists(path):
    with open(path, "r") as f:
      return f.read()
  return None 

def write_to_tempfile(content):
  with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
    tmp.write(content)
    return tmp.name

def cleanup_tempfile(tmp_path):
  os.remove(tmp_path)

def read_template():
  return read_file(".github/pull_request_template.md")
