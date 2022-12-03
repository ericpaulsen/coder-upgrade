# retrieve current sha & upgrade to latest release of coder/coder
import requests
import json
import os

def getSha():
    # make API call
    res = requests.get("https://api.github.com/repos/coder/coder/tags")
    # convert JSON response to bytes
    c = res.content
    # deserialize JSON bytes to Python object
    tags = json.loads(c)
    # pull latest version sha
    latest_sha = tags[1]['commit']['sha']
    return latest_sha

# read file for previous sha
with open('sha.txt', 'r') as file:
  current_sha = file.read().rstrip()

# compare previous sha to current sha
if current_sha != getSha():
  # install coder
  install = 'curl -L https://coder.com/install.sh | sh'
  os.system(install)
  # reload coder service
  reload = 'sudo systemctl daemon-reload && systemctl restart coder.service'
  os.system(reload)
    # write new sha to existing file
  with open('sha.txt', 'w') as f:
    print(getSha(), file=f)
else:
  pass # do nothing