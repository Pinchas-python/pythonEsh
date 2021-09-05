import json

issue_data= open('issueData.json')
json_data = json.loads(issue_data)

print(json_data)