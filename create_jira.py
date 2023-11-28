import pip._vendor.requests
from pip._vendor.requests.auth import HTTPBasicAuth
import json

url = "<your-jira-account-url>/rest/api/3/issue"

API_TOKEN = "<your-api-token>"

auth = HTTPBasicAuth("<your-jiraaa-email-address>", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My  First Jira Script With Python Scripting",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10001"
    },
    "project": {
      "key": "KP"
    },
    "summary": "My First Jira Ticket  With Python Script",
  },
  "update": {}
} )

response = pip._vendor.requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))