# Testing Skyflow Connections with PipeDream

This repository contains Python scripts to set up and run a connection between Skyflow and PipeDream, which serves as an echo server for connection testing. The scripts are designed to be run in sequence and are a reference for setting up and running connections with Skyflow. Additionally, the repository contains a GitHub Actions workflow to automate the process of updating the connection with new configuration values.

## 0. Prerequisites

Before you begin, get the following information and update the constants at the top of `skyflow_connections_setup.py`:

- `VAULT_ID`: ID of the vault. To get a vault's ID in Studio, navigate to the vault, then click the gear icon (Settings) in the side navigation.
- `SKYFLOW_ACCOUNT_ID`: ID of the Skyflow account. To get an account ID in Studio, navigate to a vault, then click the gear icon (Settings) in the side navigation.
- `VAULT_OWNER_SA_CREDENTIALS`: A bearer token for a service account with Vault Owner permissions.
  
  For Trial environments, use the following process.
  1. In Studio, click your account icon and choose **Generate API Bearer Token**.
  2. Click **Generate Token**.

  For Sandbox and Production environments, generate a bearer token from service account credentials with the [Python SDK](https://github.com/skyflowapi/skyflow-python/blob/main/samples/generate_bearer_token_from_creds_sample.py). For more information and options, see [Authenticate](https://docs.skyflow.com/api-authentication/).

  If you don't have a service account with the Vault Owner permissions, you can create a service account through [Studio](https://docs.skyflow.com/api-authentication/#create-a-service-account) or with the [Management API](https://docs.skyflow.com/management/#ServiceAccountService_CreateAPIKey).

You can change `REQUEST_BIN_BASE_URL`, but feel free to use the one specified in the script.

## 1. Create a Quickstart vault

To create a Quickstart vault,

1. In Studio, click **Create Vault**.
2. Click **Start with a template**.
3. Under **Quickstart**, click **Create**.

   Studio sets up a Quickstart vault with two samples tables and some sample data.

4. In the side navigation, click the gear icon (Settings).
5. Note your **Vault ID** and **Account ID**. You need these values to set up the connection.

## 2. Create an API key

Next, create a service account with an API key to use with the Python scripts.

1. In the side navigation, click the people icon (Access).
2. In the upper navigatino, click **Service accounts**.
3. Click **Add service account**.
4. For **Name**, enter a name for the service account.
5. Click **Next**.
6. For **Authentication type**, choose **API key**.
7. Click **Next**.
8. For **Select Resource**, choose your vault.
9. Click **Create service account**.
10. Click **Copy to clipboard** to copy the API key. Store it somewhere secure.
11. Click **Got it**.



## 3. Setup Connections via [skyflow_connections_setup.py](/skyflow_connections_setup.py)

`skyflow_connections_setup.py` creates and configures a connection to PipeDream (RequestBin), which serves as an echo server. It uses a Quickstart vault and the `credit_cards` table.

To set up the connection, run the following command:

```bash
python skyflow_connections_setup.py
```

The script creates a connection to PipeDream and configures it to tokenize `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

## 4. Invoke the Connection via [skyflow_connections_invocation.py](/skyflow_connections_invocation.py)

`skyflow_connections_invocation.py` invokes the connection created in the previous step with a payload of `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

To invoke the connection, run the following command:

```bash
python skyflow_connections_invocation.py
```

After you run the script, you can verify its functionality by:

- Observing the request and the tokenized values landing in the configured PipeDream endpoint.
- Checking that the vault is populated with the payload of the request.

## 5. Automate Connection updates with GitHub Actions

To automate the process of updating the connection with new configuration values, you can set up a workflow to update the configuration whenever [`config_payload.json`](/config_payload.json) is modified.

To set up the workflow, you need to add the `VAULT_OWNER_SA_CREDENTIALS` as a repository secret in GitHub:

1. In GitHub, navigate to the repository.
2. Click the **Settings** tab.
3. In the left navigation, click **Secrets and variables > Actions**.
4. Click **New repository secret**.
5. For **Name**, enter `VAULT_OWNER_SA_CREDENTIALS`.
6. For **Secret**, enter the bearer token for a service account with Vault Owner permissions.
7. Click **Add secret**.

After you add the secret, the GitHub Actions workflow in [`.github/workflows/main.yaml`](/.github/workflows/main.yaml) runs whenever `config_payload.json` is modified and pushed to GitHub. The workflow updates the connection with the new configuration values.
