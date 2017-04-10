import sys
import os

#sys.path.insert(0, '/projects/netCodeProject/netCodePackage/netCodeDataTypes')

import unittest
from netCodePackage import netCodeDataTypes
import urllib.request
import json
from configparser import ConfigParser

data_files = []

config = ConfigParser()
configFilePath = os.getcwd() + r'/conf.ini'
config.read(configFilePath)


def walker(arg, dirname, fnames, file_type):
    d = os.getcwd()
    os.chdir(dirname)
    try:
        fnames.remove('Thumbs')
    except ValueError:
        pass
    for f in fnames:
        print(f)
        if not os.path.isfile(f) or f.endswith(file_type):
            continue
        data_files.append(os.path.join(dirname, f))
    os.chdir(d)


class netCodeUnitTest(unittest.TestCase):
    """

    """
    net_api = 'http:/127.0.0.1:9000/search?&'

    def test_Net_Code_Json(self):
        """
        Testing json response and return data type
        :return:
        """
        try:
            cur_dir = os.getcwd()
            os.walk(cur_dir, walker, data_files, '.json')
            for f in data_files[1:]:
                with open(f, 'r') as action_file:
                    file_data = json.load(action_file.read())
                    self.net_api += 'action=%s' % file_data['action']
                    self.net_api += '&data=%s' % file_data['data']
                    response = urllib.request.Request(self.net_api)
                    self.failUnlessEqual(response.code, 200)
                    self.failUnlessEqual(response.json, dict(success=True))
                    self.assertEqual(response.code, 200)
                    self.assertEquals(response.json, dict(success=True))
        except (OSError, FileNotFoundError) as e:
            print('Exception occurred %s' % e)

    def test_Net_Code_Yaml(self):
        """
        Testing yaml data response and return data type
        :return:
        """

        try:
            cur_dir = os.getcwd()
            os.walk(cur_dir, walker, data_files, '.yaml')
            for f in data_files[1:]:
                with open(f, 'r') as action_file:
                    file_data = json.load(action_file.read())
                    self.net_api += 'action=%s' % file_data['action']
                    self.net_api += '&data=%s' % file_data['data']
                    response = urllib.request.Request(self.net_api)
                    self.failUnlessEqual(response.code, 200)
                    self.failUnlessEqual(response.json, dict(success=True))
                    self.assertEqual(response.code, 200)
                    self.assertEquals(response.json, dict(success=True))
        except (OSError, FileNotFoundError) as e:
            print('Exception occurred %s' % e)

    def test_Net_Code_Xml(self):
        """
        Testing XML data response and return data type
        :return:
        """

        try:
            cur_dir = os.getcwd()
            os.walk(cur_dir, walker, data_files, '.xml')
            for f in data_files[1:]:
                with open(f, 'r') as action_file:
                    file_data = json.load(action_file.read())
                    self.net_api += 'action=%s' % file_data['action']
                    self.net_api += '&data=%s' % file_data['data']
                    response = urllib.request.Request(self.net_api)
                    print(response.code)
                    print(response.json)
                    self.failUnlessEqual(response.code, 200)
                    self.failUnlessEqual(response.json, dict(success=True))
                    self.assertEqual(response.code, 200)
                    self.assertEquals(response.json, dict(success=True))
        except (OSError, FileNotFoundError) as e:
            print('Exception occurred %s' % e)

    def test_Xml_To_Json(self):
        """
        Testing data conversion library from xml to json
        :return:
        """

        try:
            cur_dir = None
            if 'netCodeDataTypes' in os.getcwd():
                pass
            else:
                cur_dir = os.getcwd()
                os.chdir(cur_dir + '/netCodePackage/netCodeDataTypes')

            os.walk(cur_dir, walker, data_files, '.xml')
            for f in data_files[1:]:
                with open(f, 'r') as action_file:
                    file_data = json.load(action_file.read())
                    xml_convert_json = netCodeDataTypes.convert_xml_json(file_data)
                    self.failUnlessEqual(xml_convert_json, dict(success=True))
                    self.assertEquals(xml_convert_json, dict(success=True))
        except (OSError, FileNotFoundError, ValueError) as e:
            print('Exception occurred %s' % e)

    def test_Yaml_To_Json(self):
        """
        Testing data conversion library from yaml to json
        :return:
        """

        try:
            cur_dir = None
            if 'netCodeDataTypes' in os.getcwd():
                pass
            else:
                cur_dir = os.getcwd()
                os.chdir(cur_dir + '/netCodePackage/netCodeDataTypes')
            os.walk(cur_dir, walker, data_files, '.yaml')
            for f in data_files[1:]:
                with open(f, 'r') as action_file:
                    file_data = json.load(action_file.read())
                    yaml_convert_json = netCodeDataTypes.convert_yaml_json(file_data)
                    print(yaml_convert_json)
                    print(yaml_convert_json)
                    self.failUnlessEqual(yaml_convert_json, dict(success=True))
                    self.assertEquals(yaml_convert_json, dict(success=True))
        except (OSError, FileNotFoundError, ValueError) as e:
            print('Exception occurred %s' % e)


if __name__ == '__main__':

    unittest.main()
