# Testing Skyflow Connections with PipeDream

This repository contains a procedure and Python scripts to set up and run a connection between Skyflow and PipeDream, which serves as an echo server for connection testing. The scripts also act as references for setting up and running connections with Skyflow. Additionally, the repository contains a GitHub Actions workflow to automate the process of updating the connection with new configuration values.

## 1. Create a Quickstart vault

Before you get started, you need a vault. To create a Quickstart vault,

1. In Studio, click **Create Vault**.

   If you need help locating your Studio URL, see [Accounts and environments](https://docs.skyflow.com/accounts-and-environments/).

2. Click **Start with a template**.
3. Under **Quickstart**, click **Create**.

   Studio sets up a Quickstart vault with two samples tables and some sample data.

4. In the side navigation, click the gear icon (Settings).
5. Note your **Vault ID** and **Account ID**. You need these values to set up the connection.

## 2. Create an API key

Next, create a service account with an API key for authentication in the Python scripts.

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

## 3. Set up your local environment

1. Clone the repository:

   ```bash
   git clone https://github.com/SkyflowFoundry/connections_config
   cd connections_config
   ```

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. Install the required packages:

   ```bash
    pip install -r requirements.txt
    ```

1. Open `skyflow_connections_setup.py` and update the constanst with the values you collected in the previous steps:

    | Constant                     | Description     |
    | ---------------------------- | --------------- |
    | `VAULT_ID`                   | Your Vault ID.  |
    | `SKYFLOW_ACCOUNT_ID`         | You Account ID. |
    | `VAULT_OWNER_SA_CREDENTIALS` | You API key.    |

    You can change `REQUEST_BIN_BASE_URL`, but feel free to use the one specified in the script.

1. Save and close the file.

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
6. For **Secret**, enter your API key.
7. Click **Add secret**.

After you add the secret, the GitHub Actions workflow in [`.github/workflows/main.yaml`](/.github/workflows/main.yaml) runs whenever `config_payload.json` is modified and pushed to GitHub. The workflow updates the connection with the new configuration values.
