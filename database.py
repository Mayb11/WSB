import pymysql.cursors

# Connect to the database
db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='mysql',
                     cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = db.cursor()

    sql = 'select version()'

    cursor.execute(sql)

    data = cursor.fetchall()
finally:
    db.close()

print(data)
