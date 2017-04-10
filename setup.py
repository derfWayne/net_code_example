import sys
sys.path.insert(0, '/project/netCodeProject/netCodePackage')

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

import netCodePackage

setup(name='netCodeProject',
      version=netCodePackage.__version__,
      description=netCodePackage.__doc__,
      author=netCodePackage.__author__,
      author_email='iderf.thus@gmail.com',
      url='https://github.com/derfWayne/net_code_example.git',
      license=netCodePackage.__license__,
      platforms=['all'],
      packages={'netCodePackage': ['netCodeApi']},
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: Jython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Text Processing :: Markup :: XML',
      ],
      tests_require=['unittest>=1.0', 'flask'],
      )
