import sqlite3
from sqlalchemy import create_engine
import pandas as pd
# MySQL Connector using pymysql
con = sqlite3.connect("D:\pythonProject\processed_data2.db")

# processed_data2 = pd.read_sql_table('processed_data2', con)
processed_data2 = pd.read_sql_query('select * from processed_data2', con)

w_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='W')
l_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='L')
d_condition = (processed_data2.Opponent == 'Fiorentina') &(processed_data2.Result != 'No') &(processed_data2['Result']=='D')
wins =processed_data2[w_condition].shape[0]
lose =processed_data2[l_condition].shape[0]
draw =processed_data2[d_condition].shape[0]

print(wins, lose, draw)

print(type(wins))

con.close()