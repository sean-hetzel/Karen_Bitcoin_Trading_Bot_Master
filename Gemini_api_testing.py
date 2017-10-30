import urllib3
base_url = "https://api.gemini.com/v1"
# or, for sandbox
# base_url = "https://api.sandbox.gemini.com/v1"
http = urllib3.PoolManager()
response = http.request("GET", base_url + "/pubticker/btcusd")
#response = base_url + "/pubticker/btcusd"
print(response.read())

