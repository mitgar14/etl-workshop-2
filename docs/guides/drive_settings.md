# Project Configuration Guide

This guide will help you configure the `settings.yaml` file used by the `PyDrive2` library in conjunction with the `store.py` module. This setup is part of a data pipeline managed by Airflow. Follow the steps below to fill in the necessary configuration fields.

## Prerequisites

Before proceeding, ensure that you have:

- **Google Cloud credentials** with the necessary OAuth 2.0 credentials.
- Access to your **client ID**, **client secret**, and **redirect URI** for Google Drive API access.
- A valid path for saving **credentials** locally.

### Example `settings.yaml` File

Here is an example `settings.yaml` file with placeholder values. Replace the placeholder values with your own configuration details:

```yaml
client_config_backend: file
client_config:
  client_id: your_client_id.apps.googleusercontent.com
  client_secret: your_client_secret
  redirect_uris: ['http://localhost:8090/']
  auth_uri: https://accounts.google.com/o/oauth2/auth
  token_uri: https://accounts.google.com/o/oauth2/token

save_credentials: True
save_credentials_backend: file
save_credentials_file: /path/to/your/project/credentials/saved_credentials.json

get_refresh_token: True

oauth_scope:
  - https://www.googleapis.com/auth/drive
```
  
## Instructions for `settings.yaml`

### 1. **Client Configuration Backend**

This parameter tells PyDrive2 where to retrieve the OAuth 2.0 client configuration.

```yaml
client_config_backend: file
```

Leave this set to `file`, as it indicates that the client configuration will be loaded from a file.

### 2. **Client Configuration**

This section defines the credentials required to authenticate your application with Google's OAuth 2.0 service. Replace the values below with your actual client details.

```yaml
client_config:
  client_id: your_client_id.apps.googleusercontent.com
  client_secret: your_client_secret
  redirect_uris: ['http://localhost:8090/']
  auth_uri: https://accounts.google.com/o/oauth2/auth
  token_uri: https://accounts.google.com/o/oauth2/token
```

- **client_id**: This is the unique identifier for your app provided by Google.
- **client_secret**: This is your app's secret key used for authentication.
- **redirect_uris**: URI that Google's OAuth will use to redirect after authentication. It is common to use `localhost` during development.
- **auth_uri**: The authorization endpoint for Google OAuth (usually left unchanged).
- **token_uri**: The token endpoint for Google OAuth (usually left unchanged).

### 3. **Saving Credentials**

This section tells PyDrive2 whether to save credentials and where to store them. Modify the paths as necessary to match your project directory.

```yaml
save_credentials: True
save_credentials_backend: file
save_credentials_file: /path/to/your/project/credentials/saved_credentials.json
```

- **save_credentials**: Set this to `True` to allow saving OAuth credentials for future use.
- **save_credentials_backend**: Leave as `file` to save credentials locally.
- **save_credentials_file**: Set the path to where you want to save your OAuth credentials. Adjust `/path/to/your/project` to your local project directory.

### 4. **Token Refreshing**

This parameter controls whether PyDrive2 should automatically refresh the OAuth token.

```yaml
get_refresh_token: True
```

- **get_refresh_token**: Leave this set to `True` to enable automatic refresh of the token once it expires.

### 5. **OAuth Scope**

Specify the OAuth scope to define what kind of access the application has to the user's data.

```yaml
oauth_scope:
  - https://www.googleapis.com/auth/drive
```

- **oauth_scope**: This defines the level of access your app will request. The scope `https://www.googleapis.com/auth/drive` gives full access to Google Drive.

## Final Steps

1. Save your `settings.yaml` file in the appropriate location within your project directory.
2. Make sure that your OAuth credentials are properly set up in the Google Cloud Console.
3. Once configured, run your pipeline with Airflow, and the `store.py` module will utilize this file to authenticate and interact with Google Drive.