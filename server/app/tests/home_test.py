import requests

test_auth = {
            'email':'limzhichao88@gmail.com',
            'password' : 'Abc123!'
            }

test_user = {
            'username' : 'lzc88',
            'email' : 'limzhichao88@gmail.com',
            'password' : 'Abc123!',
            'pin' : '123456'
            }

test_kid = {
            'email' : 'limzhichao88@gmail.com',
            'name' : 'ching kwun hei',
            'age' : '23',
            'school' : 'NUS'
            }

root = "http://127.0.0.1:8000/home/"

# authentication
user_auth = requests.get(root+"auth", json=test_auth)
print(f"(1) {user_auth}")
print(f"(1) Content: {user_auth.json()}")

# create user
user_create = requests.post(root+"user_create", json=test_user)
print(f"(2) {user_create}")
print(f"(2) Content: {user_create.json()}")

# get kids
user_kids = requests.get(root+"user_getkids/limzhichao88@gmail.com")
print(f"(3) {user_kids}")
print(f"(3) Content: {user_kids.json()}")

# add kid
user_addkid = requests.post(root+"user_addkid", json=test_kid)
print(f"(4) {user_addkid}")
print(f"(4) Content: {user_addkid.json()}")