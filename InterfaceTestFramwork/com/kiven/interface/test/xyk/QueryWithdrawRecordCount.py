# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def QueryWithdrawRecordCount():
    client = suds.client.Client(URL)
    result = client.service.QueryWithdrawRecordCount(**{u'QueryWithdrawRecordCountReq': {u'Status': 10, u'BankCardNo': 'test', u'MerchantUid': 'wwwwww', u'ReferenceNo': 'test', u'MerchantId': 'CTRP', u'QueryMonth': 'test', u'BankCode': 'test', u'CardBankId': 10}})
    print result

if __name__ == '__main__':
    QueryWithdrawRecordCount()