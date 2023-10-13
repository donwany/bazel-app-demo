import requests

headers = {"Authorization": "Bearer dhfdjfhdjfdjfdfd"}
response = requests.get("http://localhost:1957/hello", headers=headers)

if __name__ == '__main__':
    print(response.json())
