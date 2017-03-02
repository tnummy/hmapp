from app.core.models.resource import Resource
import requests
import xmltodict
from flask import jsonify


class Webservices():

    def getReqForm(self):

        # resources = []
        # resources.append(Resource('Large app how to', 'https://github.com/mitsuhiko/flask/wiki/Large-app-how-to'))
        # resources.append(Resource('Modular Applications with Blueprints', 'http://flask.pocoo.org/docs/blueprints/#blueprints'))
        # resources.append(Resource('Flask Mega-Tutorial', 'http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-ajax'))

        client = 'playground'
        password = 'PZWcKUPyn'



        baseurl = "https://ws-" + client + ".luceosolutions.com/rest/"


        # r = requests.get(url, auth=(client, password))

        # payload = {'params':'Prop194:test;'}
        # r = requests.post(url, data=payload, auth=(username, password))

        # print r.text

        response = requests.get(baseurl + "position/1/", auth=(client, password))
        rawReqForm = xmltodict.parse(response.text)['root']['result']['PropertyDetails']

        return rawReqForm