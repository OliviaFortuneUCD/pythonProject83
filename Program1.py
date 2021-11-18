import json

import urllib.request
# load the current status of the ISS in real-time
url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Extract the ISS location
location = result["iss_position"]
lat = location['latitude']
lon = location['longitude']

# Output lon and lat to the terminal in the
# float format
lat = float(lat)
lon = float(lon)
print("\nLatitude: " + str(lat))
print("\nLongitude: " + str(lon))