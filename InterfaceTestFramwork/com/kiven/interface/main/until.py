# -*- coding:utf-8 -*-
__author__ = 'kiven'

import suds
import re
import requests
import xml.dom.minidom
import sys,os
import time,string
from BeautifulSoup import BeautifulSoup

# wsdl接口文档地址
url = [
    'http://10.2.6.244/tx_ws/services/TxService?wsdl',
    'http://10.2.6.244/account_ws/services/AccountService?wsdl'
]
# 参数类型
pType = {'string':'string','int':'int','long':'long'}

# 保存所有接口名称
interfaceName = []
# 有用接口名称
usableInterfaceName = []
# 保存所有接口类型
allInterfaceType = []
# 保存接口参数
allInterfaceParams = []
# 所有测试接口相关信息
testInterfaceInfo = {}
# 接口测试文件代码内容
functionString = ''

# 被测接口所属服务     钱包..信用卡...此参数需经常改动
TestServiceName = 'qb'
# wsdl文件名  不同服务不同wsdl
_xmlname = 'schema.xml'

# 固定的商户UID和id
MERCHANTUID = {'MerchantUid':'wwwwww'}
MERCHANTID = {'MerchantId':'CTRP'}

# 项目根目录
_THEPATH = os.path.join(os.path.dirname(__file__), os.pardir)



# 获取wsdl文档中定义的所有接口名称和参数
def getInterfaceName():
    try:
        f = open(_xmlname)
        dom = xml.dom.minidom.parseString(f.read())
    finally:
        f.close()

    if dom != None:
        # 得到xml文档
        root = dom.documentElement
        # 获取schema节点
        schemaNodes = root.getElementsByTagName('xs:schema')
        # 得到nodelist的第一个
        schemaNode = schemaNodes[0]
        # 在schema节点下获取complexType节点
        elementNodes = schemaNode.getElementsByTagName('xs:complexType')

        # 得到所有接口名称
        for element in elementNodes:
            # 排除其他选项
            temp = element.getAttribute('name')
            if not temp.endswith('Rsp'):
                if not temp.endswith('Req'):
                    if not temp.endswith('Response'):
                        # 保存至字典
                        interfaceName.append(temp)

        # 得到所有接口的参数
        for element in elementNodes:
            tmpList = []
            temp = element.getAttribute('name')
            if temp.endswith('Req'):
                # print u'接口:'+temp
                allInterfaceType.append(temp)
                params = element.getElementsByTagName('xs:element')
                for param in params:
                    # 参数名称
                    key = param.getAttribute('name')
                    # 参数类型
                    type = param.getAttribute('type')
                    tmpList.append(key)
                    # 直接获取到的类型是这样的:xs:string  因此分割截取
                    tmpList.append(type.split(':')[1])
                allInterfaceParams.append(tmpList)

    # print interfaceName
    #     print allInterfaceType
    #     print allInterfaceParams
    for i in xrange(len(allInterfaceType)):
        testInterfaceInfo[allInterfaceType[i]] = allInterfaceParams[i]

    return testInterfaceInfo

# 根据接口获取相应的参数和参数类型
def interface_to_get_params(interfaceName):
    if not interfaceName.endswith('Req'):
        interfaceName += 'Req'
    #  先获取所有接口相关信息
    info = getInterfaceName()
    return info[interfaceName]

# 获取有用接口
def getUsableInterface(iname,itype):
    # 先获取所有接口信息
    getInterfaceName()
    for i in xrange(len(iname)):
        iname[i] += 'Req'
        if iname[i] in itype:
            usableInterfaceName.append(iname[i][:-3])
    return usableInterfaceName



# 生成参数结构  例:{'类型':{'字段':'值','字段':'值','字段':'值'}}
def createParamsStruct(interfaceName):
    paramsStruct = {}   # 参数结构
    value = {}          # 值
    p = []              # 参数
    t = []              # 类型
    pDict = {}
    interfaceName += 'Req'
    info = getInterfaceName()
    params = info[interfaceName]
    # 参数个数
    num = len(params)/2
    # 参数取值0,0+2,0+2+2
    for i in xrange(0,len(params),2):
        p.append(params[i])
    for j in xrange(1,len(params),2):
        t.append(params[j])
    for k in xrange(num):
        if t[k] == 'string':
            if p[k] == 'MerchantUid':
                pDict[p[k]] = 'wwwwww'
            elif p[k] == 'MerchantId':
                pDict[p[k]] = 'CTRP'
            else:
                pDict[p[k]] = p[k]
        else:
            pDict[p[k]] = p[k]
    # print pDict

    paramsStruct[interfaceName] = pDict
    s = '{'
    for c in str(paramsStruct)[1:len(str(paramsStruct))-1] :
        if c != '{':
            if c != '}':
                if c != ',':
                    s += c
                else:
                    s += ',\n\t\t\t'
            else:
                s += '\n\t\t}'
        else:
            s += '{\n\t\t\t '
    s += '\n\t}'
    print s
    return s

    # print p,t

    # print params


