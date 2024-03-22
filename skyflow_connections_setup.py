import os
import json
import requests
import sys
'''
# Define constants
# Change the below 6 constants according to your vault and RequestBin entries
SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT = str(os.environ.get('SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT', 'https://manage.skyflowapis.com/v1/gateway/outboundRoutes'))
SKYFLOW_ACCOUNT_ID = str(os.environ.get('SKYFLOW_ACCOUNT_ID', ''))  # Your Account ID
VAULT_ID = str(os.environ.get('VAULT_ID', ''))  # Your Vault ID
VAULT_OWNER_SA_CREDENTIALS = str(os.environ.get('VAULT_OWNER_SA_CREDENTIALS', '')) # Your API key
REQUEST_BIN_BASE_URL = str(os.environ.get('REQUEST_BIN_BASE_URL', 'https://ens3s06g2e69r.x.pipedream.net'))
REQUEST_BIN_RELATIVE_PATH = str(os.environ.get('REQUEST_BIN_RELATIVE_PATH', '/sample/post/request/'))
'''
SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT = str(os.environ.get('SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT', 'https://manage.skyflowapis.com/v1/gateway/outboundRoutes'))
VAULT_OWNER_SA_CREDENTIALS = 'Bearer ' + str(os.environ.get('VAULT_OWNER_SA_CREDENTIALS', '')) # Your API key
VAULT_ID = str(os.environ.get('VAULT_ID', ''))  # Your Vault ID
SKYFLOW_ACCOUNT_ID = str(os.environ.get('SKYFLOW_ACCOUNT_ID', ''))  # Your Account ID
REQUEST_BIN_BASE_URL = str(os.environ.get('REQUEST_BIN_BASE_URL', 'https://ens3s06g2e69r.x.pipedream.net'))
REQUEST_BIN_RELATIVE_PATH = str(os.environ.get('REQUEST_BIN_RELATIVE_PATH', '/sample/post/request/'))

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
response = requests.request("POST", SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT,
                            headers=connection_creation_headers,
                            data=connection_creation_payload)
print(response.request.url)
print(response.request.body)
print(response.request.headers)

print(response.text)
# Extract connection ID and URL
connection_id = response.json().get('ID')
connection_url = response.json().get('connectionURL') + REQUEST_BIN_RELATIVE_PATH
print("Connection URL :", connection_url)
print("Connection ID :", connection_id)
