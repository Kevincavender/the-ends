#!/usr/bin/python

# setup.py info things

from distutils.core import setup

setup(
    name="the-ends",
    packages = ['the-ends'],
    version="0.1",
    author="Kevin Cavender",
    author_email='kac1200@gmail.com',
    url="https://github.com/Kevincavender/the-ends",
    download_url='',
    keywords = ['equation', 'engineer', 'math', 'calculator'],
    classifiers=[]
  )

'''
# cx_setup.py info things
import sys, os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\Kevin\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Kevin\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

build_exe_options = {"packages": ["Eqn_solver", "TkinterGUI", "os", "tkinter", "time"],
                     'path': sys.path + ['modules'],
                     "include_files": [r"C:\Users\Kevin\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                                       r"C:\Users\Kevin\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll"],
                     }

exe = [Executable(script="run.py", base="Win32GUI")]

setup(
  name="the-ends",
  version="0.1",
  options={"build_exe": build_exe_options},
  author="Kevin Cavender",
  executables=exe
  )
'''