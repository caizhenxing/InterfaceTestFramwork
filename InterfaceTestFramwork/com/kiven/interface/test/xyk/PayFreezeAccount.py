# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def PayFreezeAccount():
    client = suds.client.Client(URL)
    result = client.service.PayFreezeAccount(**{u'PayFreezeAccountReq': {u'RequestTime': 'test', u'MerchantUid': 'wwwwww', u'ItemDesc': 'test', u'ReferenceNo': 'test', u'ItemName': 'test', u'MerchantId': 'CTRP'}})
    print result

if __name__ == '__main__':
    PayFreezeAccount()