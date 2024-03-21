# Skyflow Connections Setup

To use this script, ensure you have the following information and replace it in the constants at the top of the file:
- `vault_id`: ID of the vault
- `vault_service_account_credentials`: Credentials of the vault service account
- `skyflow_account_id`: ID of the Skyflow account

You could also change the `REQUEST_BIN_BASE_URL` if desired, but feel free to use the one provided in the script as well.

### 1. Setup the vault via [vault_setup.py](/vault_setup.py)
(TODO)

### 2. Setup Connections via [skyflow_connections_setup.py](/skyflow_connections_setup.py)

`skyflow_connections_setup.py` is a Python script and configuration used to establish a connection to PipeDream (RequestBin), which serves as an echo server. It utilizes the pre-created Quick Start vault and the `credit_cards` table.

#### Usage

To run this script, follow these steps:
1. Make the necessary changes mentioned above.
2. Execute the script.
3. The script will create a connection configuration to tokenize `cardholder_name`, `card_number`, `expiry_month`, `expiry_year`, and optionally `cvv`.




### 3. Invoke the Connection via [skyflow_connections_invocation.py](/skyflow_connections_invocation.py)

(TODO)

Next, the script will invoke the created connection with a payload of `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

#### Verification

After running the script, you can verify its functionality by:
- Observing the request and the tokenized values landing in PipeDream endpoint configured.
- Checking that the vault is populated with the payload of the request.

### 4. Automate Connection Updates via GitHub Actions

(TODO)

## Setup











## Vault Service Credentials

You can create vault service credentials using the [Skyflow API](https://docs.skyflow.com/management/#ServiceAccountService_CreateAPIKey) or through the UI.



## GitHub Actions

Alternatively, you can also run this script via GitHub Actions. You can set up a workflow to trigger it whenever `skyflow_connections_setup.py` is modified with new values.

