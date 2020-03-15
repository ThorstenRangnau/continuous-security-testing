import json

with open('/jmeter/results/zap/json/LoginTesting.JSON') as f:
	data = json.load(f)
	if len(data['alerts']) != 0:
		exit(1)
