from flask import Flask, make_response, request
from mysql.connector import Error
import mysql.connector
import pdb
import socket
from flask import Flask, render_template, flash, request,json, jsonify
import boto3, requests
from flask_restful import Api, Resource
from flask_cors import CORS
from botocore.client import Config
import logging
from botocore.exceptions import ClientError
import os
from flask_cors import CORS, cross_origin
import os, time
import datetime
from collections import Counter
import os.path
from flask import send_file
from pandas import DataFrame
import logging
import glob
from collections import Counter
import collections
import operator
from operator import itemgetter
import pandas
from collections import OrderedDict
from flask_bootstrap import Bootstrap
import sys



app = Flask(__name__)
ma = Marshmallow(app)
app.config.from_object(__name__)

CORS(app)
CORS(app, methods='POST')  
CORS(app, resources={r"/*": {"origins": "*","methods" : ['GET','POST','OPTIONS'] }})    
Bootstrap(app)


@app.route('/', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True,origin='*', methods = ['GET','POST','OPTIONS'])
@cross_origin(headers=['Content-Type'])
def index():
    return (‘hello') 



#what's the average number of fields across all the .csv files?
@app.route('/csv_quest1')
def csv_quest1():
    path = 'venv/csv_assessment'
    files = []
    num_cols=[]
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file)) 
    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        num_cols.append(len(df.columns))
    average_columns= sum(num_cols)/len(num_cols)
    return ' %f' % average_columns

         
#what's the total number or rows for the all the .csv files?
@app.route('/csv_quest2')
def csv_quest2():
    path = 'venv/csv_assessment'
    files = []
    num_rows=[]
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file)) 
    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        num_rows.append(df.shape[0] + 1)
    print(num_rows)
    total_rows= sum(num_rows)
    return ' %f' % total_rows
    
    
#what's the total number or rows for the all the .csv files?
@app.route('/csv_quest3')
def csv_quest3():
    path = 'venv/csv_assessment'
    files = []
    num_rows=[]
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file)) 
    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        num_rows.append(df.shape[0] + 1)
    print(num_rows)
    total_rows= sum(num_rows)
    return ' %f' % total_rows

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    host = os.environ.get("IP", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))
    app.run(host=host, port=port)
    app.debug = True

