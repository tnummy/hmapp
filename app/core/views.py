from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
from app.core.webservices import *
import requests
import xmltodict

mod = Blueprint('core', __name__)

@mod.route('/')
def index():
  # repository = Repository()
  # return (render_template('core/index.html', resources=repository.getResources()))

    ws = Webservices()
    return (render_template('core/index.html', req=ws.getPropTable()))
    # return jsonify(ws.getPropTable())



@mod.route('/post', methods=['POST'])
def post():
  if request.method == 'POST':
    field_data = request.form
    payloadData = 'Prop2004:eyJQcm9wNCI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOnRydWUsIm9yZGVyIjoyfSwiUHJvcDYiOnsiZW5hYmxlZCI6dHJ1ZSwibWFuZGF0b3J5Ijp0cnVlLCJvcmRlciI6MX0sIlByb3AxMSI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOmZhbHNlLCJvcmRlciI6OH0sIlByb3AxNSI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOnRydWUsIm9yZGVyIjowfSwiUHJvcDE2Ijp7ImVuYWJsZWQiOnRydWUsIm1hbmRhdG9yeSI6ZmFsc2UsIm9yZGVyIjo0fSwiUHJvcDE3Ijp7ImVuYWJsZWQiOnRydWUsIm1hbmRhdG9yeSI6dHJ1ZSwib3JkZXIiOjN9LCJQcm9wOTciOnsiZW5hYmxlZCI6dHJ1ZSwibWFuZGF0b3J5Ijp0cnVlLCJvcmRlciI6MTB9LCJQcm9wMTEyIjp7ImVuYWJsZWQiOnRydWUsIm1hbmRhdG9yeSI6ZmFsc2UsIm9yZGVyIjo2fSwiUHJvcDExMyI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOmZhbHNlLCJvcmRlciI6N30sIlJlc3VtZSI6eyJlbmFibGVkIjp0cnVlLCJtYW5kYXRvcnkiOnRydWUsIm9yZGVyIjo1fX0=;'
    # payloadData = ''
    for name, data in field_data.items():
      if data and (name != 'Prop299' and name != 'Prop300'):
        payloadData += name + ':' + data + ';'

    ws = Webservices()
    # ws.postReq()
    return (render_template('core/posted.html', req=ws.postReq(payloadData)))






@mod.route('/getfields')
def getfields():
  # repository = Repository()
  # return (render_template('core/index.html', resources=repository.getResources()))

    ws = Webservices()
    return jsonify(ws.getReqForm())
    # return jsonify(ws.getPropTable())