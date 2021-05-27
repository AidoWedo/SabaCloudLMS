import requests
from requests.exceptions import HTTPError

payload = ""
headers = {
    'Content-Type': 'application/json',
    'user': 'Your_username',
    'password': 'Your_Password'
}
try:
    response = requests.get("https://your_host_name.sabacloud.com/v1/login", headers=headers, data=payload)
    response.raise_for_status()
    # access Json content
    jsonResponse = response.json()

    print("Entire JSON response")
    print(jsonResponse)
    print("Print each key-value pair from JSON response")
    for key, value in jsonResponse.items():
        print(key, ":", value)
    print("Certificate is ")
    print(jsonResponse['certificate'])
    sabacertificate = (jsonResponse['certificate'])
    print("Dict item for sabacertificate is")
    print(sabacertificate)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

# Class Retrieval post certificate

params = {
    'type': 'web-based',
    'count': '10',
    'startPage': '1',
    'SabaCertificate': '' + str(sabacertificate)
}
headers = {
    'Content-Type': 'application/json'
}
try:
    r = requests.get('https://your_host_name.sabacloud.com/v1/offering', params=params)
    # access Json content
    print(r.url)
    jsonResponseclass = r.json()
    print("Entire JSON Class response")
    print(jsonResponseclass)
    print("Print each key-value pair from JSON response for classes")
    for key, value in jsonResponseclass.items():
        print(key, ":", value)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
