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



@mod.route('/post')
def post():
    ws = Webservices()
    # ws.postReq()
    return (render_template('core/index.html', req=ws.postReq()))






@mod.route('/getfields')
def getfields():
  # repository = Repository()
  # return (render_template('core/index.html', resources=repository.getResources()))

    ws = Webservices()
    return jsonify(ws.getReqForm())
    # return jsonify(ws.getPropTable())