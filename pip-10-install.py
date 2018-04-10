"""
Upgrade to pip 10 before installing requirements, working
around error reported in tox-dev/tox#786
"""

import sys
import subprocess
import shlex


def main():
	subprocess.check_call(shlex.split(
		'python -m pip install git+https://github.com/pypa/pip@release/10.0.0'
	))
	subprocess.check_call(shlex.split(
		'python -m pip install') + sys.argv[1:])


__name__ == '__main__' and main()
