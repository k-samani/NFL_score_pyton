import json
import requests
import itertools

def Get_Source(link):
    g_url = link
    req = requests.get(g_url, 'html.parser')
    with open('html_source.txt', 'w') as f:
        f.write(req.text)
        f.close()
    
    return


Get_Source('https://www.espn.com/nfl/scoreboard')

with open('html_source.txt', 'r') as source:
    print(next(itertools.islice(source, 228, None)), file=open('output.txt', 'w'))
    source.close()

with open('output.txt', 'r') as f, open('output1.txt', 'w') as second:
    data = f.read()
    data = data.replace("</script><script>window.espn.scoreboardData 	= ", "")
    data = data.replace(';window.espn.scoreboardSettings = {"useStatic":false,"isCollege":false,"league":"nfl","scoreboardSponsorLogo":"https://a.espncdn.com/redesign/assets/img/logos/csb-color-en.svg","initialTopic":"scoreboard-football-nfl","showOddsSponsor":true,"scoWeek":"2021-4-2","defaults":{"week":4,"year":2021,"seasontype":2},"isWeekOriented":true,"useReplay":false,"sport":"football","editionKey":"espn-en"};if(!window.espn_ui.device.isMobile){window.espn.loadType = "ready"};</script>', "")
    second.write(data)
    
with open('output1.txt', 'r') as handle:
    parsed = json.load(handle)




print(json.dumps(parsed['events'], indent = 4), file=open('output1.txt', 'w'))

games = parsed['events']

games2 = json.dumps(games)

list_of_games = {}

for x in games:
    print(x['name'])
    for game in x['competitions']:
        for detials in game['competitors']:
            if detials['homeAway'] == 'home':
                print("                          " + detials['score'])
            else:
                print(detials['score'])
            
          