# # 用于解析报文xxxxxxxxxxxxxxxxxxxxxxxxxxxx无用方法
# def analyze_msgBody():
#     a = []
#     count = 0
#     interface = []
#     file_obj = open(u'D:\python_workspace\提现相关报文.txt','r')
#     for line in file_obj:
#         if line.startswith('<soap'):
#             a.append(line)
#             count += 1
#     # print a[13]
#     # file_text = file_obj.readlines()
#     # print file_text
#     for i in xrange(0,count):
#         print i
#     file_obj.close()


# 获取wsdl并保存至本地
def getWsdlXml():
    r = requests.get(url[0])
    f = open(_xmlname,'w')
    f.write(r.text)
    f.close()


# 根据接口名称生成该接口的测试脚本
def webserviceTestBuilder(interface):
    # # 参数结构{'类型':{'字段':'值','字段':'值','字段':'值'}}
    # GetWithdrawRecordByReferenceNoReq ={
    #     'GetWithdrawRecordByReferenceNoReq' : {
    #         'MerchantUid':"wwwwww",
    #         'MerchantId':"CTRP",
    #         'ReferenceNo':"20140721000000000000158"
    #     }
    # }

    # a = []
    # client = suds.client.Client(url[0])
    # a.append(client.wsdl.services)
    # print a
    # print client.wsdl.messages.keys()  #this can be a list
    # interface_schema = client.wsdl.schema  #获取wsdl文档的schema
    # f = open('schema.xml','w')
    # f.write(str(interface_schema))
    # f.close()
    # getInterface(interface_schema)
    # print interface_schema

    # 得到格式化的参数结构体
    paramStruct = createParamsStruct(interface)
    # print paramStruct
    # 根据接口名,调用该接口
    functionString = 'client.service.'+interface+'(**paramStruct)'

    list_of_text_strings = "" \
                           "# -*- coding:utf-8 -*-\n\n# build by framework\n\n__author__ = 'kiven'\n\nimport suds,os,time\n\n" \
                           "URL = '"+ url[0] +"'\n\n" \
                           "'''\nplease change the paramStruct's value by yourself\n'''\n\n" \
                           "# project root path\n" \
                           "_THEPATH = os.path.join(os.path.dirname(__file__), os.pardir,os.pardir)\n\n" \
                           "# to log file\n" \
                           "# "+ interface +" interface TestScript\n" \
                           "def "+interface+"():\n" \
                           "\tTIME = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))\n" \
                           "\tclient = suds.client.Client(URL)\n\n" \
                           "\tparamStruct = "+ paramStruct +"\n\n"\
                           "\tresult = "+functionString+"\n" \
                           "\tprint result\n\n" \
                           "\tf = open(_THEPATH+'/result/'+'"+ interface +"-testReport.txt','a')\n" \
                           "\tf.writelines(TIME+'\\n'+'Request:\\n'+str(paramStruct)+'\\n\\n')\n" \
                           "\tf.writelines('Response:\\n'+str(result)+'\\n\\n\\n')\n" \
                           "\tf.close()\n\n" \
                           "if __name__ == '__main__':\n" \
                           "\t"+interface+"()"

    '''
    __file__：当前文件路径
    os.path.dirname(file): 某个文件所在的目录路径
    os.path.join(a, b, c,....): 路径构造 a/b/c
    os.path.abspath(path): 将path从相对路径转成绝对路径
    os.pardir: Linux下相当于"../"

    print os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    '''
    file_obj = open(_THEPATH+'/test/'+ TestServiceName +'/'+interface+'.py','w')
    file_obj.writelines(list_of_text_strings)
    file_obj.close()
    # result = client.service.GetWithdrawLimit(**paramStruct)
    # print result

