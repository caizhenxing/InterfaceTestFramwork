# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/account_ws/services/AccountService?wsdl'

def UnfreezeUser():
    client = suds.client.Client(URL)
    result = client.service.UnfreezeUser(**{u'UnfreezeUserReq': {u'UserId': 'test'}})
    print result

if __name__ == '__main__':
    UnfreezeUser()