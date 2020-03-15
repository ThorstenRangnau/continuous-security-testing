import json

with open('/jmeter/results/zap/json/LoginTesting.JSON') as f:
	data = json.load(f)
	if len(data['alerts']) != 0:
		print("==========================")
		print("\nTEST RESULTS\n")
		print("Identified %d security vulnerabilities. See gitlab-ci artifacts for further details\n" % len(data['alerts']))
		print("==========================")
		exit(1)
