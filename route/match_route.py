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

# from web_hello.bus_info.vo import Bus, Station
# from web_hello.bus_info.dao import Dao

app = Flask(__name__)  #웹 어플리케이션

app.secret_key = 'asfaf' #세션 사용시 시크릿 키 설정
url3="https://fixturedownload.com/results/epl-2016/man-utd"

team_name = pd.DataFrame({'구단명':['삼프도리아','카타니아','토리노','US 레체','AC 밀란','볼로냐 1909','제노아 CFC','피오렌티나','레지나 1914','우디네세','US 팔레르모','유벤투스','나폴리','라치오','키에보','AC 시에나','칼리아리','아탈란타','AS 바리','파르마','리보르노','살레르니티나','사수올로','엘라스 베로나','엠폴리','베네치아','인테르 밀란','스페치아'],
'검색코드':['Sampdoria','Catania','Torino','Lecce','Milan','Bologna','Genoa','Fiorentina','Reggina','Udinese','Palermo','Juventus','Napoli','Lazio','Chievo','Siena','Cagliari','Atalanta','Bari','Parma','Livorno','Salernitana','Sassuolo','Hellas Verona','Empoli','Venezia','Inter','Spezia']})
# class Service:
#     def __init__(self):
#
#         self.dao = Scheme()
# bp = Blueprint('match', __name__, url_prefix='/match')

bp = Blueprint('match', __name__,  url_prefix='/')

try:
    #분석 데이터
    inter_url1="https://fbref.com/en/squads/d609edc0/2008-2009/Internazionale-Stats"
    inter_url2="https://fbref.com/en/squads/d609edc0/2009-2010/Internazionale-Stats"
    roma_url1 = "https://fbref.com/en/squads/cf74a709/Roma-Stats"

    inter_data1 = pd.read_html(inter_url1)[1]
    inter_data2 = pd.read_html(inter_url2)[1]
    roma_data1 = pd.read_html(roma_url1)[1]

    if (len(inter_data1)<5 or len(inter_data1)>55) or (len(inter_data2)<5 or len(inter_data2)>55):
        pymysql.install_as_MySQLdb()
        engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
        conn = engine.connect()
        processed_data2 = pd.read_sql_table('processed_data2', conn)
        conn.close()
    else:
        #데이터 결합
        merge_data = pd.concat([inter_data1,inter_data2,roma_data1], ignore_index=True)
        #필요없는 컬럼 삭제
        processed_data1 = merge_data.drop(['Poss', 'Attendance', 'Captain', 'Formation', 'Referee','Match Report', 'Notes', 'xG', 'xGA'],axis=1)
        #nan값 'No'로 변경
        processed_data2 =processed_data1.fillna('#$%')
except Exception as e:
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
    conn = engine.connect()
    processed_data2 = pd.read_sql_table('processed_data2', conn)
    conn.close()
    # processed_data1[processed_data1['Opponent'] == 'Fiorentina'].size()
    # print(processed_data1[processed_data1['Opponent'] == 'Fiorentina'].size())



@bp.route('chart')
def chart():
    url3 = "https://fixturedownload.com/results/epl-2016/man-utd"
    df = pd.read_html(url3)[0]
    data = df.to_html()

    # return render_template('/match/chart.html', df=df,data=data,tables=df.to_html(),titles = df.columns.values)
    return render_template('/match/chart.html', df=df,data=data)

@bp.route('manutd')
def manu_chart():
    man_url2016 = "https://fixturedownload.com/results/epl-2016/man-utd"
    man_url2017 = "https://fixturedownload.com/results/epl-2017/man-utd"
    man_url2018 = "https://fixturedownload.com/results/epl-2018/man-utd"
    # df = pd.read_html(url3)[0]
    # data = df.to_html()
    man_data2016 = pd.read_html(man_url2016)[0].to_html()
    man_data2017 = pd.read_html(man_url2017)[0].to_html()
    man_data2018 = pd.read_html(man_url2018)[0].to_html()

    # return render_template('/match/chart.html', df=df,data=data,tables=df.to_html(),titles = df.columns.values)
    return render_template('/match/manutd.html', man_data2016=man_data2016,man_data2017=man_data2017,man_data2018=man_data2018)


