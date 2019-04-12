#!/usr/bin/env python
import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages
import os

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, 'src', 'Base64Library', 'version.py'), encoding="utf-8") as f:
      VERSION = re.search("VERSION = '(.*)'", f.read()).group(1)

REQUIREMENTS = ""
DESCRIPTION = """
Robot Framework keyword library wrapper around Base64 encoding and decoding testing library for Robot Framework.
"""[1:-1]

setup(name         = 'robotframework-base64',
      version      = VERSION,
      description  = 'Base64 encoding and decoding testing library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'oumin',
      author_email = '<oumin@mail.ustc.edu.cn>',
      url          = '',
      license      = 'MIT',
      keywords     = 'robotframework testing testautomation robotframework-base64',
      platforms    = 'any',
      classifiers  = [
                        "Development Status :: 5 - Production/Stable",
                        "License :: OSI Approved :: Apache Software License",
                        "Operating System :: OS Independent",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Testing"
                        "Framework :: Robot Framework"
                     ],
      install_requires = REQUIREMENTS,
      package_dir  = {'' : 'src'},
      packages     = ['Base64Library'],
      )
