#!/usr/bin/python

import requests
import json

# Let's call GetLoggedInUserInfo
url = 'https://login.netromedia.com/rest/GetLoggedInUserInfo'
# Set our content-type
headers = {'content-type':'application/json'}
# Grab your access token @ https://login.netromedia.com/Contacts/APITokens.aspx
payload = {'Token':'ADD-YOUR-TOKEN-HERE'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print json.load(r.text)
