import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, render_template,g, session, Blueprint, request, redirect
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_paginate import Pagination, get_page_parameter, get_page_args
import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker

from dp_test.match import vo
from dp_test.match.vo import backup_table
from dp_test.match.dao import MatchDao
import sqlite3


    #분석 데이터
inter_url1="https://fbref.com/en/squads/d609edc0/2008-2009/Internazionale-Stats"
inter_url2="https://fbref.com/en/squads/d609edc0/2009-2010/Internazionale-Stats"
roma_url1 = "https://fbref.com/en/squads/cf74a709/Roma-Stats"

inter_data1 = pd.read_html(inter_url1)[1]
inter_data2 = pd.read_html(inter_url2)[1]
roma_data1 = pd.read_html(roma_url1)[1]

if (len(inter_data1) < 5 or len(inter_data1) > 55):
    print("if:"+str(len(inter_data1)))
else:
        print("else:"+str(len(inter_data1)))
