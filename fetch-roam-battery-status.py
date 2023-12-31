import soco
import json
import requests
import xmltodict
import time
import pathlib


speaker_ip = ''
for speaker in soco.discover():
    if speaker.player_name == 'Sonos Roam':
        speaker_ip = speaker.ip_address

if speaker_ip == '':
    print('Sonos Roam not found')
    quit()


r = requests.get(url = 'http://' + speaker_ip + ':1400/status/batterystatus')

dict_data = xmltodict.parse(r.content)

json_data = {}

for data in dict_data["ZPSupportInfo"]["LocalBatteryStatus"]["Data"]:
    json_data[data["@name"]] = data["#text"]

json_data["time"] = time.time()

with open(str(pathlib.Path(__file__).parent.resolve()) + "/public/battery_data.json", "w") as outfile:
    json.dump(json_data, outfile)

