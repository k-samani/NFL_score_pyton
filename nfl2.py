import json
import requests
import itertools
import time

def Get_Source(link):
    g_url = link
    req = requests.get(g_url, 'html.parser')
    with open('html_source.txt', 'w') as f:
        f.write(req.text)
        f.close()
    
    return req.text


parsed_source = Get_Source('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')

the_list = {}

with open('html_source.txt', 'r') as f:
    nfl_data = json.load(f)

for i in nfl_data['events']:
    #print(i['name'])
    for k in i['competitions']:
        for l in k['competitors']:
           the_list[l['team']['displayName']] = l['score']



x=0
for key in the_list:
    if x < 1:
        print()
        print(key + " " + the_list[key] + " vs ")
        x = x + 1
    else:
        print(key + " " + the_list[key])
        x = 0
        print()
    