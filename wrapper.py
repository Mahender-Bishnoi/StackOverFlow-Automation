from subprocess import Popen, PIPE
import json
import requests
import webbrowser

process = Popen(['python', 'test.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
error_in_string = stderr.decode()
required_string = error_in_string.split('\n')[-2]
error_type = ""
error_message = ""
i = 0
while i<len(required_string):
    if required_string[i]==':':
        break
    else:
        error_type+=str(required_string[i])
    i+=1
i+=2
while i<len(required_string):
    error_message+=required_string[i]
    i+=1
# print(error_type)
# print(error_message)
language = "PYTHON"
URL = "https://api.stackexchange.com/2.2/search"
PARAMS = {'tagged':language,'intitle':error_message,'site':"stackoverflow"}
r = requests.get(url = URL, params = PARAMS) 
data = r.json() 
NumberOfLinksOpen = 5
for x in data['items']:
    if NumberOfLinksOpen<=0:
        break
    if x['is_answered']:
        links = x['link']
        webbrowser.open(links)
        NumberOfLinksOpen-=1
