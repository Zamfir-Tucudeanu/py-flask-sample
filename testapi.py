import requests

baseurl = "http://127.0.0.1:5000/"

# get
response = requests.get(baseurl + "os")
print('+++++++++++++')
print("method == GET")
print('++++++++++++++++++++++++++++++++++++++')
print(response.json())
print('++++++++++++++++++++++++++++++++++++++')

print("")

# post
response = requests.post(baseurl + "mem")
print('++++++++++++++')
print("method == POST")
print('++++++++++++++++++++++++++++++++++++++')
print(response.json())
print('++++++++++++++++++++++++++++++++++++++')
