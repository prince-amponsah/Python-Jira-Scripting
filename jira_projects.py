# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import pip._vendor.requests as reqs
from pip._vendor.requests.auth import HTTPBasicAuth
import json

url = "<your-jira-account-url>/rest/api/3/issue"

API_TOKEN = "<your-api-token>"

auth = HTTPBasicAuth("<your-jiraaa-email-address>", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = reqs.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)


name = output[0]["name"]
print(name)


#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))