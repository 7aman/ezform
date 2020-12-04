#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

__version__ = '0.1.0'
__author__ = 'Zaman'
__contact__ = '7amaaan@gmail.com'
__url__ = 'https://github.com/7aman/ezform'
__license__ = 'MIT'


with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ezform',
    version=__version__,
    description='Format Ugly C Codes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=__url__,
    author=__author__,
    author_email=__contact__,
    license=__license__,
    packages=['ezform'],
    entry_points={
        'console_scripts': ['ezform = ezform.cli:main'],
    },
    install_requires=[
    ],
    python_requires='>=3.7',
    zip_safe=False,
    keywords='Code Formatter',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Utilities'
    ],
    project_urls={
        'source': __url__
    }
)
