# net_code_example
Flask api to call RIPEstat Data API

To start the server run python net_code_api/net_code_api.py

`i.e. /usr/local/bin/anaconda_3/bin/python net_code_api/net_code_api.py `

The server binds to loopback address on port 9000

To test the api send GET request to http://127.0.0.1:9000/

**START SERVER**
/usr/local/bin/anaconda_3/bin/python netCodeProject.py --ll debug

**API GET request Example:**
http://127.0.0.1:9000/search?action=geoloc&data=173.194.213.113

RIPEstat information can be found here: https://stat.ripe.net/docs/data_api#Overview

**TEST**
To run test:  Start server as mentioned above. 

Then run test either through IDE or command line:

Navigate to netCodeProject directory then

i.e. python -m unittest discover -s tests -p 'netCodeUnit.py' -v

/usr/local/bin/anaconda_3/bin/python -m unittest discover -s tests -p netCodeUnit.py -v

_Test Output_

test_Net_Code_Json (netCodeUnit.netCodeUnitTest) ... ok

test_Net_Code_Xml (netCodeUnit.netCodeUnitTest) ... ok

test_Net_Code_Yaml (netCodeUnit.netCodeUnitTest) ... ok

test_Xml_To_Json (netCodeUnit.netCodeUnitTest) ... ok

test_Yaml_To_Json (netCodeUnit.netCodeUnitTest) ... ok

----------------------------------------------------------------------

Ran 5 tests in 0.001s

OK

**INSTALL**
sudo /usr/local/bin/anaconda_3/bin/python setup.py install

To point to a specif python distro:
sudo /usr/local/bin/anaconda_3/bin/python setup.py install --prefix=/path/to/python/distro

_Install Output:_

running install

running bdist_egg

running egg_info

writing netCodeProject.egg-info/PKG-INFO

writing dependency_links to netCodeProject.egg-info/dependency_links.txt

writing top-level names to netCodeProject.egg-info/top_level.txt

reading manifest file 'netCodeProject.egg-info/SOURCES.txt'

reading manifest template 'MANIFEST.in'

warning: no files found matching '*.py' under directory '*.txt'

writing manifest file 'netCodeProject.egg-info/SOURCES.txt'

installing library code to build/bdist.macosx-10.7-x86_64/egg

running install_lib

running build_py

creating build/bdist.macosx-10.7-x86_64/egg

creating build/bdist.macosx-10.7-x86_64/egg/netCodePackage

copying build/lib/netCodePackage/__init__.py -> build/bdist.macosx-10.7-x86_64/egg/netCodePackage

creating build/bdist.macosx-10.7-x86_64/egg/tests

copying build/lib/tests/__init__.py -> build/bdist.macosx-10.7-x86_64/egg/tests

copying build/lib/tests/netCodeUnit.py -> build/bdist.macosx-10.7-x86_64/egg/tests

byte-compiling build/bdist.macosx-10.7-x86_64/egg/netCodePackage/__init__.py to __init__.cpython-36.pyc

**IMPORTING PACKAGE**

/usr/local/bin/anaconda_3/bin/python

 => /usr/local/bin/anaconda_3/bin/python
 
Python 3.6.0 |Anaconda 4.3.1 (x86_64)| (default, Dec 23 2016, 13:19:00)

[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin

Type "help", "copyright", "credits" or "license" for more information.

>>> import netCodePackage

>>> from netCodePackage import netCodeApi

>>> from netCodePackage import netCodeDataTypes

>>>



