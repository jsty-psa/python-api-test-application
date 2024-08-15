import time, requests

def test_api(endpoint, loop):
    response = requests.get(f"{endpoint}/api/get_authorization")

    authorization = ""
    username = password = "username"


    if response.status_code == 200:
        authorization = response.json().get("Authorization")
        print(f"Authorization: {authorization}\n")

        headers = {
            "Authorization": "Bearer " + authorization,
            "Content-Type": "application/json"
        }

        data = {
            "username": username,
            "password": password
        }

        print(f"Headers: {headers}\n")
        print(f"Body: {data}\n")

        response = requests.get(f"{endpoint}/api/authenticate", headers = headers, json = data)

        if response.status_code == 200:
            print(f"Result: {response.json()}")
        else:
            print(f"Error: {response.status_code}")

    else:
        print(f"Error: {response.status_code}")
    

    if(loop):
        print("\n")
        time.sleep(3)
        test_api(loop)

input = input("Is the Authentication API having a loop (Y/N)? ")

test_api("http://localhost", True if input == "y" or input == "Y" else False)