import os
import sys

ROOT_DIR = os.path.realpath(
  os.path.join(
    os.path.dirname(__file__),
    '.'
  )
)

VENV_DIR = '%s/env' % ROOT_DIR

activate_this_file = "%s/bin/activate_this.py" % VENV_DIR

execfile(
    activate_this_file,
    dict(__file__=activate_this_file)
)

if __name__ == '__main__':
    print sys.path
