import requests
import json
import time
# from scipy.stats import pearsonr

requesturl = 'https://api.opendota.com/api/'

playerdata = {}

enduser = 79944981
userstr = input('> How many users would you like to search? ')
usernum = int(userstr)
filestr = 'jsondump' + str(time.time()) + 'txt'

f = open(filestr, 'w')

for player in range(enduser - (usernum - 1), enduser):
    time.sleep(1)
    cloudstring = requests.get(requesturl + 'players/' + str(player) + '/wordcloud')
    if (cloudstring == None):
        continue
    cloudjson = json.loads(cloudstring.text)

    countstring = requests.get(requesturl + 'players/' + str(player) + '/counts')
    if (countstring == None):
        continue
    countjson = json.loads(countstring.text)

    # print(player)
    # print(countjson)
    if 'my_word_counts' in cloudjson and '3' in countjson['leaver_status']:
        playerdata[player] = [cloudjson['my_word_counts'], countjson['leaver_status']]

json.dump(playerdata, f)
