import smtplib
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')


conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT msg, RecordID FROM Motivational ORDER BY RANDOM() LIMIT 1;')
info2 = cur2.fetchone()

#msg
j = info2[0]
#recordID
k = info2[1]

connx = sqlite3.connect('StriveDB2.db')
cursorx = connx.cursor()
curx = cursorx.execute("INSERT INTO RIDX VALUES (?)", (k,))
connx.commit()
cursorx.close()
connx.close()

print(j)
print(k)
#print repr(info2[1])