@bp.route('porto')
def porto_chart():
    porto_url2002 = "https://fbref.com/en/squads/5e876ee6/2002-2003/Porto-Stats"
    porto_url2003 = "https://fbref.com/en/squads/5e876ee6/2003-2004/Porto-Stats"

    porto_data2002 = pd.read_html(porto_url2002)[1].to_html()
    porto_data2003 = pd.read_html(porto_url2003)[1].to_html()

    return render_template('/match/porto.html', porto_data2002=porto_data2002,porto_data2003=porto_data2003)

@bp.route('chelsea1')
def chelsea1_chart():
    chelsea1_url2004 = "http://stats.football.co.uk/results_fixtures/2004_2005/chelsea/index.shtml"
    chelsea1_url2005 = "http://stats.football.co.uk/results_fixtures/2005_2006/chelsea/index.shtml"
    chelsea1_url2006 = "http://stats.football.co.uk/results_fixtures/2006_2007/chelsea/index.shtml"

    chelsea1_data2004 = pd.read_html(chelsea1_url2004)[0].to_html()
    chelsea1_data2005 = pd.read_html(chelsea1_url2005)[0].to_html()
    chelsea1_data2006 = pd.read_html(chelsea1_url2006)[0].to_html()
    return render_template('/match/chelsea1.html', chelsea1_data2004=chelsea1_data2004,chelsea1_data2005=chelsea1_data2005,chelsea1_data2006=chelsea1_data2006)

@bp.route('inter')
def inter_chart():
    inter_url2008 = "https://fbref.com/en/squads/d609edc0/2008-2009/Internazionale-Stats"
    inter_url2009 = "https://fbref.com/en/squads/d609edc0/2009-2010/Internazionale-Stats"

    inter_data2008 = pd.read_html(inter_url2008)[1].to_html()
    inter_data2009 = pd.read_html(inter_url2009)[1].to_html()
    return render_template('/match/inter.html', inter_data2008=inter_data2008,inter_data2009=inter_data2009)

@bp.route('real')
def real_chart():
    real_url2010 = "https://fbref.com/en/squads/53a2f082/2010-2011/Real-Madrid-Stats"
    real_url2011 = "https://fbref.com/en/squads/53a2f082/2011-2012/Real-Madrid-Stats"
    real_url2012 = "https://fbref.com/en/squads/53a2f082/2012-2013/Real-Madrid-Stats"

    real_data2010 = pd.read_html(real_url2010)[1].to_html()
    real_data2011 = pd.read_html(real_url2011)[1].to_html()
    real_data2012 = pd.read_html(real_url2012)[1].to_html()

    return render_template('/match/real.html', real_data2010=real_data2010,real_data2011=real_data2011,real_data2012=real_data2012)

@bp.route('chelsea2')
def chelsea2_chart():
    chelsea2_url2013 = "http://stats.football.co.uk/results_fixtures/2013_2014/chelsea/index.shtml"
    chelsea2_url2014 = "http://stats.football.co.uk/results_fixtures/2014_2015/chelsea/index.shtml"
    chelsea2_url2015 = "http://stats.football.co.uk/results_fixtures/2015_2016/chelsea/index.shtml"

    chelsea2_data2013 = pd.read_html(chelsea2_url2013)[0].to_html()
    chelsea2_data2014 = pd.read_html(chelsea2_url2014)[0].to_html()
    chelsea2_data2015 = pd.read_html(chelsea2_url2015)[0].to_html()
    return render_template('/match/chelsea2.html', chelsea2_data2013=chelsea2_data2013,chelsea2_data2014=chelsea2_data2014,chelsea2_data2015=chelsea2_data2015)

@bp.route('spurs')
def spurs_chart():
    spurs_url2019 = "https://fixturedownload.com/results/epl-2019/spurs"
    spurs_url2020 = "https://fixturedownload.com/results/epl-2020/spurs"

    spurs_data2019 = pd.read_html(spurs_url2019)[0].to_html()
    spurs_data2020 = pd.read_html(spurs_url2020)[0].to_html()

    return render_template('/match/spurs.html', spurs_data2019=spurs_data2019,spurs_data2020=spurs_data2020)

@bp.route('roma')
def roma_chart():
    roma_url2021 = "https://fbref.com/en/squads/cf74a709/Roma-Stats"

    roma_data2021 = pd.read_html(roma_url2021)[1].to_html()

    return render_template('/match/roma.html', roma_data2021=roma_data2021)

# @bp.route('/businfo', methods=['POST'])  # 요청 url 등록
# def businfo():
#     busnm = request.form['busnm'] # 폼 양식의 이름이 'busnm'인 요소의 값을 읽음
#     res = bus_service.getBusinfoByNm(busnm)
#     return render_template('bus/busList.html', res=res, flag=True)

