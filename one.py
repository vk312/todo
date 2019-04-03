import requests
rget = requests.get('https://api.github.com/events')                            #get method
print(rget.json())
print(rget.raise_for_status())          #rget.raise_for_status()
print(rget.status_code)                 #rget.status_code
rpost = requests.post('https://httpbin.org/post', data={'task': 'complete'})        #post methnod
print(rpost)
rput = requests.put('https://httpbin.org/put', data={'task': 'complete'})           #put method
print(rput)
rdelete = ('https://httpbin.org/delete')                                            #delete method
print(rdelete)
rhead = requests.head('https://httpbin.org/get')                                    #head method
print(rhead)
roption = requests.options('https://httpbin.org/get')                               #options method
print(roption)

#passing parameters in url's
payload = {'task1': 'add', 'task2': ['delete','view']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
print(r)

#headers
url = 'https://httpbin.org/get'
headers = {'user-agent':'my-app'}
rr = requests.get(url, headers=headers)
#print(rr.content)
