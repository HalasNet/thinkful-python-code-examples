import json

import requests

# Create Joe
joe = {
   "name": "Joe Turner",
   "email": "joe@oampo.co.uk"
}

requests.put("http://0.0.0.0:5000/api/user/1", data=json.dumps(joe),
             headers={'content-type': 'application/json'})

# Create Devon
devon = {
   "name": "Devon Campbell",
   "email": "devon@raddevon.com"
}

requests.put("http://0.0.0.0:5000/api/user/2", data=json.dumps(devon),
             headers={'content-type': 'application/json'})

# Get Devon back
request = requests.get("http://0.0.0.0:5000/api/user/2")
devon = request.json()
print devon

# Add the admin role to Devon
devon["roles"].append("admin")
requests.put("http://0.0.0.0:5000/api/user/2", data=json.dumps(devon),
             headers={'content-type': 'application/json'})

# Get Devon to make sure the role has been added
request = requests.get("http://0.0.0.0:5000/api/user/2")
devon = request.json()
print devon
