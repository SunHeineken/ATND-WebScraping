import requests

params = {
'keyword':  'DeepLearning',
'format':   'json'
}

url = 'http://api.atnd.org/events/'

res = requests.get(url, params=params)

# check status code
print(res.status_code)

res.json()