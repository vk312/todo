import helper
from flask_mysqldb import MySQL
from flask import Flask, request, Response
from flask import Flask , config
import json

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


con = mysql.connect(host='localhost', user='root', password='root', db='flask')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/additem', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.get_json()
    task_name = req_data['task_name']
    #token = req_data['Authorization_key']

    # Add item to the list
    sql=" insert into tasks('task_name','is_deleted','is_completed','user_id') values(task_name,True,False,1);"
    result = con.execute(sql)
    print(result)
    # Return error if item not added
    if result is None:
        response = Response("{'error': 'Item not added - " + task_name + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(result), mimetype='application/json')

    return response


@app.route('/items/all')
def get_all_items():
    # Get items from the helper
    res_data = helper.get_all_items()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/item/status', methods=['GET'])
def get_item():
    # Get parameter from the URL
    item_name = request.args.get('name')

    # Get items from the helper
    status = helper.get_item(item_name)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error': 'Item Not Found - %s'}"  % item_name, status=404 , mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response



@app.route('/item/update', methods=['PUT'])
def update_status():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']
    status = req_data['status']

    # Update item in the list
    res_data = helper.update_status(item, status)

    # Return error if the status could not be updated
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response





@app.route('/item/remove', methods=['DELETE'])
def delete_item():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']

    # Delete item from the list
    res_data = helper.delete_item(item)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + item +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run(debug=True)