import pymysql
from flask import jsonify
from flask import request, Flask , Response
from flaskext.mysql import MySQL
import mysql.connector
from waitress import serve
import random

app = Flask(__name__)

mysql_object = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql_object.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/signup', methods=['POST'])
def signup():
    print('in signup method')

    json = request.json
    user_name = json['user_name']
    email = json['email']
    password = json['password']
    print(user_name, email, password)

        # validate the received values
    if user_name and email and password and request.method == 'POST':
        print('in validate condition')

        con= mysql.connector.connect(user='root', password='root', host='localhost', database='flask')
        print('database connection for signup')
        cursors = con.cursor()

        print('connection done')
        sql = "INSERT INTO signup(user_name, email,password) VALUES( %s, %s,%s);"
        print(sql)
        data = (user_name, email, password)
        cursors.execute(sql, data)
        con.commit()
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        cursors.close()
        con.close()
        return resp

    else:
        return not_found()


@app.route('/add_task', methods=['POST'])
def add_task():
    print('in add method')

    token = request.headers.get('token')
    json = request.json
    _name = json['task_name']
    print(_name)

        # validate the received values
    if _name and request.method == 'POST':
        print('in if condition')

        con= mysql.connector.connect(user='root', password='root', host='localhost', database='flask')
        print('hello')

        sql = "SELECT user_id FROM token_data where token = %s;"
        print(sql)
        cursors = con.cursor()
        cursors.execute(sql, (token,))
        user_id = cursors.fetchone()
        con.commit()
        print(user_id[0])

        cursors = con.cursor()

        print('in connection mysql')
        sql = "INSERT INTO tasks(task_name, is_deleted, is_completed,user_id) VALUES(%s, %s, %s,%s);"
        print(sql)
        data = (_name, False, False, user_id[0])
        cursors.execute(sql, data)
        con.commit()
        resp = jsonify('task added successfully!')
        resp.status_code = 200
        cursors.close()
        con.close()
        return resp

    else:
        return not_found()


@app.route('/login', methods=['POST'])
def login():
    print('in login method')

    json = request.json
    email = json['email']
    password = json['password']
    print(email, password)

        # validate the received values
    if email and password and  request.method == 'POST':
        print('in if condition')
        con= mysql.connector.connect(user='root', password='root', host='localhost', database='flask')
        print('connection established')

        print('in connection mysql')
        sql = "SELECT * FROM signup where email = %s and password = %s ;"
        print(sql)
        cursors = con.cursor()
        cursors.execute(sql, (email, password,))
        data = cursors.fetchone()
        con.commit()
        #print(data[0])
        if data:
            Authorization = random.randrange(1,1094387485)
            print(Authorization)
            print(data[0])

            sql = "INSERT INTO token_data(token, status,user_id) VALUES( %s, %s,%s);"
            data = (Authorization, True, data[0])
            cursors.execute(sql, data)
            con.commit()

            resp = jsonify(message='login successfully!', token=Authorization)
            resp.status_code = 200
            cursors.close()
            con.close()
            return resp
        else:
            resp = jsonify('login failed not valid user!')
            resp.status_code = 404
            cursors.close()
            con.close()
            return resp

    else:
        return not_found()


@app.route('/update', methods=['POST'])
def update_task():
    try:
        json = request.json
        task_name = json['task_name']
        token = request.headers.get('token')

        # validate the received values
        if task_name and request.method == 'POST':
            con = mysql.connector.connect(user='root', password='root', host='localhost', database='flask')
            print('hello updated')

            sql = "SELECT user_id FROM token_data where token = %s;"
            print(sql)
            cursors = con.cursor()
            cursors.execute(sql, (token,))
            user_id = cursors.fetchone()
            con.commit()
            print(user_id[0])

            sql_update = "UPDATE tasks SET task_name=%s, WHERE user_id=%s"
            cursors = con.cursor()
            cursors.execute(sql_update, user_id[0])
            con.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)



@app.route('/delete')
def delete_task():
    try:
        print('in')
        json = request.json
        task_id = json['task_id']
        token = request.headers.get('token')
        print(task_id, token)
        con = mysql.connector.connect(user='root', password='root', host='localhost', database='flask')

        sql = "SELECT user_id , status FROM token_data where token = %s;"
        print(sql)
        cursors = con.cursor()
        cursors.execute(sql, (token,))
        user_id = cursors.fetchone()
        con.commit()
        print(user_id[0], user_id[1])

       # cursors = con.cursor()
        dele = "UPDATE tasks SET is_deleted = %s WHERE user_id=%s and task_id=%s;"
        print(dele)
        #if user_id[1] == 1:

        cursors.execute(dele, (True,user_id[0], task_id,))
        con.commit()
        resp = jsonify('task deleted successfully!')
        resp.status_code = 200
        return resp
       # else:
            #resp = jsonify(message='session expired , login again')
            #return resp

    except Exception as e:
        print(e)


@app.route('/complete_mark')
def complete_task():
    try:
        print('in')
        json = request.json
        task_id = json['task_id']
        token = request.headers.get('token')
        print(task_id, token)
        con = mysql.connector.connect(user='root', password='root', host='localhost', database='flask')

        sql = "SELECT user_id , status FROM token_data where token = %s;"
        print(sql)
        cursors = con.cursor()
        cursors.execute(sql, (token,))
        user_id = cursors.fetchone()
        con.commit()
        print(user_id[0], user_id[1])

       # cursors = con.cursor()
        dele = "UPDATE tasks SET is_completed = %s WHERE user_id=%s and task_id=%s;"
        print(dele)
        #if user_id[1] == 1:

        cursors.execute(dele, (True,user_id[0], task_id,))
        con.commit()
        resp = jsonify('completed marked successfully!')
        resp.status_code = 200
        return resp
        #else:
           # resp = jsonify(message='session expired , login again')
           # return resp
    except Exception as e:
        print(e)

@app.route('/view_tasks')
def view_task():
    try:
        print('in view_tasks method')

        token = request.headers.get('token')
        #print(task_id, token)
        con = mysql.connector.connect(user='root', password='root', host='localhost', database='flask')

        sql = "SELECT user_id , status FROM token_data where token = %s;"
        print(sql)
        cursors = con.cursor()
        cursors.execute(sql, (token,))
        user_id = cursors.fetchone()
        con.commit()
        print(user_id[0],user_id[1])

        view = "SELECT * from tasks WHERE user_id=%s;"
        print(view)

        cursors.execute(view, (user_id[0],))
        tasks = cursors.fetchall()

        con.commit()
        resp = jsonify(message='your task list', task=tasks)
        resp.status_code = 200
        return resp


    except Exception as e:
        print(e)


@app.route('/logout')
def logout():
    try:
        print('in')

        token = request.headers.get('token')
        #print(task_id, token)
        con = mysql.connector.connect(user='root', password='root', host='localhost', database='flask')

        sql = "UPDATE token_data SET status = %s WHERE  token=%s;"
        print(sql)
        cursors = con.cursor()
        cursors.execute(sql,(False,token,))
        con.commit()

        resp = jsonify(message='logout successful')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)





@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    serve(app, host='127.0.0.1',port='5002')