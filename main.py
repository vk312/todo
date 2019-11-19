from flask import Flask
import helper
from flask_mysqldb import MySQL
import pymysql
#from db_config import mysql
from flask import jsonify
from flask import Flask, request, Response
from flask import Flask , config
import json
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask'

mysql.init_app(app)





@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/additem', methods=['POST'])
def add_item():
    print('in additem method')
    con = mysql.connect(host='localhost', user='root', password='root', db='flask')

    # Get item from the POST body
    req_data = request.get_json()
    task_name = req_data['task_name']
    #token = req_data['Authorization_key']

    # Add item to the list
    sql=" insert into tasks('task_name','is_deleted','is_completed','user_id') values('task_name','True','False',1);"
    result = con.execute(sql)
    con.commit()
    print(result)
    # Return error if item not added
    if result is None:
        response = Response("{'error': 'Item not added - " + task_name + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(result))

    return response


if __name__ == '__main__':
    app.run()
