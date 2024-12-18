import requests

# Define API URL and parameters
api_url = "https://www.googleapis.com/youtube/v3/videos"
api_key = ""
params = {
    "part": "snippet",
    "id": "C3misTE2ErA",
    "key": api_key,
}

# Send GET request to the API
response = requests.get(api_url, params=params)

# Check response status and handle data
if response.status_code == 200:
    data = response.json()
    print("API Response:")
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)