'''报告类'''
class _toHtmlReport(object):
    _TIME = ''
    # 初始化时间戳
    def __init__(self):
        # 当前时间
        self._TIME = time.strftime('%Y%m%d',time.localtime(time.time()))

    '''
    固定格式生成
    '''
    def generateReport(self):
        # 固定内容
        TEXT = "<html>\n" \
               "<head>\n" \
               "<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n" \
               "<style type='text/css'>" \
               "    #summary{font-family:\"Trebuchet MS\", Arial, Helvetica, sans-serif; width:100%;border-collapse:collapse;}\n" \
               "    #summary td, #summary th{font-size:0.8em;border:1px solid #98bf21;padding:3px 7px 2px 7px;}\n" \
               "    #summary th{font-size:1.0em;text-align:left;padding-top:5px;padding-bottom:4px;background-color:#A7C942;color:#ffffff;}\n" \
               "    #componentWiseSummary{font-family:\"Trebuchet MS\", Arial, Helvetica, sans-serif;width:100%;border-collapse:collapse;}\n" \
               "    #summary td, #summary th{font-size:0.8em;border:1px solid #98bf21;padding:3px 7px 2px 7px;}\n" \
               "    #summary th{font-size:1.0em;text-align:left;padding-top:5px;padding-bottom:4px;background-color:#A7C942;color:#ffffff;}\n" \
               "    #customers{font-family:\"Trebuchet MS\", Arial, Helvetica, sans-serif;width:100%;border-collapse:collapse;}\n" \
               "    #customers td, #customers th{font-size:0.8em;border:1px solid #98bf21;padding:3px 7px 2px 7px;}\n" \
               "    #customers th{font-size:1.1em;text-align:left;padding-top:5px;padding-bottom:4px;background-color:#A7C942;color:#ffffff;}\n" \
               "    #customers tr.alt td{color:#000000;background-color:#EAF2D3;}\n" \
               "</style>\n" \
               "</head>\n" \
               "<body text-align:center>\n" \
               "<table width=100% border=0 cellpadding=2 cellspacing=2>\n" \
               "<tbody>\n" \
               "<tr>\n" \
               "<td>\n" \
               "<table width=100% border=0 cellpadding=2 cellspacing=2>\n" \
               "<tbody>\n" \
               "<tr>\n" \
               "<td align=center><p class=title><h1>接 口 测 试 报 告</h1></p></td></tr>\n" \
               "</tr></tbody></table><br>\n" \
               "<table id=\"customers\">\n" \
               "<tr>\n" \
               "<th>CaseID</th>\n" \
               "<th>Interface Name</th>\n" \
               "<th>Parameters</th>\n" \
               "<th>Result</th>\n" \
               "</tr>\n" \
               "</body>\n" \
               "</html>\n"
        file_obj = open(_THEPATH + '/Case/' + self._TIME + '-Report.html','w')
        file_obj.writelines(TEXT)
        file_obj.close()

    # 每条接口通过状态
    def sendStatusToReport(self,id,interfaceName,params,result='N/A'):
        myid = string.atoi(id)
        f = open(_THEPATH + '/Case/' + self._TIME + '-Report.html','a')
        if myid%2 == 0:
            if result.upper() == 'FAIL':
                f.write("<tr bgcolor=#FF0000>")
            else:
                f.write("<tr>")
        else:
            if result.upper() =='FAIL':
                f.write("<tr bgcolor=#FF0000>")
            else:
                f.write("<tr bgcolor=#EAF2D3>")
        f.write("<td><b>" + id + "</b></td>")
        f.write("<td><b>" + interfaceName + "</b></td>")
        f.write("<td><b>" + params + "</b></td>")
        f.write("<td><b>" + result + "</b></td>")
        f.write("</tr>")
        f.close()



if __name__ == '__main__':
    # report = _toHtmlReport()
    # report.generateReport()
    # report.sendStatusToReport('1','TestInterface','id=2','Pass')
    # report.sendStatusToReport('2','TestInterface','id=2','Fail')


    # createParamsStruct('CreateRechargeOrder')

    # 先去下载wsdl文件
    getWsdlXml()
    # 为不同服务创建不同的包
    if not os.path.exists(_THEPATH+'/test/'+TestServiceName+'/'):
        # 包不存在则创建包
        os.makedirs(_THEPATH+'/test/'+TestServiceName+'/')
    # 所有可测试的接口
    usable = getUsableInterface(interfaceName,allInterfaceType)

    # print usable    # 可测试接口名称
    # print allInterfaceType  # 参数类型
    print allInterfaceParams    # 参数
    # 批量生成测试接口脚本
    for i in xrange(len(usable)):
        webserviceTestBuilder(usable[i])