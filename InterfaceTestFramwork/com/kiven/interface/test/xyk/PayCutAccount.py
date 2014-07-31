# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def PayCutAccount():
    client = suds.client.Client(URL)
    result = client.service.PayCutAccount(**{u'PayCutAccountReq': {u'MerchantId': 'CTRP', u'RequestTime': 'test', u'FrozenReferenceNo': 'test', u'ReferenceNo': 'test'}})
    print result

if __name__ == '__main__':
    PayCutAccount()