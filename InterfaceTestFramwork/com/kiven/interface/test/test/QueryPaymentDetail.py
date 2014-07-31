# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds

URL = 'http://10.2.6.244/account_ws/services/AccountService?wsdl'

def QueryPaymentDetail():
    client = suds.client.Client(URL)
    result = client.service.QueryPaymentDetail(**{u'QueryPaymentDetailReq': {u'MoneySource': 10, u'MerchantUid': 'wwwwww', u'ReferenceNo': 'test', u'Page': 10, u'QueryMonth': 'test', u'MoneyFlows': 10, u'MerchantId': 'CTRP', u'RowsPerPage': 10}})
    print result

if __name__ == '__main__':
    QueryPaymentDetail()