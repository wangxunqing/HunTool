import os
from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name='hun_tool',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-restful',
        'flask-migrate',
        'flask-jwt-extended',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'python-dotenv',
        'passlib',
        'apispec[yaml]',
        'apispec-webframeworks',
    ],
    entry_points={
        'console_scripts': [
            'hun_tool = hun_tool.manage:cli'
        ]
    }
)
