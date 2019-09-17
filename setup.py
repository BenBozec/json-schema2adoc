#!/usr/bin/env python

"""
Script used to generate Python package
"""

from setuptools import setup, find_packages

# Makes long_description == README.md content
with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='api_from_schema',
    version='0.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    url='https://github.com/AAFC-BICoE/json-schema2adoc',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(include=[
        'api_from_schema',
    ]),
    # Uncomment when non-python files are to be included in the package. In such cases '
    # a MANIFEST.in file must also be included at the setup.py level of the project.
    # include_package_data=True,

    # This creates an entry point which can be called directly: e.g. '$ generate_api_doc file.json output/directory/'
    entry_points={
        'console_scripts': [
            'generate_api_doc = api_from_schema.schemaAdocGeneratorV2:main',
        ],
    },
)
