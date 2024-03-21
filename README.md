# Testing Skyflow Connections with PipeDream

This repository contains Python scripts to set up and run a connection between Skyflow and PipeDream, which serves as an echo server for connection testing. The scripts are designed to be run in sequence and are a reference for setting up and running connections with Skyflow.

## 0. Prerequisites

Before you begin, get the following information and update the constants at the top of `skyflow_connections_setup.py`:

- `VAULT_ID`: ID of the vault. To get a vault's ID in Studio, navigate to the vault, then click the gear icon (Settings) in the side navigation.
- `SKYFLOW_ACCOUNT_ID`: ID of the Skyflow account. To get an account ID in Studio, navigate to a vault, then click the gear icon (Settings) in the side navigation.
- `VAULT_OWNER_SA_CREDENTIALS`: A bearer token for a service account with Vault Owner permissions.
  
  For Trial environments, use the following process.
  1. In Studio, click your account icon and choose __Generate API Bearer Token__.
  2. Click __Generate Token__.

  For Sandbox and Production environments, generate a bearer token from service account credentials with the [Python SDK](https://github.com/skyflowapi/skyflow-python/blob/main/samples/generate_bearer_token_from_creds_sample.py). For more information and options, see [Authenticate](https://docs.skyflow.com/api-authentication/).

  If you don't have a service account with the Vault Owner permissions, you can create a service account through [Studio](https://docs.skyflow.com/api-authentication/#create-a-service-account) or with the [Management API](https://docs.skyflow.com/management/#ServiceAccountService_CreateAPIKey).

You can change the `REQUEST_BIN_BASE_URL`, but feel free to use the one specified in the script.

## 1. Set up the vault via [vault_setup.py](/vault_setup.py)

(TODO)

## 2. Setup Connections via [skyflow_connections_setup.py](/skyflow_connections_setup.py)

`skyflow_connections_setup.py` creates and configures a connection to PipeDream (RequestBin), which serves as an echo server. It uses a Quickstart vault and the `credit_cards` table.

To run this script, run the following command:

```bash
python skyflow_connections_setup.py
```

The script creates a connection to PipeDream and configures it to tokenize `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

## 3. Invoke the Connection via [skyflow_connections_invocation.py](/skyflow_connections_invocation.py)

`skyflow_connections_invocation.py` invokes the connection created in the previous step with a payload of `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

To run this script, run the following command:

```bash
(TODO)
```

After you run the script, you can verify its functionality by:

- Observing the request and the tokenized values landing in the configured PipeDream endpoint.
- Checking that the vault is populated with the payload of the request.

## 4. Automate Connection updates with GitHub Actions

To automate the process of updating the connection with new configuration values, you can set up a workflow to update the configuration whenever [`config_payload.json`](/config_payload.json) is modified.

1. 