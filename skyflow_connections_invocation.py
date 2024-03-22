import os
import json
import requests
import sys

#Define constants
VAULT_OWNER_SA_CREDENTIALS = 'Bearer '+ str(os.environ.get('VAULT_OWNER_SA_CREDENTIALS', ''))
SKYFLOW_CONNECTION_URL = sys.argv[1]

# Invoke the created connection to tokenize a simple message to RequestBin

# Set headers for connection invocation request
connection_invocation_headers = {
    'Content-Type': 'application/json',
    'Authorization': VAULT_OWNER_SA_CREDENTIALS
}

# Create Connection Invocation Payload
with open('connections_invocation_payload.json', 'r') as file:
    connection_invocation_payload = json.dumps(json.load(file))

# Send request to invoke connection
response = requests.request("POST", SKYFLOW_CONNECTION_URL,
                            headers=connection_invocation_headers,
                            data=connection_invocation_payload)

# Print response
print(response.text)
