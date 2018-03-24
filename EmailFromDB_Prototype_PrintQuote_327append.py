import smtplib
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')


conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT msg, RecordID FROM Motivational ORDER BY RANDOM() LIMIT 1;')
info2 = cur2.fetchone()

print(info2[0])
print(info2[1])
#print repr(info2[1])

