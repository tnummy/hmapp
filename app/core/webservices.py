from app.core.models.resource import Resource
import requests
import xmltodict
from flask import jsonify
from lxml import html
from collections import defaultdict


class Webservices(object):

    def __init__(self):
        self.client = 'playground'
        self.password = 'PZWcKUPyn'
        self.baseurl = "https://ws-" + self.client + ".luceosolutions.com/rest/"

    def getReqForm(self):

        # resources = []
        # resources.append(Resource('Large app how to', 'https://github.com/mitsuhiko/flask/wiki/Large-app-how-to'))
        # resources.append(Resource('Modular Applications with Blueprints', 'http://flask.pocoo.org/docs/blueprints/#blueprints'))
        # resources.append(Resource('Flask Mega-Tutorial', 'http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-ajax'))






        # r = requests.get(url, auth=(client, password))

        # payload = {'params':'Prop194:test;'}
        # r = requests.post(url, data=payload, auth=(username, password))

        # print r.text

        response = requests.get(self.baseurl + 'position/1/', auth=(self.client, self.password))
        rawReqForm = xmltodict.parse(response.text)['root']['result']['PropertyDetails']

        return rawReqForm

    def getPropTable(self):

        response = requests.get('https://ws-playground.luceosolutions.com/rest/doc/requisitions',
                                auth=('playground', 'PZWcKUPyn'))
        page = html.fromstring(response.content)

        props = page.xpath('/html/body/div/div[2]/table/tbody/tr')

        flatten = lambda l: [item for sublist in l for item in sublist]
        propDict = []
        for p in props:
            req_field_type = p.xpath('./td[3]/text()')
            url = p.xpath('./td[4]/a/text()')
            if req_field_type == 'Integer':
                field_type = ['number']
            elif len(url) > 0:
                field_type = ['select']
            elif req_field_type == 'Date':
                field_type = ['date']
            else:
                field_type = ['text']

            propDict.append(flatten([p.xpath('./td[1]/text()'), p.xpath('./td[2]/text()'), field_type, url]))

        for p in propDict:
            if len(p) == 4:
                url = p.pop(3)
                response = xmltodict.parse(requests.get(url, auth=('playground', 'PZWcKUPyn')).text)['root']
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