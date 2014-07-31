# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def WithdrawSubmitByReferenceNo():
    client = suds.client.Client(URL)
    result = client.service.WithdrawSubmitByReferenceNo(**{u'WithdrawSubmitByReferenceNoReq': {u'WithdrawReferenceNo': 'test', u'MerchantUid': 'wwwwww', u'IsTerminate': 10, u'MerchantId': 'CTRP'}})
    print result

if __name__ == '__main__':
    WithdrawSubmitByReferenceNo()