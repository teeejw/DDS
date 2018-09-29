import sqlite3
from datetime import datetime

conn = sqlite3.connect('test.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS alerts(
			ranger text,
			age datetime, # used datetime for uniquness
			classification text,
			coords text)''')

ranger = input('Enter your full name: ')
# TODO: restrict classification values to POSITIVE, FALSE
classification = input('Enter the alert classification: (POSITIVE/FALSE')
# coords = input('Enter the GPS coordinates')
coords = '32.76839451804323, -117.08301007747652'
date = datetime.now()

insert_value = (ranger, date, classification, coords)

c.execute('''INSERT INTO alerts VALUES(?,?,?,?)''', insert_value) 

conn.commit()
c.close()