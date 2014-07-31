# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/account_ws/services/AccountService?wsdl'

def IsInWhiteList():
    client = suds.client.Client(URL)
    result = client.service.IsInWhiteList(**{u'IsInWhiteListReq': {u'MerchantUid': 'wwwwww', u'MerchantId': 'CTRP'}})
    print result

if __name__ == '__main__':
    IsInWhiteList()