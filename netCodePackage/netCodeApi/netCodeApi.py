import sys

#sys.path.insert(0, '/netCodeExample/netCodeDataTypes')

from flask import Flask, request
import urllib.request
import os
import json
import re
import socket
from netCodeDataTypes import netCodeDataTypes
from configparser import ConfigParser
import jsonschema
from jsonschema import Draft3Validator
from optparse import OptionParser
import logging

app = Flask(__name__)

net_api_queries = []

config = ConfigParser()
configFilePath = os.getcwd() + r'conf.ini'
config.read(configFilePath)

netApiLogger = logging.getLogger('netCodeAPiLogger')
logFile = "netCodeApi.log"

@app.route('/search', methods=['GET'])
def get():
    """
     Entry point for api
     Method to query backend api
     :return:
     """
    net_code_uri = 'https://stat.ripe.net/data/%s/data.json?'
    query_params = request.args.to_dict()

    is_valid = validateParams(query_params)
    json_data = validateConvertData(query_params)

    if not is_valid:
        return "Invalid action or parameters for action"

    req = None
    if not str(query_params['data']):
        for params in query_params["data"]:
            for parameter in params:
                net_code_uri += ("resource=%s" % str(parameter))
        req = urllib.request.Request(net_code_uri % query_params["action"])
        print(net_code_uri)
    else:
        net_code_uri = net_code_uri % query_params["action"]
        net_code_uri += 'resource=%s' % query_params['data']
        print('URI with un param: %s' % net_code_uri)
        req = urllib.request.Request(net_code_uri)

    req.add_header("Content-type", "application/json")

    resp = urllib.request.urlopen(req)
    p_dict_array = json.load(resp)

    print(p_dict_array)

    return json.dumps(p_dict_array)


def validateParams(query_params):
    """
     Validating parameters sent to api
     :param query_params:
     :return:
     """

    # if action is network-info validate ip address
    # if action is as-overview vaidate only alphanumberic
    # if action is geoloc validate IP address, validate hostname is string, validate

    valid_action = re.match('^[\w-]+$', query_params["action"]) is not None

    if not valid_action or query_params["action"] not in ["geoloc", "as-overview", "network-info"]:
        return "Invalid action parameter string"

    if query_params["action"] is not "geoloc":
        if 'as-overview' in query_params["action"]:
            valid_param = re.match('^[\w-]+$', query_params["data"]) is not None
            if not valid_param:
                print('Invalid parameters')
                return False  # "Invalid AS-Overview parameter"
        else:
            try:
                # validate if IP address
                """
                    socket.inet_aton(query_params["data"])
                    """
                a = str(query_params['data']).split('.')
                i = int()
                if len(a) != 4:
                    return False
                for x in a:
                    if not x.isdigit():
                        i = int(x)
                        return False
                    if i < 0 or i > 255:
                        return False
            except socket.error as e:
                # Not legal
                return False
    else:
        # Validate if geoloc is net plus mask request
        for params in query_params["data"]:
            print(params)
            for parameter in params:
                if "/" in parameter:
                    if str(parameter).split('/')[0] <= 3 and str(parameter).split('/')[1] <= 2:
                        for asn in str(parameter).split('/'):
                            valid_param = re.match('^[\w-]+$', asn) is not None
                            if not valid_param:
                                return "Invalid Geoloc parameters"
                # Validate if geoloc is IP Address
                elif len(str(parameter.split('.'))) == 4 or not re.match('^[\w-]+$', parameter):
                    try:
                        # validate if IP address
                        socket.inet_aton(parameter)
                    except socket.error:
                        # Not legal
                        return "Invalid IP Address for Geoloc"
                # Validate if Geoloc is hostname
                else:
                    valid_param = re.match('^[\w-]+$', parameter) is not None
                    if not valid_param:
                        return "Invalid IP Address for Geoloc"
    return True


def validateConvertData(data):
    """
    validate and convert parameters sent to api
    :param data:
    :return:
    """
    json_data = {}
    try:
        Draft3Validator(data)
        # json_data = json.loads(data)
    except (TypeError, OverflowError, jsonschema.ValidationError) as e:
        if type(data) == "yaml":
            json_data = netCodeDataTypes.convert_yaml_json(data)
            return json_data
        elif type(data) == "xml":
            json_data = netCodeDataTypes.convert_xml_json(data)
            return json_data
        else:
            print('Failure converting valid document! :( %s' % str(e))
    else:
        return json_data


def main():
    """
    Parsing command line parameters and setting defaults if none
    :return:
    """

    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)

    # Command line options
    parser.add_option("--c", "--conf_file", action="store", type="string", dest="conf")
    parser.add_option("--h", "--host", action="store", type="string", dest='host', help="Host is bind ip address")
    parser.add_option("--p", "--port", action="store", type="int", dest='port',
                      help="Port number must be a valid integer")
    parser.add_option("--d", "--debug", action="store", type="string", dest='debug', help="Must be True or False")
    parser.add_option("--ll", "--log_level", action="store", type="string", dest='logLevel', default='info')

    (options, args) = parser.parse_args()

    return options


if __name__ == "__main__":

    options = main()
    loggerFile = open(os.getcwd() + logFile, 'wb+')

    if options.logLevel == "info":
        netApiLogger.level = logging.INFO
    elif options.logLevel == "verbose":
        netApiLogger.level = logging.__all__
    elif options.logLevel == "debug":
        netApiLogger.level = logging.DEBUG

    # Creating a file handler for logging
    logHandler = logging.FileHandler(loggerFile.name)

    # Log file formatting
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logHandler.setFormatter(formatter)
    netApiLogger.addHandler(logHandler)

    # server settings
    CONF_HOST = str()
    CONF_PORT = int()
    CONF_DEBUG_MODE = bool()

    if options.host is not None:
        CONF_HOST = str(options.host)
    elif options.port is not None:
        CONF_PORT = int(options.port)
    elif options.conf is not None:
        configFilePath = options.conf
    else:
        # server settings
        CONF_HOST = str(config.get('api', 'HOST'))
        CONF_PORT = int(os.environ.get('PORT', int(config.get('api', 'PORT'))))
        CONF_DEBUG_MODE = bool(config.get('api', 'DEBUG_MODE'))

    app.run(debug=CONF_DEBUG_MODE, host=CONF_HOST, port=CONF_PORT)
    # app.run()
