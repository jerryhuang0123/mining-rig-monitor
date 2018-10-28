import json

#resp: http response
def parse_http_response_to_json(resp):
	resp_str = resp.text
	print(resp_str)
	json_data = json.loads(resp_str)
	return json_data