import requests
import json

BASE_URL = "https://api.jdoodle.com/v1/execute"

headers = {'content-type': 'application/json'}
with open('tests/test_wealth_manger.py', 'r') as f:
	code = f.read()

data = {
	'script': code,
	'language': "python3",
	'versionIndex': '2',
	'clientId': '8acba1648460ab5cc5e502f507d3230e',
	'clientSecret': '6ca2d92b2a297ad77ddd01da8f73f39228f07b4fdee1bb5dfbd0f90d517cb64b',
}

json_data = json.dumps(data)


r = requests.post(url=BASE_URL, data=json_data, headers=headers)
print(r.json())




