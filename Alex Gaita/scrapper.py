import urllib.request
import json

TWITTER_API = "https://localhost-python-abstraction.glitch.me"


def fetch(username):
    url = TWITTER_API + "/api/tweets/" + username
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request).read()
    decoded_response = response.decode('utf-8')
    data = json.loads(decoded_response)
    return data['data']
print(fetch("elonmusk"))