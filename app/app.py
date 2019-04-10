from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify, Markup
import logging as logger
import json
from MyAPI import APIClass
from functools import wraps
import urllib3 as URL


logger.basicConfig(level="DEBUG")
app = Flask(__name__)


# Api redirect to UI (2 text boxes side by side)
# text box showing "type request here:"
# sub button
# display response in text box
@app.route('/api/', defaults={'path': ''})
@app.route('/api/<path:path>')
def API_func(path, methods=['GET','POST']):
    # http = URL.PoolManager()
    # r = http.request('GET', path)
    API = APIClass(Request=request.url) # API parser class call
    Status = 200
    return render_template('API.html',Status=Status)
    # return jsonify(API.__dict__)


# Home
@app.route('/')
def hello_world():
    return render_template('index.html')


# Info
@app.route('/info')
def show_info():
    return render_template('info.html')


# About
@app.route('/about')
def show_about():
    return render_template('about.html')


# 404 Error Handling
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    logger.debug("Starting Flask Server")
    # from api import *
    app.run(host="0.0.0.0",port=5000,debug=True)

"""
change redirect for API
added homepage

"""
