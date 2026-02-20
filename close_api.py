import requests

API_KEY = "api_4e5ISkHfBFELWJ8A9wuWj9.4sqWuRlhAtPn6gBGoq9STX"

response = requests.get("https://api.close.com/api/v1/lead/",
 auth =(API_KEY, ""))

print("Status Code:", response.status_code)
print("Response:", response.json())