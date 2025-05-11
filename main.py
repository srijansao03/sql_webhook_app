import requests
import json

# User information
payload = {
    "name": "John Doe",
    "regNo": "REG12347",
    "email": "john@example.com"
}

# API URL to generate webhook
generate_webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

try:
    # Step 1: Send POST request to generate webhook
    response = requests.post(generate_webhook_url, json=payload)
    response.raise_for_status()
    
    data = response.json()
    webhook_url = data.get("webhook")
    access_token = data.get("accessToken")

    if not webhook_url or not access_token:
        raise ValueError("Missing webhook URL or access token in response.")

    print("Webhook URL:", webhook_url)
    print("Access Token:", access_token)

    # Step 2: Provide the SQL query here after solving
    with open("sql_solution.sql", "r") as f:
        sql_query = f.read().strip()

    # Step 3: Send SQL query to webhook
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    final_payload = {
        "finalQuery": sql_query
    }

    submit_response = requests.post(webhook_url, headers=headers, json=final_payload)
    submit_response.raise_for_status()

    print("Solution submitted successfully!")

except Exception as e:
    print(f"Error occurred: {e}")
