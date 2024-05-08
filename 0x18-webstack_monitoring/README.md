# Datadog Monitoring Setup for web-01

This README provides instructions for setting up Datadog monitoring on the `web-01` server. It covers the steps for logging into an existing Datadog account, installing the Datadog agent, and configuring the server for monitoring.

## Prerequisites

- Access to an existing Datadog account.
- Server `web-01` should have internet access and permission to install software.

## 1. Log In to Datadog

Ensure you're logged into the Datadog US1 region. Use the following link to access your account:

[Datadog Login](https://app.datadoghq.com)

## 2. Install the Datadog Agent

If the Datadog agent is not yet installed on `web-01`, run the following command:

```bash
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=your_existing_api_key DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"
