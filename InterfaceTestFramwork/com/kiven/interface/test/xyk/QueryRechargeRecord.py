# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def QueryRechargeRecord():
    client = suds.client.Client(URL)
    result = client.service.QueryRechargeRecord(**{u'QueryRechargeRecordReq': {u'Status': 10, u'MerchantUid': 'wwwwww', u'ReferenceNo': 'test', u'MerchantId': 'CTRP', u'QueryMonth': 'test', u'Page': 10, u'RowsPerPage': 10}})
    print result

if __name__ == '__main__':
    QueryRechargeRecord()