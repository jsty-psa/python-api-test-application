import time, requests

def test_api(endpoint, loop):

    time_start = time.perf_counter()

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
            print(f"Result: {response.json()}\n")
        else:
            print(f"Error: {response.status_code}\n")

    else:
        print(f"Error: {response.status_code} \n")
    
    time_stop = time.perf_counter()

    print(f"Time Lapsed: {time_stop - time_start:0.3f} Seconds")

    if(loop):
        print("\n")
        time.sleep(3)
        test_api(endpoint, loop)

input = input("Is the Authentication API having a loop (Y/N)? ")

test_api("http://localhost", True if input == "y" or input == "Y" else False)