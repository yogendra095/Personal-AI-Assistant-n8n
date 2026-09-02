import requests
import os


URL= os.getenv("URL")
print(URL)


# json_message={"message":message}

# response= requests.post(URL,json=json_message)

# print(response.json()[0]['output'])