@bp.route('team_input')
def input_team():
    team_list=team_name.to_html()
    return render_template('/match/team_input.html', team_list=team_list)

@bp.route('easter_egg')
def easter_egg():
    return render_template('/match/easter_egg.html')

@bp.route('function_manual')
def function_manual():
    return render_template('/match/function_manual.html')


@bp.route('expect', methods=['POST'])
def expect():
    team = request.form['team']  # 폼 양식의 이름이 'team'인 요소의 값을 읽음
    w_condition = (processed_data2.Opponent == team) & (processed_data2.Result != '#$%') & (processed_data2['Result'] == 'W')
    l_condition = (processed_data2.Opponent == team) & (processed_data2.Result != '#$%') & (processed_data2['Result'] == 'L')
    d_condition = (processed_data2.Opponent == team) & (processed_data2.Result != '#$%') & (processed_data2['Result'] == 'D')
    wins = processed_data2[w_condition].shape[0]
    lose = processed_data2[l_condition].shape[0]
    draw = processed_data2[d_condition].shape[0]

    img_path = 'static/my_plot.png'

    fig = plt.figure(figsize=(8, 8))  ## 캔버스 생성
    fig.set_facecolor('white')  ## 캔버스 배경색을 하얀색으로 설정
    ax = fig.add_subplot()  ## 프레임 생성

    x = [wins, lose, draw]
    labels = ['win', 'lose', 'draw']
    pie = plt.pie(x,
                  startangle=90,  ## 시작점을 90도(degree)로 지정
                  counterclock=False,  ## 시계 방향으로 그린다.
                  autopct=lambda p: '{:.2f}%'.format(p)  ## 퍼센티지 출력
                  )
    plt.legend(pie[0], labels)

    fig.savefig(img_path)  # 플랏의 이미지를 파일로 저장
    img_path = '/' + img_path


    return render_template('/match/expect.html',img_path=img_path, team=team, wins=wins,lose=lose,draw=draw)

@bp.route('mysql_backup_page')
def mysql_backup_page():
    return render_template('/backup/mysql_backup_page.html')

@bp.route('mysql_backup')
def mysql_backup():
    # MySQL Connector using pymysql
    pymysql.install_as_MySQLdb()

    # {} 안에 해당하는 정보 넣기. {}는 지우기.
    # engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
    engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
    conn = engine.connect()

    inter_url1 = "https://fbref.com/en/squads/d609edc0/2008-2009/Internazionale-Stats"
    inter_url2 = "https://fbref.com/en/squads/d609edc0/2009-2010/Internazionale-Stats"
    roma_url1 = "https://fbref.com/en/squads/cf74a709/Roma-Stats"

    inter_data1 = pd.read_html(inter_url1)[1]
    inter_data2 = pd.read_html(inter_url2)[1]
    roma_data1 = pd.read_html(roma_url1)[1]
    # 데이터 결합
    merge_data = pd.concat([inter_data1, inter_data2, roma_data1], ignore_index=True)
    # 필요없는 컬럼 삭제
    processed_data1 = merge_data.drop(
        ['Poss', 'Attendance', 'Captain', 'Formation', 'Referee', 'Match Report', 'Notes', 'xG', 'xGA'], axis=1)
    # nan값 'No'로 변경
    processed_data2 = processed_data1.fillna('#$%')
    # MySQL에 저장하기
    # 변수명은 이전에 만든 데이터프레임 변수명
    # name은 생성할 테이블명
    # index=False= 인덱스 제외 , index=True= 인덱스 포함
    processed_data2['indexes'] = processed_data2.index
    processed_data2.to_sql(name='processed_data2', con=engine, if_exists='replace', index=False)
    conn.close()

    # return render_template('/match/easter_egg.html')
    return redirect('/')

@bp.route('mysql_truncate_page')
def mysql_truncate_page():
    return render_template('/backup/mysql_truncate_page.html')

@bp.route('mysql_truncate')
def mysql_truncate():
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
    conn = engine.connect()
    sql = "truncate table hellodb.processed_data2"
    engine.execute(sql)
    conn.close()

    return redirect('/')

