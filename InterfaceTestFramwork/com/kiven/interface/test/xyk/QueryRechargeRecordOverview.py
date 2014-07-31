# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def QueryRechargeRecordOverview():
    client = suds.client.Client(URL)
    result = client.service.QueryRechargeRecordOverview(**{u'QueryRechargeRecordOverviewReq': {u'Status': 10, u'MerchantUid': 'wwwwww', u'LastReferenceNo': 'test', u'ReferenceNo': 'test', u'QueryMonth': 'test', u'MerchantId': 'CTRP', u'RowsPerPage': 10}})
    print result

if __name__ == '__main__':
    QueryRechargeRecordOverview()