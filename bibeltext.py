import os
import sqlite3
import sys
from time import *

#number="491706363320-1483136405"

conn = sqlite3.connect('bibel.sql')
c = conn.cursor()
"""
c.execute('SELECT * FROM control')
all_rows_control = c.fetchall()
row_control = all_rows_control[0]
control_date = row_control[0]
control_sent = row_control[1]
lt = localtime()
year, month, day = lt[0:3]
print("lt: ", lt)
print("Datum: ", year,"-",month,"-",day)
print("control_date: ", control_date)
print("control_sent: ", control_sent)
"""

c.execute('SELECT * FROM users')
all_rows_user = c.fetchall()
number_users=len(all_rows_user)
for i in range(number_users):
    user_row = all_rows_user[i]
    user_number = user_row[0]
    user_name = user_row[1]
    user_call_number = user_row[2]
    user_status = user_row[3]
    user_status_new = user_status+1
    c.execute('SELECT * FROM text')
    all_rows_text = c.fetchall()
    text_row = all_rows_text[user_status]
    bible_number = text_row[0]
    bible_text = text_row[1]
    user_call_number_str=str(user_call_number)
    os.system('python yowsup-cli demos --config config-bengoshi -M --send ' + user_call_number_str + ' ' + '"' + bible_text + '"')
    user_status_new_str=str(user_status_new)
    user_number_str=str(user_number)
    build_sql = "UPDATE users SET status="+user_status_new_str+" WHERE rowid="+user_number_str
    print("build_sql: ", build_sql)
    c.execute(build_sql)
    conn.commit()
conn.close()
