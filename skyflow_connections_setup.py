import os
import json
import requests
import sys

# Define constants
# Define constants
# saAPIKey = str(os.environ.get('VAULT_OWNER_SA_API_KEY', ''))

# Change the below 6 constants according to your vault and RequestBin entries
SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT = str(os.environ.get('SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT', ''))
#sa_creds = "Bearer sky-ae63e-k8117f25e83e4c68bc8f9e642e3e1c29"
#print("sa_creds :", sa_creds)
VAULT_OWNER_SA_CREDENTIALS = 'Bearer '+ str(os.environ.get('VAULT_OWNER_SA_CREDENTIALS', ''))
VAULT_ID = str(os.environ.get('VAULT_ID', ''))  # Replace with your Vault ID
SKYFLOW_ACCOUNT_ID = str(os.environ.get('SKYFLOW_ACCOUNT_ID', ''))  # Replace Account ID with your Account ID
#SKYFLOW_ACCOUNT_ID = "t50877c6ada449308cff528e38467614"
REQUEST_BIN_BASE_URL = str(os.environ.get('REQUEST_BIN_BASE_URL', ''))
REQUEST_BIN_RELATIVE_PATH = str(os.environ.get('REQUEST_BIN_RELATIVE_PATH', ''))

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
# Extract connection ID and URL

connection_id = response.json().get('ID')
connection_url = response.json().get('connectionURL') + REQUEST_BIN_RELATIVE_PATH
print("Connection URL :", connection_url)
