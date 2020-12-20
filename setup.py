"""
The setup script for tarski.py. Can be used to install the module in the usual way.
"""
from codecs import open
from distutils.core import setup

import dicealyzer

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(name='dicealyzer.py',
      # Meta data
      version=dicealyzer.__VERSION__,
      description="Tools for rolling dice and analyzing them.",
      long_description=long_description,
      keywords='logic',
      license='MIT',

      # Author information
      author='René Mellema',
      author_email='rene.mellema@gmail.com',
      packages=['dicealyzer'],

      # Requirements
      install_requires=['lark-parser'],
      extras_require={
          'dev': ['pylint>=1.7',
                  'spinx>=4.0.0'],
          },
      python_requires='~=3.4',

      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities',
          ],

      # Entry points
      entry_points={
      },
     )
