#!/usr/bin/python

# setup.py info things
from setuptools import setup, find_packages


# Distributing commands:
# python setup.py sdist (builds the project from this file)
# twine upload dist/* (uploads everything in that folder to pypi)
setup(
    name="the_ends",
    packages = ['the_ends'],
    author="Kevin Cavender",
    description='Implicit Equation Solver (will reorder equations for maths)',
    author_email='kac1200@gmail.com',
    url="https://github.com/Kevincavender/the_ends",
    download_url='https://github.com/Kevincavender/the_ends/archive/0.1.tar.gz',
    keywords = ['equation', 'engineer', 'math', 'calculator'],
    entry_points={
        'console_scripts':[
        ]
    }
  )
