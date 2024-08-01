import requests

# response = requests.post('http://127.0.0.1:8000/v1/adv/',
#                          json={
#                              "heading": "adv 1",
#                              "description": "jhgfc",
#                                "price": "15",
#                               'user': "user1"
#                          })
# print(response.json())
# print(response.status_code)

# response = requests.patch('http://127.0.0.1:8000/v1/adv/1/',
#                           json={"heading": "adv 2"}
#                           )
# print(response.json())
# print(response.status_code)

# response = requests.delete('http://127.0.0.1:8000/v1/adv/1/',)
# print(response.json())
# print(response.status_code)
#
#
# response = requests.get('http://127.0.0.1:8000/v1/adv/1/',)
# print(response.json())
# print(response.status_code)
#
response = requests.get('http://127.0.0.1:8000/v1/adv?param1=1',)
print(response.json())
print(response.status_code)

