# test_edit_config_running.py
import sys
import logging 
from ncclient import manager
from ncclient import operations
log = logging.getLogger(__name__)

CREATE_INTERFACE = '''<config>
                 <ifm xmlns="http://www.huawei.com/netconf/vrp/huawei-ifm">
                   <interfaces>                     <interface>
                       <ifName></ifName>
                       <ifMtu>1300</ifMtu>                      </interface>
                    </interfaces>                  </ifm>
                </config>'''
#Fill the device information and establish a NETCONF session
def huawei_connect(host, port, user, password):
    return manager.connect(host=host,                           port=port,
                           username=user,
                           password=password,
                           hostkey_verify = False,
                           device_params={'name': "huawei"},
                           allow_agent = False,
                           look_for_keys = False)
def _check_response(rpc_obj, snippet_name):
    print("RPCReply for %s is %s" % (snippet_name, rpc_obj.xml))
    xml_str = rpc_obj.xml    
if "<ok/>" in xml_str:
	print("%s successful" % snippet_name)    
else:
    print("Cannot successfully execute: %s" % snippet_name)      

def test_edit_config_running(host, port, user, password):
    #1.Create a NETCONF session
    with huawei_connect(host, port=port, user=user, password=password) as m:
        #2.Send RPC and check RPC reply
        rpc_obj = m.edit_config(target='candidate', config=CREATE_INTERFACE)
        _check_response(rpc_obj, 'CREATE_INTERFACE')       
	m.commit()
if __name__ == '__main__':
	test_edit_config_running(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])