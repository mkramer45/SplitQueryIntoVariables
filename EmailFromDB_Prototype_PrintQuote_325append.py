import smtplib
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')


conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT RecordID, Msg FROM Motivational ORDER BY RANDOM() LIMIT 1;')
info2 = cur2.fetchall()

print(info2)

# this will print the following:
# [(77, u' The reason most people never reach their goals is that they don\u2019t define them ...')]
# I would like each of the values from this list stored in their own variables ... so we need to separate by commas
# ie: assign '77' to a python object variable named RID & the text string assigned to one named msg1
	# RID = 77
	# MSG1 = 'The reason most people never reach their ....'


