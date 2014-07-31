# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def GetWithdrawLimit():
    client = suds.client.Client(URL)
    result = client.service.GetWithdrawLimit(**{u'GetWithdrawLimitReq': {u'MerchantUid': 'wwwwww', u'MerchantId': 'CTRP'}})
    print result

if __name__ == '__main__':
    GetWithdrawLimit()