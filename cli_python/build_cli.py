# python -m doctest -v .\cli_python\build_cli.py
"""
The argparse Package

>>> import sys
>>> sys.version > "3.5"
True
"""
from argparse import Action, ArgumentParser

class DriverAction(Action):
    """
    DriverAction only provides the __call__ function based on Action

    >>> type(DriverAction)
    <class 'type'>
    """
    def __call__(self, parser, namespace, values, option_string=None):
        """
        provides driver and destination

        >>> parser = create_parser()
        >>> args = parser.parse_args(['https://some_urls', '--driver', 's3', 'bucket_name'])
        >>> (args.url, args.driver, args.destination)
        ('https://some_urls', 's3', 'bucket_name')
        """
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    """
    creates parser based on ArgumentParser

    >>> parser = create_parser()
    >>> args = parser.parse_args(['https://some_url', '--driver', 's3', 's3_bucket_name'])
    >>> (args.url, args.driver, args.destination)
    ('https://some_url', 's3', 's3_bucket_name')
    """

    parser = ArgumentParser(description="""
    Back up PostgreSQL databases locally or to AWS S3.
    """)
    parser.add_argument("url", help="URL of database to backup")
    parser.add_argument("--driver", "-d",
            help="how & where to store backup",
            nargs=2,
            metavar=("DRIVER", "DESTINATION"),
            action=DriverAction,
            required=True)
    return parser

def main():
    """
    generate a timestamp with time.strftime, generate a database file name,
    and print what we're doing as we upload/write files. 

    broken since pgdump cant be done in windows.
    """
    import time
    import boto3
    from cli_python import psql_dump, store_data

    args = create_parser().parse_args(
        ['https://some_url', '--driver', 's3', 'bucket_name'])
    print(args.url)
    dump = psql_dump.dump(args.url)

    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = psql_dump.dump_file_name(args.url, timestamp)
        print(f"Backing database up to {args.destination} in S3 as {file_name}")
        store_data.s3(client,
                dump.stdout,
                args.destination,
                file_name)
    else:
        outfile = open(args.destination, 'wb')
        print(f"Backing database up locally to {outfile.name}")
        store_data.local(dump.stdout, outfile)

parser = create_parser()
args = parser.parse_args(['https://some_url', '--driver', 's3', 'bucket_name'])
print(args.url)
print(args.driver)
print(args.destination)
main()
