"""
python -m doctest -v .\cli_python\store_data.py
Implement Local Storage

>>> import sys
>>> sys.version > "3.5"
True
"""
def local(infile, outfile):
    """
    copy data from one file to another.

    >>> True
    True
    """
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s_3(client, infile, bucket, name):
    """
    upload file to aws s3

    >>> True
    True
    """
    client.upload_fileobj(infile, bucket, name)

# Manually Testing S3 Integration
import boto3
client = boto3.client('s3')
infile = open('.\cli_python\example.txt', 'rb')
s_3(client, infile, 'py0', infile.name)
