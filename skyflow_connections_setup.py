import os
import json
import requests
import sys

# Define constants
# Change the below 6 constants according to your vault and RequestBin entries
#SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT = str(os.environ.get('SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT', ''))
SKYFLOW_ACCOUNT_ID = str(os.environ.get('SKYFLOW_ACCOUNT_ID', ''))  # Your Account ID
VAULT_ID = str(os.environ.get('VAULT_ID', ''))  # Your Vault ID
VAULT_OWNER_SA_CREDENTIALS = str(os.environ.get('VAULT_OWNER_SA_CREDENTIALS', '')) # Your API key
REQUEST_BIN_BASE_URL = str(os.environ.get('REQUEST_BIN_BASE_URL', ''))
REQUEST_BIN_RELATIVE_PATH = str(os.environ.get('REQUEST_BIN_RELATIVE_PATH', ''))

SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT = 'https://manage.skyflowapis.com/v1/gateway/outboundRoutes'
#VAULT_OWNER_SA_CREDENTIALS = 'Bearer sky-n8caa-j3c09c30b9e345b68ff5bbf95cff5f88'
#VAULT_ID = 'w6063d10d50d4386807dd7794f714577'  # Replace with your Vault ID
#SKYFLOW_ACCOUNT_ID = 't50877c6ada449308cff528e38467614'  # Replace Account ID with your Account ID
#REQUEST_BIN_BASE_URL = 'https://ens3s06g2e69r.x.pipedream.net'
#REQUEST_BIN_RELATIVE_PATH = '/sample/post/request/'

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
print(response.request.body)
# Extract connection ID and URL
connection_id = response.json().get('ID')
connection_url = response.json().get('connectionURL') + REQUEST_BIN_RELATIVE_PATH
print("Connection URL :", connection_url)
print("Connection ID :", connection_id)
