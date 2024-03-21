import json
import requests

# Define constants
SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT = str(os.environ.get('SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT', ''))
VAULT_OWNER_SA_CREDENTIALS = str(os.environ.get('VAULT_OWNER_SA_CREDENTIALS', ''))
VAULT_ID = str(os.environ.get('VAULT_ID', ''))  # Replace with your Vault ID
SKYFLOW_ACCOUNT_ID = str(os.environ.get('SKYFLOW_ACCOUNT_ID', ''))  # Replace Account ID with your Account ID
REQUEST_BIN_BASE_URL = str(os.environ.get('REQUEST_BIN_BASE_URL', ''))
REQUEST_BIN_RELATIVE_PATH = str(os.environ.get('REQUEST_BIN_RELATIVE_PATH', ''))
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
