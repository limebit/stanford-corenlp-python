#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(name='corenlp',
version='3.4.1',
description='Python wrapper for Stanford CoreNLP tools v3.4.1',
long_description=README,
author='Dustin Smith',
author_email='dustin@media.mit.edu',
url='https://github.com/dasmith/stanford-corenlp-python',
py_modules=['client', 'corenlp', 'jsonrpc', 'progressbar'],
license='GPL v2+',
install_requires=['pexpect', 'unidecode'],
data_files=[
    ('.', ['default.properties']),
    ('stanford-corenlp-full-2014-08-27',
     ['stanford-corenlp-full-2014-08-27/stanford-corenlp-3.4.1.jar',
      'stanford-corenlp-full-2014-08-27/stanford-corenlp-3.4.1.jar',
      'stanford-corenlp-full-2014-08-27/stanford-corenlp-3.4.1-models.jar',
      'stanford-corenlp-full-2014-08-27/joda-time.jar',
      'stanford-corenlp-full-2014-08-27/xom.jar',
      'stanford-corenlp-full-2014-08-27/jollyday.jar'
     ])
],
)