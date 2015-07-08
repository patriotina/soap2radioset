__author__ = 'patriot'
## encoding=utf-8

import logging
from suds.client import Client
from suds.transport.http import HttpTransport as SudsHttpTransport
from suds.transport.https import HttpTransport as SudsHttpsTransport
import os


class WellBehavedHttpTransport(SudsHttpTransport):
    """HttpTransport which properly obeys the ``*_proxy`` environment variables."""
    def u2handlers(self):
        return []


class WellBehavedHttpsTransport(SudsHttpsTransport):
    def u2handlers(self):
        return []


def getSoap1():
# Configure HTTP proxy from OS environment (e.g. http_proxy="http://proxy.example.com:8080")
    proxyOpts = dict()
    proxyOpts = {'http': 'panyukov:pea315@proxy.belkam.com:8090', 'https': 'panyukov:pea315@proxy.belkam.com:8090'}
#d = dict(http='panyukov:pea315@proxy.belkam.com:8090')

# Send log messages to console
    #logging.basicConfig(level=logging.INFO)
# Set Suds logging level to debug, outputs the SOAP messages.
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)
    #logging.getLogger('suds.transport').setLevel(logging.DEBUG)

    print "Connection..."
    url = 'https://service.rkn.gov.ru/services/Claims.test'
    urlwsdl = 'http://service.rkn.gov.ru/services/Claims/?wsdl'
    client = Client(urlwsdl, proxy=proxyOpts, timeout=360)
    client.set_options(proxy=proxyOpts)
    return client
#print client
#response = client.getDicETSKind()


"""
def getDicPolarization():
    #Справочник поляризаций
    getSoap1()

    response = client.service.getDicPolarization()
    return response
"""


def getDicETSKind():
    # справочник видов РЭС из Единого технического справочника РЭС и ВЧУ

    response = getSoap1().service.getDicETSKind()
    return response


def getDicETSType():
    #справочник наименований РЭС из Единого технического справочника РЭС и ВЧУ
    ## !!! требуется дата старта и дата окончания!!!
    print "load ETS_Type"
    response = getSoap1().service.getDicETSType()
    return response


def getDicRSNParts():
    #для получения списка территориальных Управлений Роскомнадзора.
    ##!!! DateTimeStart DateTimeEnd
    response = getSoap1().service.getDicRSNParts()
    return response


def getDicSectorType():
    #для получения списка типов антенн

    response = getSoap1().service.getDicSectorType()
    return response


def getDicPolarization():
    #4.5 для получения списка видов поляризаций

    response = getSoap1().service.getDicPolarization()
    return response


def getDicRadClass():
    #4.6 для получения списка классов излучения

    response = getSoap1().service.getDicRadClass()
    return response


# client = SoapClient(wsdl="https://service.rkn.gov.ru/services/Claims.test/",trace=False)
#response = client.sendClaim('test')
#result = response['AddResult']
#print result

#etslist = getDicETSType()
#print type(etslist)
#print type(etslist[0])
#print type(etslist[0][0])
#print len(etslist[0][0])
#for ets in etslist:
#print len(etslist[0])
#print len(etslist[0][0])
#print etslist[0][0][0]
#print etslist[0][0][1]
#print etslist[0][0][2]

#reslist = getDicPolarization()
#print reslist