import requests

# Define the login API URL for Reqres
login_url = "https://reqres.in/api/login"

# Test case for valid credentials
def test_valid_login():
    payload = {
        "email": "eve.holt@reqres.in",  # Valid email from Reqres
        "password": "pistol"  # Valid password from Reqres
    }
    response = requests.post(login_url, data=payload)
    if response.status_code == 200:
        print("Valid login test passed.")
        token = response.json().get("token")
        print("Token:", token)
        # Example of using the token for another request
        user_info_url = "https://reqres.in/api/users/2"
        headers = {"Authorization": f"Bearer {token}"}
        user_info_response = requests.get(user_info_url, headers=headers)
        if user_info_response.status_code == 200:
            print("User info fetched successfully.")
        else:
            print("Failed to fetch user info.")
    else:
        print("Valid login test failed. Status code:", response.status_code)

# Test case for invalid credentials
def test_invalid_login():
    payload = {
        "email": "invalid_email@reqres.in",  # Invalid email
        "password": "wrongpassword"  # Invalid password
    }
    response = requests.post(login_url, data=payload)
    if response.status_code == 400:  # 400 for Bad Request when credentials are invalid
        print("Invalid login test passed. Status code:", response.status_code)
    else:
        print("Invalid login test failed. Status code:", response.status_code)

# Test case for missing credentials
def test_missing_credentials():
    payload = {}  # No email or password
    response = requests.post(login_url, data=payload)
    if response.status_code == 400:  # 400 for Bad Request when credentials are missing
        print("Missing credentials test passed. Status code:", response.status_code)
    else:
        print("Missing credentials test failed. Status code:", response.status_code)

# Test case for empty fields
def test_empty_fields():
    payload = {
        "email": "",  # Empty email
        "password": ""  # Empty password
    }
    response = requests.post(login_url, data=payload)
    if response.status_code == 400:  # 400 for Bad Request when fields are empty
        print("Empty fields test passed. Status code:", response.status_code)
    else:
        print("Empty fields test failed. Status code:", response.status_code)

# Run the test cases
if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_missing_credentials()
    test_empty_fields()
