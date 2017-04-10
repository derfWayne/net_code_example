import os
import json
import yaml
from optparse import OptionParser
import xmltodict
from configparser import ConfigParser


config = ConfigParser()
configFilePath = os.getcwd() + r'/conf.ini'
config.read(configFilePath)


class netCodeDataTypes():
    """
    
    """
    def __init__(self):
        pass

    def convert_yaml_json(self, yaml_data):
        """
        
        :param yaml_data: 
        :return: 
        """
        try:
            return json.dumps(yaml.load(yaml_data), sort_keys=True, indent=2) #json.dumps(data_map)

        except (yaml.YAMLError, yaml.MarkedYAMLError) as e:
            return print('Exception converting yaml data %s' % e)

    def convert_xml_json(self, xml_data, xml_attribs=True):
        """
        
        :param xml_data: 
        :param xml_attribs: 
        :return: 
        """

        try:

            data_map = xmltodict.parse(xml_data, xml_attribs=xml_attribs)
            return json.dumps(data_map, indent=4)

        except ValueError as e:
            return print('Exception converting xml to json %s' % e)


def main():
    """
    Parsing command line parameters and setting defaults if none
    :return:
    """

    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)

    # Command line options
    parser.add_option("--xml", "--convert_xml", action="store", type="string", dest="convertXml", help="Convert xml to json file")
    parser.add_option("--yaml", "--convert_yaml", action="store", type="string", dest='convertYaml', help="Convert yaml to json file")
    parser.add_option("--ll", "--log_level", action="store", type="string", dest='logLevel', default='info')

    (options, args) = parser.parse_args()

    return options

if __name__ == "__main__":

    options = main()

    dataTypes = netCodeDataTypes()

    if len(options.convertXml) > 0:
        if os.path.isfile(options.convertXml):
            with open(options.convertXml, 'r') as fp:
                xmlData = fp.read()
                convertedJson = dataTypes.convert_xml_json(xmlData)
                print('Converted Json %s' % convertedJson)
        else:
            print('Not a valid file path')

    if len(options.convertYaml) > 0:
        if os.path.isfile(options.convertYaml):
            with open(options.convertYaml) as fp:
                yamlData = fp.read()
                convertedJson = dataTypes.convert_yaml_json(yamlData)
                print('Converted Json %s' % convertedJson)
        else:
            print('Not a valid file path')




