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
# WithdrawSubmit interface TestScript
def WithdrawSubmit():
	TIME = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
	client = suds.client.Client(URL)

	paramStruct = {u'WithdrawSubmitReq': {
			 u'BankCardType': u'BankCardType',
			 u'IdType': u'IdType',
			 u'RequestTime': u'RequestTime',
			 u'MerchantUid': 'wwwwww',
			 u'SubBranchName': u'SubBranchName',
			 u'WithdrawCardId': u'WithdrawCardId',
			 u'MobileNo': u'MobileNo',
			 u'IdNo': u'IdNo',
			 u'CardBankId': u'CardBankId',
			 u'Currency': u'Currency',
			 u'Amount': u'Amount',
			 u'BankCardNo': u'BankCardNo',
			 u'BankAccountName': u'BankAccountName',
			 u'UserIp': u'UserIp',
			 u'BankCode': u'BankCode',
			 u'BranchName': u'BranchName',
			 u'MerchantId': 'CTRP'
		}
	}

	result = client.service.WithdrawSubmit(**paramStruct)
	print result

	f = open(_THEPATH+'/result/'+'WithdrawSubmit-testReport.txt','a')
	f.writelines(TIME+'\n'+'Request:\n'+str(paramStruct)+'\n\n')
	f.writelines('Response:\n'+str(result)+'\n\n\n')
	f.close()

if __name__ == '__main__':
	WithdrawSubmit()