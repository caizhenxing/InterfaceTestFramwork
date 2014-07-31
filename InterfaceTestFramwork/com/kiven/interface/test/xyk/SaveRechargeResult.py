# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

def SaveRechargeResult():
    client = suds.client.Client(URL)
    result = client.service.SaveRechargeResult(**{u'SaveRechargeResultReq': {u'RechargeReferenceNo': 'test', u'Status': 10, u'RequestTime': 'test', u'GwPayReferenceNo': 'test', u'MerchantData': 'test', u'PaymentWay': 'test'}})
    print result

if __name__ == '__main__':
    SaveRechargeResult()