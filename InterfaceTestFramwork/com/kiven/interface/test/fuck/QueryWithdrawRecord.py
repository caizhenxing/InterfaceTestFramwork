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
# QueryWithdrawRecord interface TestScript
def QueryWithdrawRecord():
	TIME = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
	client = suds.client.Client(URL)

	paramStruct = {u'QueryWithdrawRecordReq': {
			 u'Status': u'Status',
			 u'BankCardNo': u'BankCardNo',
			 u'MerchantUid': 'wwwwww',
			 u'Page': u'Page',
			 u'ReferenceNo': u'ReferenceNo',
			 u'MerchantId': 'CTRP',
			 u'QueryMonth': u'QueryMonth',
			 u'BankCode': u'BankCode',
			 u'CardBankId': u'CardBankId',
			 u'RowsPerPage': u'RowsPerPage'
		}
	}

	result = client.service.QueryWithdrawRecord(**paramStruct)
	print result

	f = open(_THEPATH+'/result/'+'QueryWithdrawRecord-testReport.txt','a')
	f.writelines(TIME+'\n'+'Request:\n'+str(paramStruct)+'\n\n')
	f.writelines('Response:\n'+str(result)+'\n\n\n')
	f.close()

if __name__ == '__main__':
	QueryWithdrawRecord()