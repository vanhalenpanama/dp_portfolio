
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, session, Blueprint
from dp_test.match.vo import Scheme
import pandas as pd
# from web_hello.bus_info.vo import Bus, Station
# from web_hello.bus_info.dao import Dao

app = Flask(__name__)  #웹 어플리케이션

app.secret_key = 'asfaf' #세션 사용시 시크릿 키 설정
url3="https://fixturedownload.com/results/epl-2016/man-utd"


class Service:
    def __init__(self):

        self.dao = Scheme()
bp = Blueprint('match', __name__, url_prefix='/match')


@bp.route('/chart')
def chart():
    url3 = "https://fixturedownload.com/results/epl-2016/man-utd"
    df = pd.read_html(url3)[0]
    chart = df.to_html()

    return render_template('/match/chart.html', df=df)


   # html = requests.get(url3).text  # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
    # root = BeautifulSoup(html, 'lxml-xml')  # 파서 객체 생성
    # headerCd = root.find('headerCd').text
    # if headerCd != '0':
    #     msg = root.find('headerMsg').text
    #     print(msg)
    #     return

    # stationList = root.find_all('table')  # 태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
    # res = []
    # for station in stationList:
    #     Round_Number = station.find('Round_Number').text
    #     Date = station.find('Date').text
    #     Location= station.find('Location').text
    #     Home_Team = station.find('Home_Team').text
    #     Away_Team = station.find('Away_Team').text
    #     Result = station.find('Result').text
    #     res.append(Scheme(Round_Number=Round_Number,	Date=Date,	Location=Location,	Home_Team=Home_Team,Away_Team=	Away_Team,Result=	Result))