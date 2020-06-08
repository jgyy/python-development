# python-development

Read, write, and understand Python code. Have a basic understanding of Object-Oriented Programming (OOP). Utilize Python as a primary language for tooling. Develop Python projects from start to finish.

Aside from learning python, there is also a project which will be stated below.

## Running python in windows

There are 2 commands below for running python scripts with test cases and debugging.

```console
$ python -m doctest -v .\folder\file.py
<output>
$ python -m pdb .\folder\file.py
<output>
```

## pgbackup

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

## Usage

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

```console
$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
<output>
```

Local Example w/ local path:

```console
$ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups
<output>
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```console
$ pip install --user -e .
<output>
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:example/pgbackup`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`
