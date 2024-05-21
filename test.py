import requests
print("Hello world")
url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for user in data:
        print("User: %s,\tEmail: %s\tCity : %s" % (user['name'], user['email'], user['address']['city']))
else:
    print("Failed fuck you")
