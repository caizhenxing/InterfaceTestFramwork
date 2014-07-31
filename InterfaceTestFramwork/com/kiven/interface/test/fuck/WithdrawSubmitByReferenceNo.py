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
# WithdrawSubmitByReferenceNo interface TestScript
def WithdrawSubmitByReferenceNo():
	TIME = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
	client = suds.client.Client(URL)

	paramStruct = {u'WithdrawSubmitByReferenceNoReq': {
			 u'WithdrawReferenceNo': u'WithdrawReferenceNo',
			 u'MerchantUid': 'wwwwww',
			 u'IsTerminate': u'IsTerminate',
			 u'MerchantId': 'CTRP'
		}
	}

	result = client.service.WithdrawSubmitByReferenceNo(**paramStruct)
	print result

	f = open(_THEPATH+'/result/'+'WithdrawSubmitByReferenceNo-testReport.txt','a')
	f.writelines(TIME+'\n'+'Request:\n'+str(paramStruct)+'\n\n')
	f.writelines('Response:\n'+str(result)+'\n\n\n')
	f.close()

if __name__ == '__main__':
	WithdrawSubmitByReferenceNo()