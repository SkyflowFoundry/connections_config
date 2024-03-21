# Testing Skyflow Connections with PipeDream

This repository contains Python scripts to set up and run a connection between Skyflow and PipeDream, which serves as an echo server for connection testing. The scripts are designed to be run in sequence and are a reference for setting up and running connections with Skyflow.

## 0. Prerequisites

Before you begin, get the following information and update the constants at the top of `skyflow_connections_setup.py`:

- `VAULT_ID`: ID of the vault. To get a vault's ID in Studio, navigate to the vault, then click the gear icon (Settings) in the side navigation.
- `SKYFLOW_ACCOUNT_ID`: ID of the Skyflow account. To get an account ID in Studio, navigate to a vault, then click the gear icon (Settings) in the side navigation.
- `VAULT_OWNER_SA_CREDENTIALS`: Credentials of a service account with Vault Owner permissions. If you used Studio to create the service account, this is the contents of your _credentials.json_ file.

  If you don't have a service account with the Vault Owner permissions, you can create a service account with the [Management API](https://docs.skyflow.com/management/#ServiceAccountService_CreateAPIKey) or through [Studio](https://docs.skyflow.com/api-authentication/#create-a-service-account).

You can change the `REQUEST_BIN_BASE_URL`, but feel free to use the one specified in the script.

## 1. Set up the vault via [vault_setup.py](/vault_setup.py)

(TODO)

## 2. Setup Connections via [skyflow_connections_setup.py](/skyflow_connections_setup.py)

`skyflow_connections_setup.py` creates and configures a connection to PipeDream (RequestBin), which serves as an echo server. It uses a Quickstart vault and the `credit_cards` table.

To run this script, run the following command in a terminal:

```bash
python skyflow_connections_setup.py
```

The script creates a connection to PipeDream and configures it to tokenize `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

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