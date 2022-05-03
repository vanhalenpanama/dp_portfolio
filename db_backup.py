import pymysql
from sqlalchemy import create_engine
import pandas as pd

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()

# {} 안에 해당하는 정보 넣기. {}는 지우기.
engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/encore_db", encoding='utf-8')
conn = engine.connect()

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



# MySQL에 저장하기
# 변수명은 이전에 만든 데이터프레임 변수명
# name은 생성할 테이블명
# index=False, 인덱스 제외

processed_data2.to_sql(name='processed_data2', con=engine, if_exists='replace', index=True)

conn.close()