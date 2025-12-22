import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "sisdkjfhfhjsdkjfsdsf"
USER_NAME = "ganeshawh"
GRAPH_ID = "graph1"

#creating an user account using post method

user_parameters = {
    "token" : TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

#creating an graph for new user
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Gym Graph",
    "unit" : "Kg",
    "type" : "int",
    "color" : "ajisai"
}
gheader = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=gheader)

# today = datetime.now()
today = datetime.now()


post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilograms you lift today? "),
}

response = requests.post(post_pixel_endpoint, json=pixel_data, headers=gheader)

#put request -> used to update any data

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "1300",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=gheader)

#delete request
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=gheader)
# print(response.text)