import http.client

conn = http.client.HTTPSConnection("twitter154.p.rapidapi.com")

payload = "{\"username\":\"some_user\",\"include_replies\":false}"

headers = {
    'x-rapidapi-key': "<YOUR_RAPIDAPI_KEY>",
    'x-rapidapi-host': "twitter154.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/user/tweets", payload, headers)
res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))