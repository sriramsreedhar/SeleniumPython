import requests 
url = 'https://trakit.domain.com/legatoppmweb/login.html'
user_agent = 'MSIE'
headers = {'User-Agent': user_agent}

userdata = {"username": "Rag", "password": "passwd"}
resp = requests.post('https://trakit.domain.com/legatoppmweb/login.html', data=userdata, headers=headers)
print(resp.content)
