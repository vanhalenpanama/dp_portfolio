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

db = SQLAlchemy()

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='oracle',
                       db='encore_db',
                       charset='utf8')
pymysql.install_as_MySQLdb()
engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/encore_db", encoding='utf-8')
con = engine.connect()
processed_data2 = pd.read_sql_table('processed_data2', con)
leng = len(processed_data2)


factory = sessionmaker(bind=engine)
session = factory()
connection = engine.connect()
metadata = db.MetaData()
table = db.Table('processed_data2', metadata, autoload=True, autoload_with=engine)
query = db.select([table])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)

#############
# sql = 'select * from processed_data2'
# result = conn.cursor().execute(sql)
# print(result.fetchall())
#
# print(result)
# for instance in session.query(processed_data2).filter_by(Opponent="Sampdoria"):
#     print("indexes: ", instance.indexes)
#     # print("result: ", instance.result)
#     print("---------")