import requests

BASE_URL = "http://localhost:8080/auth"

def signup(email, username, password):
    data = {
        "email": email,
        "username": username,
        "password": password
    }
    response = requests.post(f"{BASE_URL}/signup", json=data)
    print("Signup:", response.status_code, response.json())

def login(email, password):
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{BASE_URL}/login", json=data)
    print("Login:", response.status_code, response.json())
    if response.status_code == 200:
        return response.json().get("jwt")
    return None

def verify_user(email, code):
    data = {
        "email": email,
        "verificationCode": code
    }
    response = requests.post(f"{BASE_URL}/verify", json=data)
    print("Verify:", response.status_code, response.text)

def resend_verification_code(email):
    params = {"email": email}
    response = requests.post(f"{BASE_URL}/resend", params=params)
    print("Resend Verification:", response.status_code, response.text)

if __name__ == "__main__":
    test_email = "vikramadityakhupse@gmail.com"
    test_username = "testuser"
    test_password = "password123"
    signup(test_email, test_username, test_password)
    test_verification_code = input("Verification Code: ")
    verify_user(test_email, test_verification_code)
    token = login(test_email, test_password)
    if token:
        print("JWT Token:", token)
    else:
        print("Login failed")

    verify_user(test_email, test_verification_code)
    resend_verification_code(test_email)
