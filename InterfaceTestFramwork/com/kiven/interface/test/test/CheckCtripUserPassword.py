# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/account_ws/services/AccountService?wsdl'

def CheckCtripUserPassword():
    client = suds.client.Client(URL)
    result = client.service.CheckCtripUserPassword(**{u'CheckCtripUserPasswordReq': {u'Password': 'test', u'Uid': 'test', u'LoginType': 'test'}})
    print result

if __name__ == '__main__':
    CheckCtripUserPassword()