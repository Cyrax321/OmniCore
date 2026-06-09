import urllib.request
import json
import urllib.error

url = "https://pypi.org/pypi/pyttsx3/json"
req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.64.1'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print("Success! Version:", data['info']['version'])
except urllib.error.URLError as e:
    print("Failed:", e)
