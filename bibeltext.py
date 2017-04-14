#!/usr/bin/env python3
import telepot
import time
import os
import sys
import sqlite3
path = '/home/bengoshi/bibelbot'
database = 'bibel.sql'
database_p = path + '/' + database
bot = telepot.Bot('328839872:AAGEyntpNshEeGp9kr-w73_431gDCkIgk9w')
kai = '317818350'

def message_send(recipient, text):
    try:
        #print("recipient: ", recipient)
        bot.sendMessage(recipient, text, parse_mode='Markdown')
    except ValueError:                                                                                           
        message_send(kai, 'Da hat was nicht geklappt (ValueError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')                                                      
    except RuntimeError:                                                                                         
        message_send(kai, 'Da hat was nicht geklappt (RuntimeError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')                                                    
    except TypeError:                                                                                            
        message_send(kai, 'Da hat was nicht geklappt (TypeError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')                                                       
    except NameError:                                                                                            
        message_send(kai, 'Da hat was nicht geklappt (NameError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')
    except:
        error_code = sys.exc_info()[0]
        error_code = str(error_code)
        message = 'Da hat was nicht geklappt (Unexpected). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320. Fehlercode: ' + error_code
        message_send(kai, message)

# connection to database
print(database_p)
conn = sqlite3.connect(database_p)
c = conn.cursor()
c.execute('SELECT * FROM telegram_users')
all_rows_user = c.fetchall()
user_number=len(all_rows_user)
for i in range(user_number):
    if user_number > 30:
        time.sleep(30)
    user_row = all_rows_user[i]
    user_number = user_row[0]
    user_name = user_row[1]
    user_id = user_row[2]
    user_status = user_row[3]
    user_status_new = user_status+1
    c.execute('SELECT * FROM text')
    all_rows_text = c.fetchall()
    text_row = all_rows_text[user_status]
    bible_number = text_row[0]
    bible_text = text_row[1]
    user_id=str(user_id)
    length_bible_text = len(bible_text)
    if length_bible_text > 4000:
        text_neu = bible_text.split("\n")
        number_of_paragraphs = len(text_neu)
        time.sleep(30)
        for i in range(number_of_paragraphs):
            if i == 15:
                time.sleep(60)
            elif i == 30:
                time.sleep(60)
            elif i == 60:
                time.sleep(60)
            current_text = text_neu[i]
            if current_text != '':
                message_send(user_id, current_text)
    else:
        message_send(user_id, bible_text)
    user_status_new_str=str(user_status_new)
    user_number_str=str(user_number)
    build_sql = "UPDATE telegram_users SET status="+user_status_new_str+" WHERE rowid="+user_number_str
    #print("build_sql: ", build_sql)
    c.execute(build_sql)
    conn.commit()
conn.close()
