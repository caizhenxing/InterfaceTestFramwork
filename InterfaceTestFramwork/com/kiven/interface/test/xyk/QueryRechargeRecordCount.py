# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def QueryRechargeRecordCount():
    client = suds.client.Client(URL)
    result = client.service.QueryRechargeRecordCount(**{u'QueryRechargeRecordCountReq': {u'Status': 10, u'ReferenceNo': 'test', u'QueryMonth': 'test', u'MerchantUid': 'wwwwww', u'MerchantId': 'CTRP'}})
    print result

if __name__ == '__main__':
    QueryRechargeRecordCount()