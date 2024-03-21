import json
import requests

#Define constants
VAULT_OWNER_SA_CREDENTIALS = 'Bearer sky-ae63e-k8117f25e83e4c68bc8f9e642e3e1c29'
SKYFLOW_CONNECTION_URL = "https://ebfc9bee4242.gateway.skyflowapis.com/v1/gateway/outboundRoutes/da75a471be5b43ee86b51665075260aa/sample/post/request/"

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
