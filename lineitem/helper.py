###########################################################################
#
#  Copyright 2017 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################


import argparse

from util.project import project
from util.dbm import lineitem_read, lineitem_write


if __name__ == "__main__":

  # get parameters
  parser = argparse.ArgumentParser()
  parser.add_argument('lineitem', help='lineitem ID to pull schema, or "list" to get index')

  # initialize project
  project.load(parser=parser)
  auth = 'service' if project.args.service else 'user'

  for row in lineitem_read(auth, lineitems=[project.args.lineitem]):
    print row

'''
Example:
python lineitem/helper.py 9915840 -u /Users/kenjora/.credentials/kenjora_user.json
'''
