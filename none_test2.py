import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, session, Blueprint
import pandas as pd
import numpy
try:
    inter_url1="https://fbref.com/en/squads/d609edc0/2008-2009/Internazionale-Stats"
    inter_url2="https://fbref.com/en/squads/d609edc0/2009-2010/Internazionale-Stats"
    roma_url1 = "https://sfbref.com/en/squads/cf74a709/Roma-Stats"

    inter_data1 = pd.read_html(inter_url1)[1]
    inter_data2 = pd.read_html(inter_url2)[1]
    roma_data1 = pd.read_html(roma_url1)[1]

except Exception as e:
    # print(e)
    roma_data1 = pd.DataFrame(index=range(0,0), columns=['A'])
finally:
    print(len(roma_data1))

    roma_data1 = pd.read_html("https://fbref.com/en/squads/cf74a709/Roma-Stats")[1]

    print(len(roma_data1))
# roma_data2 = pd.DataFrame(index=range(0,0), columns=['A'])
#
# print("len:" + str(len(roma_data2)))
