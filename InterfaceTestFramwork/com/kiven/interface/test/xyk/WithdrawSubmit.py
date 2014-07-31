# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def WithdrawSubmit():
    client = suds.client.Client(URL)
    result = client.service.WithdrawSubmit(**{u'WithdrawSubmitReq': {u'BankCardType': 10, u'IdType': 10, u'RequestTime': 'test', u'MerchantUid': 'wwwwww', u'SubBranchName': 'test', u'WithdrawCardId': 'test', u'MobileNo': 'test', u'CardBankId': 10, u'Currency': 10, u'IdNo': 'test', u'BankCardNo': 'test', u'BankAccountName': 'test', u'UserIp': 'test', u'BankCode': 'test', u'BranchName': 'test', u'MerchantId': 'CTRP'}})
    print result

if __name__ == '__main__':
    WithdrawSubmit()