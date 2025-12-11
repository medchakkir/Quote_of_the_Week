import os
import smtplib
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables
api_key = os.getenv("API_KEY")
api_endpoint = os.getenv("API_ENDPOINT")
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")


# Validate that all required environment variables
required_vars = {
    "API_KEY": api_key,
    "API_ENDPOINT": api_endpoint,
    "SENDER_EMAIL": sender_email,
    "RECEIVER_EMAIL": receiver_email,
    "SENDER_PASSWORD": sender_password,
}

missing_vars = [var for var, value in required_vars.items() if value is None]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Headers
headers = {
    "X-Api-Key": api_key
}

# Fetch quotes from API
try:
    response = requests.get(url=api_endpoint, headers=headers, timeout=10)
    response.raise_for_status()
    quote_data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching quotes from API: {e}")
    exit(1)
except ValueError as e:
    print(f"Error parsing JSON response: {e}")
    exit(1)

# Print quote
quote = quote_data[0]["quote"]
author = quote_data[0]["author"]
print(f"{quote} - {author}")

# Send Email
try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email, 
            to_addrs=receiver_email, 
            msg=f"Subject: Quote of the Day\n\n{quote} - {author}"
        )
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP authentication failed: {e}")
    exit(1)
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
    exit(1)
except Exception as e:
    print(f"Unexpected error sending email: {e}")
    exit(1)