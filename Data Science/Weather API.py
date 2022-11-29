#%% libraries
import pandas as pd
import requests
import json

#%% Credentials
api_key = "d6fab9816abda8d0a5505a7bbfd1bb7f"
lat = 39.1502
lon = 123.2078
cnt = 16
cnh = 7


#%% API
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)

weather_forcast = json.loads(response.text)
weather_forcast

# pd.json_normalize(weather_forcast)



#%%
import json
# load data using Python JSON module
with open('data/nested_array.json','r') as f:
    data = json.loads(f.read())
# Flatten data
df_nested_list = pd.json_normalize(data, record_path =['students'])

#%% History
response = requests.get(f"https://history.openweathermap.org/data/2.5/history/city?lat=41.85&lon=-87.65&appid={api_key}")

weather_history = json.loads(response.text)

print(data)

