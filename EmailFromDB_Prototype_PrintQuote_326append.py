import smtplib
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')


conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT msg, RecordID FROM Motivational ORDER BY RANDOM() LIMIT 1;')
info2 = cur2.fetchone()

y = [x[0].encode("utf-8") for x in info2]


# this prints our recordID
print(info2)[1]
print str(y)[1:-1]



# line 18 and 13 are integrated from 'TextStringFromDBError_Punctuation' repository
# the code in the mentioned repository allows us to print the text
# however, when attempting to use it in this script, we get the error seen below:
	# TypeError: 'int' object has no attribute '__getitem__'


