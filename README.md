# Testing Skyflow Connections with PipeDream

This repository contains a procedure and Python scripts to set up and run a connection between Skyflow and PipeDream, which serves as an echo server for connection testing. The scripts also act as references for setting up and running connections with Skyflow. Additionally, the repository contains a GitHub Actions workflow to automate the process of updating the connection with new configuration values.

## 1. Create a Quickstart vault

Before you get started, you need a vault. To create a Quickstart vault,

1. In Studio, click **Add Vault**.

   If you need help locating your Studio URL, see [Accounts and environments](https://docs.skyflow.com/accounts-and-environments/).

2. Click **Start with a template**.
3. Under **Quickstart**, click **Create**.

   Studio sets up a Quickstart vault with two samples tables and some sample data.

4. In the side navigation, click **Settings** the gear icon.
5. Note your **Account ID** and **Vault ID**. You need these values to set up the connection.

## 2. Create an API key

Next, create a service account with an API key for authentication in the Python scripts.

1. In the side navigation, click **Access** (the people icon).
2. In the upper navigation, click **Service accounts**.
3. Click **Add service account**.
4. For **Name**, enter a name for the service account.
5. Click **Next**.
6. For **Authentication type**, choose **API key**.
7. Click **Next**.
8. For **Select Resource**, choose your vault.
9. For **Roles**, choose **Vault Owner**.
10. Click **Create service account**.
11. Click **Copy to clipboard** to copy the API key. Store it somewhere secure.
12. Click **Got it**.

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

1. Set your environment variables:

   ```bash
   export VAULT_ID=<Your Vault ID>
   export SKYFLOW_ACCOUNT_ID=<Your Account ID>
   export VAULT_OWNER_SA_CREDENTIALS=<Your API key>
   export SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT=https://manage.skyflowapis.com/v1/gateway/outboundRoutes
   export REQUEST_BIN_BASE_URL=https://ens3s06g2e69r.x.pipedream.net
   export REQUEST_BIN_RELATIVE_PATH=/sample/post/request/
   ```

1. Open `config_payload.json` and update the `vaultID` field to your Vault ID.

## 4. Create the connection

[skyflow_connections_setup.py](/skyflow_connections_setup.py) creates and configures a connection to PipeDream (RequestBin), which serves as an echo server. It uses the `credit_cards` table in your Quickstart vault.

To create the connection, run the following command:

```bash
python skyflow_connections_setup.py
```

Note your connection ID and URL. You'll need them for the next steps.

The script creates a connection to PipeDream and configures it to tokenize `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

## 5. Invoke the connection

`skyflow_connections_invocation.py` invokes the connection created in the previous step with a payload of `cardholder_name`, `card_number`, `expiry_month`, and `expiry_year`.

To invoke the connection, run the following command:

```bash
python skyflow_connections_invocation.py <CONNECTION_URL>
```

After you run the script, you can verify its functionality by:

- Observing the request and the tokenized values landing in the configured PipeDream endpoint.
- Checking that the vault is populated with the payload of the request.

## 6. Automate connection updates with GitHub Actions

To automate the process of updating the connection with new configuration values, you can set up a workflow to update the configuration whenever [`config_payload.json`](/config_payload.json) is modified.

To set up the workflow, you need to add the `VAULT_OWNER_SA_CREDENTIALS` as a repository secret in GitHub:

1. In GitHub, navigate to the repository.
2. Click the **Settings** tab.
3. In the left navigation, click **Secrets and variables > Actions**.
4. Click **New repository secret**.
5. For **Name**, enter `VAULT_OWNER_SA_CREDENTIALS`.
6. For **Secret**, enter your API key.
7. Click **Add secret**.

**Note:** You can repeat this process for the `SKYFLOW_ACCOUNT_ID`, `VAULT_ID`, and `SKYFLOW_CONNECTION_ID` secrets as well if you prefer to not hardcode them in the workflow.

After you add the secret, you need to update the GitHub Actions workflow template with your information:

1. Open _.github/workflows/main.yaml_ and update the `env` section with your information:

   ```yaml
   env:
      SKYFLOW_ACCOUNT_ID: "<ACCOUNT_ID>"
      VAULT_ID: "<VAULT_ID>"
      SKYFLOW_CONNECTION_ID: "<CONNECTION_ID>"
      VAULT_OWNER_SA_CREDENTIALS: ${{secrets.VAULT_OWNER_SA_CREDENTIALS}}
      REQUEST_BIN_BASE_URL: "https://ens3s06g2e69r.x.pipedream.net"
      REQUEST_BIN_RELATIVE_PATH: "/sample/post/request/"
      SKYFLOW_OUTBOUND_CONNECTION_ENDPOINT: "https://manage.skyflowapis.com/v1/gateway/outboundRoutes"
   ```

2. Save, close, commit, and push the file.

Now whenever `config_payload.json` is modified and pushed to GitHub, the workflow updates your connection with the new configuration values. You can also run the workflow manually by navigating to the **Actions** tab in your repository, selecting the workflow, and clicking **Run workflow**.
