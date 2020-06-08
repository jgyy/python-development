"""
python -m doctest -v .\cli_python\psql_dump.py
Interacting with Subprocesses

>>> import sys
>>> sys.version > "3.5"
True
"""
import sys
import subprocess

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

# Manual Testing
dump = dump('postgres://jgyy:jgyy@13.229.82.53:80/sample')
f = open('.\cli_python\dump.sql', 'w+b')
f.write(dump.stdout.read())
f.close()
