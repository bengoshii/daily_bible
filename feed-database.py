#!/usr/bin/env python3
# Das Programm ist nur für die interne Verwendung. Daher werden
# unsinnige oder gefährliche Eingaben des Benutzers nicht
# abgefangen.
import sqlite3
import os
import sys
import re
#import pickle
file_number = input("Welche Dateinummer soll eingelesen werden? ")
title = input("Wie ist der Titel: ")
quotation = input("Fundstelle: ")
annotations = input("Anmerkungen - falls keine 0: ")
try:
    conn = sqlite3.connect('bibel.sql')
    c = conn.cursor()
    c.execute('SELECT * FROM text')
except:
    print("Fehler beim Aufbau der Datenbankverbindung")
all_rows_text = c.fetchall()
number_text = len(all_rows_text)
for i in range(number_text):
    text_row = all_rows_text[i]
    text_number = text_row[0]
# text_number is the last number of the bible-texts
file_name = file_number + '.txt'
title = '*' + title + '*'
quotation = '_' + quotation + '_'
try:
    text_bible = open(file_name).read()
except:
    print("Datei nicht vorhanden oder Dateiname falsch. Verwendeter Dateiname ist: ", file_name)
text_bible = re.sub(r'[0-9]', "", text_bible)
text_bible = text_bible.replace("  "," ")
text_bible = title + '\n' + text_bible + '\n' + quotation + '\n' + annotations
new_text_number = str(text_number + 1)
c.execute("INSERT INTO text VALUES (?, ?)", (new_text_number, text_bible))
conn.commit()
conn.close()
#text_bible.close()
