import certifi
import urllib3
import json

#base_url = "https://api.gemini.com/v1"

base_url = "https://api.sandbox.gemini.com/v1"
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
response = http.request("GET", base_url + "/pubticker/btcusd")
json.loads(response.data.decode("utf-8"))
#response = base_url + "/pubticker/btcusd"
print(response.read())
urllib3.HTTPConnectionPool
