#!/usr/bin/env python3
import os
import sqlite3
import sys


conn = sqlite3.connect('bibel.sql')
c = conn.cursor()
c.execute('SELECT * FROM telegram_users')
all_rows_user = c.fetchall()
number_users=len(all_rows_user)
for i in range(number_users):
    user_row = all_rows_user[i]
    user_number = user_row[0]
    user_name = user_row[1]
    user_call_number = user_row[2]
    user_status = user_row[3]
    user_status_new = user_status-1
    user_status_new_str=str(user_status_new)
    user_number_str=str(user_number)
    build_sql = "UPDATE telegram_users SET status="+user_status_new_str+" WHERE rowid="+user_number_str
    print("build_sql: ", build_sql)
    c.execute(build_sql)
    conn.commit()
conn.close()
