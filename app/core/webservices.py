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

        response = requests.get(self.baseurl + 'doc/requisitions', auth=(self.client, self.password))
        page = html.fromstring(response.content)
        props = page.xpath('/html/body/div/div[2]/table/tbody/tr')
        # prop_info = page.xpath('//option/@value')
        # / html / body / div / div[2] / table / tbody / tr[1] / td[1]
        # propDict = defaultdict()
        propDict = []
        for prop in props:
            # propDict[prop[0]] = [prop[1]]
            propDict.append(prop[0])
        # term_list = []
        # for i in xrange(0, len(terms)):
        #     term_list.append({'value': term_ids[i], 'term': terms[i]})
        #
        # if return_list:
        #     return term_list

        # response = requests.get(self.baseurl + 'doc/requisitions', auth=(self.client, self.password))
        # rawReqForm = html.fromstring(response.content)

        return propDict[0]
        # return