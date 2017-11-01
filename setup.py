#!/usr/bin/env python
# -*- coding: utf-8 -*-


description = """Reorganising NIfTI files from dcm2niix into the Brain Imaging Data Structure"""


#from distutils.core import setup
from setuptools import setup


DISTNAME = "dcm2bids"
DESCRIPTION = description
VERSION = "1.0.1"
AUTHOR = "Christophe Bedetti"
AUTHOR_EMAIL = "christophe.bedetti@umontreal.ca"
URL = 'https://github.com/cbedetti/Dcm2Bids'


if __name__ == "__main__":
    setup(
            name=DISTNAME,
            version=VERSION,
            description=description,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            url=URL,
            packages=['dcm2bids'],
            scripts=['scripts/dcm2bids', 'scripts/dcm2bids_helper'],
            install_requires=['future'],
            )
