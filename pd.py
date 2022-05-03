import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, session, Blueprint

key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'
url3="https://fixturedownload.com/results/epl-2016/man-utd"
df = pd.read_html(url3)[0]

chart = df.to_html()


# print(type(charttest))
# print(charttest)

print(chart)