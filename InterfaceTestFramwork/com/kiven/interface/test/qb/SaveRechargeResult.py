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
# SaveRechargeResult interface TestScript
def SaveRechargeResult():
	TIME = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
	client = suds.client.Client(URL)

	paramStruct = {u'SaveRechargeResultReq': {
			 u'RechargeReferenceNo': u'RechargeReferenceNo',
			 u'Status': u'Status',
			 u'RequestTime': u'RequestTime',
			 u'GwPayReferenceNo': u'GwPayReferenceNo',
			 u'MerchantData': u'MerchantData',
			 u'PaymentWay': u'PaymentWay',
			 u'Amount': u'Amount'
		}
	}

	result = client.service.SaveRechargeResult(**paramStruct)
	print result

	f = open(_THEPATH+'/result/'+'SaveRechargeResult-testReport.txt','a')
	f.writelines(TIME+'\n'+'Request:\n'+str(paramStruct)+'\n\n')
	f.writelines('Response:\n'+str(result)+'\n\n\n')
	f.close()

if __name__ == '__main__':
	SaveRechargeResult()