import json
from wsgiref.simple_server import make_server

def hello_world_app(environ, start_response):
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')] # HTTP Headers
    dic= {'list':[{'auto_increment_id':1 ,'done':'true' , 'subject':'oops'}]}
    start_response(status, headers)
    json_mylist = json.dumps(dic)
    bb = bytes(json_mylist,'utf8')
    return [bb]


httpd = make_server('', 8001, hello_world_app)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()
