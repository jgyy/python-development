# python .\cli_python\project_setup.py build
# python .\cli_python\project_setup.py install
# Unit test is not possible with "setup"
from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgpackup',
    version='0.1.0',
    author='jgyy',
    author_email='jeffrey.goh@sit.singaporetech.edu.sg',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jgyy/python-development',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ],
    }
)
