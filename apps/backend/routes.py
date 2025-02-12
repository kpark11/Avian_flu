# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:25:23 2025

@author: Kiman Park, Ph.D.
"""
from apps.backend import blueprint
from flask import make_response
from flask_login import login_required
from apps.backend.models import Avian_flu
import pandas as pd
import os, json

@blueprint.route('/map_data', methods=['GET'])
@login_required
def map_data():
    try: 
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "../static/assets/data", "counties-fips.json")
        data = make_response(json.load(open(json_url)), 200)
        return data
    except Exception as e:
        print('The map data does not exist')
        return e

@blueprint.route('/us_data', methods=['GET'])
@login_required
def us_data():
    try: 
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "../static/assets/data", "us-states.json")
        data = make_response(json.load(open(json_url)), 200)
        return data
    except Exception as e:
        print('The map data does not exist')
        return e

@blueprint.route('/all_avianflu_data', methods=['GET'])
@login_required
def all_avianflu_data():
    try: 
        table = Avian_flu.query.all()
        table_list = [t.json() for t in table]
        df = pd.DataFrame(table_list)
        df['Outbreak Date'] = pd.to_datetime(df['Outbreak Date'])
        df = df.sort_values(by='Outbreak Date', ascending=False)
        df['Year'] = df['Outbreak Date'].dt.year
        df['Month'] = df['Outbreak Date'].dt.month
        df['Day'] = df['Outbreak Date'].dt.day
        return make_response(df.to_json(orient="records"), 200)
    except Exception as e:
        print('The avian flu data does not exist')
        return e
    
@blueprint.route('/state_code', methods=['GET'])
@login_required
def state_code():
    try: 
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "../static/assets/data", "states-array.json")
        data = make_response(json.load(open(json_url)), 200)
        return data
    except Exception as e:
        print('The map data does not exist')
        return e

@blueprint.route('/map_avianflu_data', methods=['GET'])
@login_required
def map_avianflu_data():
    try: 
        table = Avian_flu.query.all()
        table_list = [t.json() for t in table]
        df = pd.DataFrame(table_list)
        df = df[['State','County','Flock size', 'Flock type']].groupby(['County','State']).agg(list).reset_index()
        df['Flock size'] = df['Flock size'].apply(lambda x: sum(x))
        df['Occurrence'] = df['Flock type'].apply(lambda x: len(x))
        return make_response(df.to_json(orient="records"), 200)
    except Exception as e:
        print('The avian flu data does not exist')
        return e
    
@blueprint.route('/state_num', methods=['GET'])
@login_required
def state_num():
    try: 
        table = Avian_flu.query.all()
        table_list = [t.json() for t in table]
        df = pd.DataFrame(table_list)
        df = df[['State','County','Flock size', 'Flock type']].groupby(['State']).agg(list).reset_index()
        df['Flock size'] = df['Flock size'].apply(lambda x: sum(x))
        df['Occurrence'] = df['Flock type'].apply(lambda x: len(x))
        return make_response(df.to_json(orient="records"), 200)
    except Exception as e:
        print('The avian flu data does not exist')
        return e
    
@blueprint.route('/time_num', methods=['GET'])
@login_required
def time_num():
    try: 
        table = Avian_flu.query.all()
        table_list = [t.json() for t in table]
        df = pd.DataFrame(table_list)
        df['Outbreak Date'] = pd.to_datetime(df['Outbreak Date'])
        df = df[['State','County','Flock size', 'Flock type', 'Outbreak Date']].groupby(['Outbreak Date']).agg(list).reset_index().sort_values(by='Outbreak Date')
        df['Year'] = df['Outbreak Date'].dt.year
        df['Month'] = df['Outbreak Date'].dt.month
        df['Day'] = df['Outbreak Date'].dt.day
        df['Flock size'] = df['Flock size'].apply(lambda x: sum(x))
        df['Occurrence'] = df['Flock type'].apply(lambda x: len(x))
        return make_response(df.to_json(orient="records"), 200)
    except Exception as e:
        print('The avian flu data does not exist')
        return e
    
@blueprint.route('/download', methods=['GET'])
@login_required
def download():
    try: 
        table = Avian_flu.query.all()
        table_list = [t.json() for t in table]
        df = pd.DataFrame(table_list)
        df = df[['State','County','Flock size', 'Flock type']].groupby(['County','State']).agg(list).reset_index()
        df['Flock size'] = df['Flock size'].apply(lambda x: sum(x))
        df['Occurrence'] = df['Flock type'].apply(lambda x: len(x))
        return make_response(df.to_json(orient="records"), 200)
    except Exception as e:
        print('The avian flu data does not exist')
        return e