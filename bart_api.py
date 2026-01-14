import requests
import json

# Public key form bar.gov site.
key = "MW9S-E7SL-26DU-VV8V"
jfile = "data.json"

response = requests.get(f"https://api.bart.gov/api/etd.aspx?cmd=etd&key={key}&json=y")
data = response.json()
with open("data.json","w") as json_file:
    json.dump(data,json_file,indent=4)
