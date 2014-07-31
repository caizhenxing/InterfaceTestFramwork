# -*- coding:utf-8 -*-


'''
WebService PFTest
'''

#requests imports
from requests import Session

#system imports
from xml.dom import minidom
import os
import threading


#XMLPATH
_XMLPATHGE=lambda XMLNAME:os.path.join(os.path.abspath(os.getcwd()),XMLNAME+'.xml')

#ERROR信息,错误码,错误信息
_ERROR={}

#必要的全局定义
HEADERS={'User-Agent':'gSOAP/2.8','Connection':'keep-alive'}
URL="http://172.16.121.17/cui/cui.fcgi"
METHOD='POST'


class reqUsers(object):

    '''
    用户类
    创建一个用户时给到一个会话实例并且绑定到这个用户上
    '''

    def __init__(self,username,password,session=Session()):

        self.username=username
        self.password=password
        self.session=session

        #初始化的时候需要直接构造登录的xml请求体
        reqContentGe('Login',{

            'userName':self.username,
            'password':self.password,

        })



class reqContentGe(object):

    '''
    用于生成业务请求body体,并自动进行存储
    '''

    def __init__(self,REQ_NAME,REQ_PRAM):

        self.REQ_NAME=REQ_NAME
        self.REQ_PRAM=REQ_PRAM

        self.k=[]
        self.v=[]

        #初始化时调用
        self._toXML()

    #递归生成两个容器,用于_toXML方法
    def _listDic(self,testdic):
        if not isinstance(testdic,dict):
            pass
        else:
            for k,v in testdic.iteritems():

                self.k.append(k)
                self.v.append(v)

                #递归
                self._listDic(v)


    def _toXML(self):

        #存储用户生成的请求体xml文件
        xmltmp=open(_XMLPATHGE(self.REQ_NAME),'w')

        #创建一个xml文档对象
        XMLDOC=minidom.Document()

        #自动构建请求主体
        ENVNode=XMLDOC.createElement("SOAP-ENV:Envelope")

        #必要的xml格式
        ENVNode.setAttribute('xmlns:SOAP-ENV','http://schemas.xmlsoap.org/soap/envelope/')
        ENVNode.setAttribute('xmlns:SOAP-ENC','http://schemas.xmlsoap.org/soap/encoding/')
        ENVNode.setAttribute('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
        ENVNode.setAttribute('xmlns:xsd','http://www.w3.org/2001/XMLSchema')
        ENVNode.setAttribute('xmlns:cusdk','urn:cusdk')

        XMLDOC.appendChild(ENVNode)
        REQBody=XMLDOC.createElement("SOAP-ENV:Body")
        ENVNode.appendChild(REQBody)

        REQName=XMLDOC.createElement("cusdk:"+self.REQ_NAME)
        REQBody.appendChild(REQName)

        REQreq=XMLDOC.createElement("cusdk:req")
        REQreq.setAttribute('xsi:type','cusdk:'+self.REQ_NAME+'Req')
        REQName.appendChild(REQreq)

        #先内部递归生成两个列表
        self._listDic(self.REQ_PRAM)

        #根据两个列表智能生成xml,目前支持两层嵌套
        for nodeitem in self.k:

            valueitem=self.v[self.k.index(nodeitem)]

            if not isinstance(valueitem,dict):
                #print "%s is %s" % (nodeitem,valueitem)
                valueitem=XMLDOC.createTextNode(valueitem)
                nodeitem=XMLDOC.createElement(nodeitem)
                nodeitem.appendChild(valueitem)
                #再将最外层的包裹上
                REQreq.appendChild(nodeitem)
            else:
                nodeitem=XMLDOC.createElement(nodeitem)
                #print nodeitem
                #print "->"*count+nodeitem
                for key,kvalue in valueitem.iteritems():
                    #如果不是个字典
                    if not isinstance(kvalue,dict):
                        #算法核心部分
                        self.k.remove(key)
                        self.v.remove(kvalue)
                        #print "%s is %s" % (key,kvalue)
                        kvalue=XMLDOC.createTextNode(kvalue)
                        key=XMLDOC.createElement(key)
                        #包裹上
                        key.appendChild(kvalue)
                        nodeitem.appendChild(key)

                    #如果还是字典的话要嵌套处理
                    else:

                        key=XMLDOC.createElement(key)
                        nodeitem.appendChild(key)

                    #最后用REQreq包裹上最外层
                    REQreq.appendChild(nodeitem)


        #生成xml请求体,格式化缩进
        XMLDOC.writexml(xmltmp,'\t','\t','\n',encoding='UTF-8')
        #关闭文件对象
        xmltmp.close()


class wbpError(Exception):

    '''
    自定义WBPFtest的异常类
    '''

    def __init__(self,errorcode,errorinfo):

        self.errorcode=errorcode
        self.errorinfo=errorinfo

    def __str__(self):

        return '错误码:%s-错误信息:%s' % (self.errorcode,self.errorinfo)



if __name__=="__main__":

    user1=reqUsers(r'admin@xxxxxx',r'888888')
    requestbody=''
    requestfile=open('Login.xml','r')

    for line in requestfile.readlines():
        requestbody+=line


    print requestbody #Debug


    res=user1.session.request(method=METHOD,url=URL,data=requestbody,headers=HEADERS,timeout=6000)
    requestfile.close()

    print res.text