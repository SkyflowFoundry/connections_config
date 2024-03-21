import json
import requests

# Define constants
SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT = 'https://manage.skyflowapis.com/v1/gateway/outboundRoutes'
VAULT_OWNER_SA_CREDENTIALS = 'Bearer sky-nb934-e64a0b4b69174eeeb160b02e82ef54ef'
VAULT_ID = 'w6063d10d50d4386807dd7794f714577'  # Replace with your Vault ID
SKYFLOW_ACCOUNT_ID = 't50877c6ada449308cff528e38467614'  # Replace Account ID with your Account ID
REQUEST_BIN_BASE_URL = 'https://ens3s06g2e69r.x.pipedream.net'
REQUEST_BIN_RELATIVE_PATH = '/sample/post/request/'
SKYFLOW_CONNECTION_ID = "f684f9dde104472f9a00a0fc679314dd"

# Construct the Connection Update URL
connectionUpdateUrl = SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT + '/' + SKYFLOW_CONNECTION_ID
print(connectionUpdateUrl)

# Create a Skyflow Connection payload
with open('config_payload.json', 'r') as file:
    connection_creation_payload = json.dumps(json.load(file))

# Set headers for connection creation request
connection_creation_headers = {
    'X-SKYFLOW-ACCOUNT-ID': SKYFLOW_ACCOUNT_ID,
    'Content-Type': 'application/json',
    'Authorization': VAULT_OWNER_SA_CREDENTIALS
}

# Send request to create connection
response = requests.request("PUT", connectionUpdateUrl,
                            headers=connection_creation_headers,
                            data=connection_creation_payload)
# Extract connection ID and URL

print(response.request.url)
print(response.request.body)
print(response.request.headers)
print(response)
