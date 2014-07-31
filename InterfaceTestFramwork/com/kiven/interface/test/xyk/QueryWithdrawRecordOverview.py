# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def QueryWithdrawRecordOverview():
    client = suds.client.Client(URL)
    result = client.service.QueryWithdrawRecordOverview(**{u'QueryWithdrawRecordOverviewReq': {u'Status': 10, u'BankCardNo': 'test', u'MerchantUid': 'wwwwww', u'LastReferenceNo': 'test', u'ReferenceNo': 'test', u'MerchantId': 'CTRP', u'QueryMonth': 'test', u'BankCode': 'test', u'CardBankId': 10, u'RowsPerPage': 10}})
    print result

if __name__ == '__main__':
    QueryWithdrawRecordOverview()