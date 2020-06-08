"""
python -m doctest -v .\cli_python\store_data.py
Implement Local Storage

>>> import sys
>>> sys.version > "3.5"
True
"""
def local(infile, outfile):
    """
    copy data from one file to another. test omitted
    """
    outfile.write(infile.read())
    outfile.close()
    infile.close()
