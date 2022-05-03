import pymysql
import pandas as pd
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()


engine = create_engine("mysql+mysqldb://root:oracle@localhost:3306/hellodb", encoding='utf-8')
conn = engine.connect()

processed_data2 = pd.read_sql_table('processed_data2', conn)

w_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='W')
l_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='L')
d_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='D')
wins =processed_data2[w_condition].shape[0]
lose =processed_data2[l_condition].shape[0]
draw =processed_data2[d_condition].shape[0]

print(wins, lose, draw)

print(type(wins))

conn.close()