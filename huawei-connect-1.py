# -*- coding: utf-8 -*- 
import sys 
from ncclient import manager 
from ncclient import operations 
 
def huawei_connect(host, port, user, password): 
    return manager.connect(host=host, 
                           port=port, 
                           username=user, 
                           password=password, 
                           hostkey_verify = False, 
                           device_params={'name': "huawei"}, 
                           allow_agent = False, 
                           look_for_keys = False) 
 
def test_connect(host, port, user, password): 
    with huawei_connect(host, port=port, user=user, password=password) as m: 
 
        n = m._session.id         
        print("The session id is %s." % (n)) 
 
