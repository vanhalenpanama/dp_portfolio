import pymysql
import pandas as pd
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()


engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/encore_db", encoding='utf-8')
conn = engine.connect()

processed_data2 = pd.read_sql_table('processed_data2', conn)

# print(pd.read_sql_query('select * from processed_data2', conn))


print("len:"+str(len(processed_data2)))
# print(type(processed_data2))
#
# print(processed_data2)