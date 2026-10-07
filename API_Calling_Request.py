import requests

url = "https://api.github.com/users/octocat"
try:
  r = requests.get(url, timeout=10)
  r.raise_for_status()
  user = r.json()
  print(user)
  print(user["name"], user["public_repos"])
except requests.Timeout:
  print("Request timed out")
except requests.HTTPError as e:
  print(f"HTTP error: {e.response.status_code}")
