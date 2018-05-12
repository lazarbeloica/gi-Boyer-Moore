#!/usr/bin/env python

from distutils.core import setup

setup(name='gi_boyermoore',
      version='1.0',
      description='A Boyer-Moore algorithm implementation',
      author=['Lazar Beloica', 'Milan Zafirovic'],
      author_email=['lazarbeloica@gmail.com', 'zafirovicmilan2@gmail.com'],
      url='https://github.com/lazarbeloica/gi-Boyer-Moore/',
      packages=['src/algorithm', 'src/heuristics', 'src/tests'],
     )