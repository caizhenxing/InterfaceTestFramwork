# -*- coding:utf-8 -*-

# build by framework

__author__ = 'kiven'

import suds,os,time

URL = 'http://10.2.6.244/tx_ws/services/TxService?wsdl'

'''
please change the paramStruct's value by yourself
'''

# project root path
_THEPATH = os.path.join(os.path.dirname(__file__), os.pardir,os.pardir)

# to log file
# PayRefundAccount interface TestScript
def PayRefundAccount():
	TIME = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
	client = suds.client.Client(URL)

	paramStruct = {u'PayRefundAccountReq': {
			 u'MerchantId': 'CTRP',
			 u'RequestTime': u'RequestTime',
			 u'Amount': u'Amount',
			 u'FrozenReferenceNo': u'FrozenReferenceNo',
			 u'ReferenceNo': u'ReferenceNo'
		}
	}

	result = client.service.PayRefundAccount(**paramStruct)
	print result

	f = open(_THEPATH+'/result/'+'PayRefundAccount-testReport.txt','a')
	f.writelines(TIME+'\n'+'Request:\n'+str(paramStruct)+'\n\n')
	f.writelines('Response:\n'+str(result)+'\n\n\n')
	f.close()

if __name__ == '__main__':
	PayRefundAccount()