# 수정 기능이 없는 전체데이터출력 백업
# @bp.route('mysql_data_view_all')
# def mysql_data_view_all():
#     pymysql.install_as_MySQLdb()
#     engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
#     conn = engine.connect()
#     processed_data2 = pd.read_sql_table('processed_data2', conn)
#
#     data = processed_data2.to_html()
#     leng = len(processed_data2)
#     conn.close()
#     return render_template('/backup/mysql_data_view_all.html', data=data, leng=leng)

@bp.route('mysql_data_view_all')
def mysql_data_view_all():
    conn = pymysql.connect(host='localhost',
                       user='root',
                       password='oracle',
                       db='hellodb',
                       charset='utf8')
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
    con = engine.connect()
    processed_data2 = pd.read_sql_table('processed_data2', con)
    leng = len(processed_data2)
    con.close()
    sql = 'select * from processed_data2'
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
            res = [backup_table(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])for row in result]

    return render_template('/backup/mysql_data_view_all.html', res=res, leng=leng)

def getById(self, idx:str)->backup_table:
        return self.dao.select(idx)



@bp.route("mysql_data_view/page/<int:page>")
@bp.route('mysql_data_view',defaults={"page": 1})
@bp.route('mysql_data_view')
def mysql_data_view():
    conn = pymysql.connect(host='localhost',
                       user='root',
                       password='oracle',
                       db='hellodb',
                       charset='utf8')
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
    con = engine.connect()
    processed_data2 = pd.read_sql_table('processed_data2', con)
    leng = len(processed_data2)
    con.close()
    sql = 'select * from processed_data2'
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
            res = [backup_table(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])for row in result]
#########################################################
    import sqlalchemy as db
    factory = sessionmaker(bind=engine)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table('processed_data2', metadata, autoload=True, autoload_with=engine)
    query = db.select([table])
    result_proxy = connection.execute(query)
    res2 = result_proxy.fetchall()

    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=leng, search=search, record_name='res2')
##################################################
    return render_template('/backup/mysql_data_view.html', res=res, leng=leng,
                           pagination=pagination, res2=res2, page=page
                           )


# mysql_data_view백업 20220301 pm8
# @bp.route('mysql_data_view')
# def mysql_data_view():
#     conn = pymysql.connect(host='localhost',
#                        user='root',
#                        password='oracle',
#                        db='hellodb',
#                        charset='utf8')
#     pymysql.install_as_MySQLdb()
#     engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
#     con = engine.connect()
#     processed_data2 = pd.read_sql_table('processed_data2', con)
#     leng = len(processed_data2)
#     con.close()
#     sql = 'select * from processed_data2'
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(sql)
#             result = cur.fetchall()
#             res = [backup_table(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])for row in result]
# #########################################################
#     users = res.find(...)
#     search = False
#     q = request.args.get('q')
#     if q:
#         search = True
#
#     page = request.args.get(get_page_parameter(), type=int, default=1)
#     pagination = Pagination(page=page, total=leng, search=search, record_name='res')
#
# ##################################################
#     return render_template('/backup/mysql_data_view.html', res=res, leng=leng,
#                            pagination=pagination,
#                            )

@bp.route('<string:index>')  # 요청 url 등록
def editmatch_input(index):
    conn = pymysql.connect(host='localhost',
                       user='root',
                       password='oracle',
                       db='hellodb',
                       charset='utf8')
    sql = 'select * from processed_data2 where indexes =%s'
    d = (index,)
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql,d)
            row = cur.fetchone()
            res = backup_table(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
    # row = conn.cursor().fetchone()
    # res = backup_table(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
    return render_template('backup/editmatch_form.html', res=res)

@bp.route('editmatch_form', methods=['POST'])
def editmatch_form():
    conn = pymysql.connect(host='localhost',
                       user='root',
                       password='oracle',
                       db='hellodb',
                       charset='utf8')
    index= request.form['indexes']
    # Date= request.form['Date']
    Time= request.form['Time']
    Comp= request.form['Comp']
    Round= request.form['Round']
    Day= request.form['Day']
    Venue= request.form['Venue']
    Result= request.form['Result']
    GF= request.form['GF']
    GA= request.form['GA']
    Opponent= request.form['Opponent']

    sql = 'update processed_data2 set Time=%s, Comp=%s, Round=%s, Day=%s, Venue=%s, Result=%s, GF=%s, GA=%s, Opponent=%s where indexes = %s'
    d = (Time,Comp,Round,Day,Venue,Result,GF,GA,Opponent,index)

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql,d)
            conn.commit()
    # service.editMember(Member(id=id, pwd=pwd, name=name, email=email))
    return redirect('/mysql_data_view')


