import requests   #response = request
import json
from datetime import datetime



# --apiurl = "http://api.open-notify.org/astros.json"
apiurl = "http://api.open-notify.org/iss-pass.json"


parameters = {
    "lat": 40.71,
    "lon": -74
}



# -- = requests.get(apiurl)
response = requests.get(apiurl, params=parameters)
print(response.status_code)
# --print(response.json())

#for printing in json format with --dumps()
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

# ----< extracting 'pass times' from json obj >
pass_times = response.json()['response']
jprint(pass_times)

#----< extracting 'rise times' from 'pass_times' >
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)


##<make object> :datatime
#-----< converting 'risetimes' to readable human values >
#from datetime import datetime
times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
