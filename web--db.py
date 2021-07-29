import time

from flask import Flask, render_template, request
import pymysql.cursors

app = Flask(__name__)

@app.route("/")
def hello():
    data = model('select * from child')

    return render_template('tempmap.html', data=data)

@app.route("/add")
def add():
    return render_template('add.html')
@app.route('/insert',methods=['POST'])
def insert():
    data = request.form.to_dict()

    data['date'] = time.strftime('%Y-%m-%d %H:%I:%S')
    sql = 'insert into childs value(null ,"{data["Name"]}","{data["status"]}","{data["date"]}")'
    res = model(sql)

    if res:
        return '<script>alert("success");location.href="/"<script>'
    else :
        return '<script>alert("fail");location.href="/add/"<script>'


    return '接收成功'
def model(sql):
    # Connect to the database
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         database='wsb',
                         cursorclass=pymysql.cursors.DictCursor)
    try:
        cursor = db.cursor()

        # sql = 'select version()'

        row = cursor.execute(sql)
        db.commit()

        data = cursor.fetchall()

        if data:
            return data
        else:
            return row
    except:
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    app.run(debug = False,host='127.0.0.2',port='8080')