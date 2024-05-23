import requests

# Example HTTPS GET request
response = requests.get("https://example.com/data", verify=True)  # Verify SSL/TLS certificate
print(response.text)