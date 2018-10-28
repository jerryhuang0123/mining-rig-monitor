import rigmonitor
import jsonreader
import requests

resp = requests.get('https://api.nanopool.org/v1/eth/hashrate/{0}'.format(rigmonitor.rig_address))

if(resp.status_code != 200):
	rigmonitor.SendSms("API call returning invalid status code {0}".format(resp.status_code))
else:
	data = jsonreader.parse_http_response_to_json(resp)
	if(data["data"] <= 20):
		rigmonitor.SendSms("Your Mining rig might be down with current hash rate at {0}".format(data["data"]))
	else:
		print(data["data"])