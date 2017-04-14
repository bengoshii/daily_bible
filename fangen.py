#!/usr/bin/python3
import telepot
import time
import os
import sys
import sqlite3
# If you use the database first, you have to insert the first use manual.
path = '/home/bengoshi/bibelbot'
database = 'bibel.sql'
database_p = path + '/' + database
bot = telepot.Bot('328839872:AAGEyntpNshEeGp9kr-w73_431gDCkIgk9w')
kai = '317818350'

def message_send(recipient, text):
    try:
       bot.sendMessage(recipient, text)
    except:
       print("Da hat was mit dem Senden nicht geklappt.")
       print("recipient: ", recipient)
       print("text: ", text)

def handle(msg):
    print(msg)
    global kai
    content_type, chat_type, chat_id = telepot.glance(msg)
    user_text = msg['text']
    #foo[0]['message']['chat']['id']
    #chat_id = msg['from']['id']
    user_id = msg['from']['id']
    user_name = msg['chat']['first_name']
    signal = 'bitte_eintragen'
#    subscribe(users_text, user_id, user_name, signal)
#def subscribe(user_text, user_id, user_name, signal):
    if signal in user_text:
        double_test = 0
        conn = sqlite3.connect(database_p)
        c = conn.cursor()
        c.execute('SELECT * FROM telegram_users')
        all_rows_users = c.fetchall()
        user_number = len(all_rows_users)
        double_test = 0
        message_send(user_id, "Ich teste kurz, ob Du schon eingetragen bist...")
        for i in range(user_number):
            user_row = all_rows_users[i]
            user_number_db = user_row[0]
            user_name_db = user_row[1]
            user_id_db = user_row[2]
            if user_id_db == user_id:
                message_send(user_id, 'Du bist bereits eingetragen. Aber danke für Dein Interesse.')
                double_test = 1
                break
        if double_test == 0:
            user_id_str = str(user_id)
            user_number = user_number + 1
            try:
                status = 1
                user_number_str = str(user_number)
                user_name_str = str(user_name)
                status_str = str(status)
                user_id_str = str(user_id)
                build_sql = "INSERT INTO `telegram_users`(`user_number`,`user_name`,`user_id`,`status`) VALUES(" + user_number_str + ", \"" + user_name_str + "\", " + user_id_str + ", " + status_str + ")"
                message_send(user_id, 'Du bist jetzt eingetragen. Vielen Dank für Dein Interesse.\n Wenn Du in die Gruppe Bibelbot möchtest, klicke bitte auf den Link: https://t.me/joinchat/AAAAAAtpe497jEzDTaNS0w\n Warum solltest Du in die Gruppe gehen? Weil es eine Möglichkeit bietet, sich mit anderen Lesern des Bibelbots auszutauschen. Das Lesen der Bibel und der Austausch darüber stehen in einer Einheit. Und vielleicht hast Du aucheinfach mal eine Frage oder bist interessiert an den Fragen und Antworten anderer. Du kannst also möglichen Diskussionen auch einfach nur „Lauschen“.\n Wenn Du vorher bei WhatsApp dabei warst, kann es ein bis zwei Tage dauern, bis Du an der Stelle fortsetzt, an der Du vorher aufgehört hast. Es kann also sein, dass Du erstmal wieder die ersten Texte bekommen.\n Roadmap:\n 1. Möglichkeit zum Abmelden schaffen \n 2. Möglichkeit schaffen, um selber mit einem beliebigen Text loszulegen (ggf. für Fortsetzungen)\n \n Wenn Dir weitere Funktionen einfallen, die Du vermisst, schreib es Kai (+170-6363320)')
                c.execute(build_sql)
                conn.commit()
                kai_text = 'user_number: ' + user_number_str + ', user_name: ' + user_name_str + ', status: ' + status_str + ', user_id' + user_id_str 
                print(kai_text)
                message_send(kai, kai_text)
                """
                while 1:
                    #response = bot.getUpdates()
                    bot.message_loop(msg)
                    content_type_inner, chat_type_inner, chat_id_inner = telepot.glance(msg)
                    user_name_inner = msg['chat']['first_name']
                    user_id_inner = msg['from']['id']
                    if user_id_inner!=user_id:
                        message_send(user_id_inner, "Hallo ", user_name_inner, "!\nDer Bot ist gerade mit der Eintragung eines anderen Benutzers beschäftigt. Könntest Du Dich bitte nochmal in circa drei Minuten versuchen anzumelden? Vielen Dank!")
                    user_text_inner = msg['text']
                    try:
                        user_text_inner = int(user_text_inner)
                        user_text_inner = str(user_text_inner)
                        build_sql = "UPDATE telegram_users SET status="+user_text_inner+" WHERE rowid="+user_number_str
                        c.execute(build_sql)
                        conn.commit()
                    except:
                        message_send(user_id, "Du kannst nur eine Zahl eintragen. Wenn Du nicht vorher bei WhatsApp warst, bitte einfach warten und nichts machen.")
                    """
            except ValueError:
                message_send(user_id, 'Da hat was nicht geklappt (ValueError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')
            except RuntimeError:
                message_send(user_id, 'Da hat was nicht geklappt (RuntimeError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')
            except TypeError:
                message_send(user_id, 'Da hat was nicht geklappt (TypeError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')
            except NameError:
                message_send(user_id, 'Da hat was nicht geklappt (NameError). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320.')
            except:
                error_code = sys.exc_info()[0]
                error_code = str(error_code)
                message = 'Da hat was nicht geklappt (Unexpected). Bitte probiere es noch einmal. Wenn es irgendwie gar nicht klappen will, wende Dich an Kai - +491706363320. Fehlercode: ' + error_code
                message_send(user_id, message)
    else:
        message_send(user_id, "Ich bin ein Bot und denke nicht weiter als ein Brot. Ich kann Dir also nicht wirklich antworten. Wenn Du Antworten wünschst, wende Dich bitte an Kai. Dieser Bot kann Dich nur in die Liste aufnehmen. Dafür musst Du bitte_eintragen posten. Genau so, mit Unterstrich und klein geschrieben.\n Falls was nicht klappt oder Du Hilfe brauchst, zögere nicht, Kai anzuchreiben.")

bot.message_loop(handle)
while 1:
    time.sleep(1)

"""
from pprint import pprint
while 1:
    response = bot.getUpdates()
    pprint(response)
    time.sleep(10)
"""
