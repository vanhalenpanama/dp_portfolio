import pymysql
from dp_test.match.vo import backup_table

class MatchDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='oracle', db='encore_db', charset='utf8')

    def disconn(self):
        self.conn.close()

    def select(self):
        try:
            self.connect()#db연결
            cursor=self.conn.cursor() # 사용할 커서 객체 생성
            sql = 'select * from processed_data2'

            cursor.execute(sql,) #sql 실행
            row = cursor.fetchone() # fetchone() : 현재 커서 위치의 한 줄 추출
            if row:
                return backup_table(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])

        except Exception as e:
            msg = e
        finally:
            self.disconn()

    def selectidx(self, idx:int):
        try:
            self.connect()#db연결
            cursor=self.conn.cursor() # 사용할 커서 객체 생성
            sql = 'select * from processed_data2 where idx=%s'
            d=(idx,)
            cursor.execute(sql, d) #sql 실행
            row = cursor.fetchone() # fetchone() : 현재 커서 위치의 한 줄 추출
            if row:
                return backup_table(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])

        except Exception as e:
            msg = e
        finally:
            self.disconn()