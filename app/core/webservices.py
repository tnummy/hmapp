from app.core.models.resource import Resource
import requests
import xmltodict
from flask import jsonify
from lxml import html
from collections import defaultdict


class Webservices(object):

    def __init__(self):
        # self.client = 'playground'
        # self.password = 'PZWcKUPyn'
        # self.baseurl = "https://ws-" + self.client + ".luceosolutions.com/rest/"
        #
        self.client = 'kfix'
        self.password = 'zZrnteUtu'
        self.baseurl = "https://ws-" + self.client + ".luceosolutions.com/rest/"

    def getReqForm(self):

        response = requests.get(self.baseurl + 'position/1/', auth=(self.client, self.password))
        rawReqForm = xmltodict.parse(response.text)['root']['result']['PropertyDetails']

        return rawReqForm

    def getPropTable(self):

        response = requests.get('https://ws-' + self.client + '.luceosolutions.com/rest/doc/requisitions',
                                auth=(self.client, self.password))
        page = html.fromstring(response.content)

        props = page.xpath('/html/body/div/div[2]/table/tbody/tr')

        flatten = lambda l: [item for sublist in l for item in sublist]
        propDict = []
        for p in props:
            req_field_type = p.xpath('./td[3]/text()')
            url = p.xpath('./td[4]/a/text()')
            if req_field_type == ['Integer']:
                field_type = ['number']
            elif len(url) > 0:
                field_type = ['select']
            elif req_field_type == ['Date']:
                field_type = ['date']
            else:
                field_type = ['text']

            propDict.append(flatten([p.xpath('./td[1]/text()'), p.xpath('./td[2]/text()'), field_type, url]))

        for p in propDict:
            if len(p) == 4:
                url = p.pop(3)
                response = xmltodict.parse(requests.get(url, auth=(self.client, self.password)).text)['root']
                # print response['recordCount']
                if int(response['recordCount']) > 1:
                    plist = []
                    for key, value in response['result'].items():
                        for piece in value:
                            # print key, value
                            plist.append({'id': piece['id'], 'lib': piece['lib']})
                    p.append(plist)
                else:
                    p.append([{'id': response['result']['item']['id'], 'lib': response['result']['item']['lib']}])

        return propDict


    def postReq(self):
        url = 'https://ws-' + self.client + '.luceosolutions.com/rest/position/'
        payload = {'params': 'Prop11:1;Prop27:90293;Prop28:78558;Prop29:78617;Prop34:90998;Prop35:90995;Prop36:91010;Prop38:Text example;Prop39:1;Prop40:2017-03-03 05:45:46;Prop42:5;Prop43:16;Prop44:Text example;Prop45:Text example;Prop66:Text example;Prop67:Text example;Prop88:Text example;Prop89:Text example;Prop96:Text example;Prop97:Text example;Prop143:38;Prop156:22;Prop157:51;Prop163:49;Prop169:40,48,69;Prop170:40;Prop171:40;Prop172:40;Prop174:13;Prop185:553,549,547;Prop299.lang:1;Prop299:1;Prop300.lang:1;Prop300:1;Prop2003:New York City, NY, US;Prop2004: eyJQcm9wNCI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOnRydWUsIm9yZGVyIjoyfSwiUHJvcDYiOnsiZW5hYmxlZCI6dHJ1ZSwibWFuZGF0b3J5Ijp0cnVlLCJvcmRlciI6MX0sIlByb3AxMSI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOmZhbHNlLCJvcmRlciI6OH0sIlByb3AxNSI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOnRydWUsIm9yZGVyIjowfSwiUHJvcDE2Ijp7ImVuYWJsZWQiOnRydWUsIm1hbmRhdG9yeSI6ZmFsc2UsIm9yZGVyIjo0fSwiUHJvcDE3Ijp7ImVuYWJsZWQiOnRydWUsIm1hbmRhdG9yeSI6dHJ1ZSwib3JkZXIiOjN9LCJQcm9wOTciOnsiZW5hYmxlZCI6dHJ1ZSwibWFuZGF0b3J5Ijp0cnVlLCJvcmRlciI6MTB9LCJQcm9wMTEyIjp7ImVuYWJsZWQiOnRydWUsIm1hbmRhdG9yeSI6ZmFsc2UsIm9yZGVyIjo2fSwiUHJvcDExMyI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOmZhbHNlLCJvcmRlciI6N30sIlJlc3VtZSI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOnRydWUsIm9yZGVyIjo1fX0=;Prop2006:DR32;Prop2010:Text example;Prop2011:Text example;Prop2012:Text example'}
        return requests.post(url, data=payload, auth=(self.client, self.password))