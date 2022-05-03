import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, session, Blueprint
import pandas as pd
import numpy

inter_url1="https://fbref.com/en/squads/d609edc0/2008-2009/Internazionale-Stats"
inter_url2="https://fbref.com/en/squads/d609edc0/2009-2010/Internazionale-Stats"
roma_url1 = "https://fbref.com/en/squads/cf74a709/Roma-Stats"

inter_data1 = pd.read_html(inter_url1)[1]
inter_data2 = pd.read_html(inter_url2)[1]
roma_data1 = pd.read_html(roma_url1)[1]


#데이터 결합
merge_data = pd.concat([inter_data1,inter_data2,roma_data1], ignore_index=True)

#필요없는 컬럼 삭제
processed_data1 = merge_data.drop(['Poss', 'Attendance', 'Captain', 'Formation', 'Referee','Match Report', 'Notes', 'xG', 'xGA'],axis=1)

#nan값 'No'로 변경
processed_data2 =processed_data1.fillna('No')

# processed_data1[processed_data1['Opponent'] == 'Fiorentina'].size()
# print(processed_data1[processed_data1['Opponent'] == 'Fiorentina'].size())

w_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='W')
l_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='L')
d_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='D')
wins =processed_data2[w_condition].shape[0]
lose =processed_data2[l_condition].shape[0]
draw =processed_data2[d_condition].shape[0]

print(wins, lose, draw)

# order_all[order_all["status"]!=9 ]

# processed_data2[processed_data2['Result']=='W']

# print(processed_data2[w_condition].shape[0])
# print(processed_data2[condition].pivot_table(index='Result',aggfunc='count'))


# print(merge_data.columns)
# print(processed_data1.columns)
# if processed_data1['Opponent'] == 'Fiorentina':
#         processed_data1['Opponent']



# print(processed_data1['Opponent'])



# class Test:
#     def __init__(self):
#         print('init')
#
#     def TestFunc(self, Argument):
#         # print('Type of Argument  : ', type(Argument))
#         print('Value of Argument : ', Argument)
#
#     def expect(self, opponent):
#         if processed_data1['Opponent'] == opponent:
#             return processed_data1['Opponent']
#
# from football import Test
# def main():
#     T = Test()
#     opponent = 'Fiorentina'
#     print(T.expect(opponent))
# if __name__== "__main__":
#     main()


    # print(T.expect(opponent))

# print(expect('Fiorentina'))
# app = Flask(__name__)  #웹 어플리케이션
#
# app.secret_key = 'asfaf' #세션 사용시 시크릿 키 설정
# url3="https://fixturedownload.com/results/epl-2016/man-utd"
#
# class Scheme:
#     def __init__(self, Round_Number=None, Date=None, Location=None, Home_Team=None, Away_Team=None, Result=None):
#         self.Round_Number = Round_Number
#         self.Date = Date
#         self.Location = Location
#         self.Home_Team = Home_Team
#         self.Away_Team = Away_Team
#         self.Result = Result
#
# # Round Number	Date	Location	Home Team	Away Team	Result
# @app.route('/')
# def root():
#     '''
#     로그아웃 처리
#     session.pop('flag')
#     session.pop('loginid')
#     '''
#     return render_template('index.html')
#
# if __name__=='__main__':
#     app.run()
#
# # @app.route('/stationinfo/<string:id>')  # 요청 url 등록
# # def stationinfo(id):
# #     res = bus_service.getStationInfoById(id)
# #     return render_template('bus/stationList.html', res=res)
#
# bp = Blueprint('match', __name__, url_prefix='/match')
#
# @bp.route('/chart')
# def chart():
#     html = requests.get(url3).text  # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
#     root = BeautifulSoup(html, 'lxml-xml')  # 파서 객체 생성
#     # headerCd = root.find('headerCd').text
#     # if headerCd != '0':
#     #     msg = root.find('headerMsg').text
#     #     print(msg)
#     #     return
#
#     stationList = root.find_all('table')  # 태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
#     res = []
#     for station in stationList:
#         Round_Number = station.find('Round_Number').text
#         Date = station.find('Date').text
#         Location= station.find('Location').text
#         Home_Team = station.find('Home_Team').text
#         Away_Team = station.find('Away_Team').text
#         Result = station.find('Result').text
#         res.append(Scheme(Round_Number=Round_Number,	Date=Date,	Location=Location,	Home_Team=Home_Team,Away_Team=	Away_Team,Result=	Result))
#
#     return render_template('/match/chart.html', res=res)
