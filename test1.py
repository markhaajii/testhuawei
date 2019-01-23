#!/usr/bin/env python

import logging
from lxml import etree
from ncclient import manager
from ncclient.xml_ import *
import sys


HOST = '10.22.1.1'
# use the NETCONF port for your CSR1000V device
PORT = 830
# use the user credentials for your CSR1000V device
USER = 'netconf'
PASS = '123qweASD.,'

		
def main():
    """
    Simple main method calling our function.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'huawei'},
                         allow_agent=False, look_for_keys=False) as m:

        interface_filter = """
                        <filter>
                            <interfaces xmlns="urn:huawei:yang:huawei-ietf-interfaces-deviations-ATN-980B">
                                <interface></interface>
                            </interfaces>
                        </filter>
                        """

        interfaces = m.get_config('running', interface_filter)
        # print YANG module
        print('***Here is the YANG Module***')
        #data = m.get_schema('ietf-interfaces')
        print(interfaces.xml)

if __name__ == '__main__':
    sys.exit(main())
