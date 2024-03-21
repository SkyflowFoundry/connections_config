# Testing Skyflow Connections with PipeDream

This repository contains Python scripts to set up and run a connection between Skyflow and PipeDream, which serves as an echo server for connection testing. The scripts are designed to be run in sequence and are a reference for setting up and running connections with Skyflow.

## 0. Prerequisites

Before you begin, get the following information and update the constants at the top of `skyflow_connections_setup.py`:

- `VAULT_ID`: ID of the vault. To get a vault's ID in Studio, navigate to the vault, then click the gear icon (Settings) in the side navigation.
- `VAULT_OWNER_SA_CREDENTIALS`: Credentials of the vault service account
- `SKYFLOW_ACCOUNT_ID`: ID of the Skyflow account

You can change the `REQUEST_BIN_BASE_URL`, but feel free to use the one specified in the script.

If you don't have a service account with the Vault Owner permissions, you can create a service account with the [Management API](https://docs.skyflow.com/management/#ServiceAccountService_CreateAPIKey) or through [Studio](https://docs.skyflow.com/api-authentication/#create-a-service-account).

## 1. Set up the vault via [vault_setup.py](/vault_setup.py)

(TODO)

## 2. Setup Connections via [skyflow_connections_setup.py](/skyflow_connections_setup.py)

`skyflow_connections_setup.py` is a Python script and configuration used to establish a connection to PipeDream (RequestBin), which serves as an echo server. It utilizes the pre-created Quick Start vault and the `credit_cards` table.

### Usage

To run this script, follow these steps:

1. Make the necessary changes mentioned above.
2. Execute the script.
3. The script will create a connection configuration to tokenize `cardholder_name`, `card_number`, `expiry_month`, `expiry_year`, and optionally `cvv`.

## 3. Invoke the Connection via [skyflow_connections_invocation.py](/skyflow_connections_invocation.py)

(TODO)

Next, the script will invoke the created connection with a payload of `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

### Verification

After running the script, you can verify its functionality by:

- Observing the request and the tokenized values landing in PipeDream endpoint configured.
- Checking that the vault is populated with the payload of the request.

## 4. Automate Connection updates via GitHub Actions

(TODO)

...via GitHub Actions. You can set up a workflow to trigger it whenever {TODO: JSON file} is modified with new values.