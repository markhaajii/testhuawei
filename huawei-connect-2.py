# -*- coding: utf-8 -*- 
import sys 
from ncclient import manager 
from ncclient import operations 
 
def huawei_connect(): 
    return manager.connect(host="10.22.1.1", 
                           port=830, 
                           username="netconf", 
                           password="123qweASD.,", 
                           hostkey_verify = False, 
                           device_params={'name': "huawei"}, 
                           allow_agent = False, 
                           look_for_keys = False)
def test_connect(): 
    with huawei_connect() as m: 
 
        n = m._session.id         
        print("The session id is %s." % (n)) 
 
if __name__ == '__main__':
	test_connect()