import itertools

# Dummy login simulation
def check_login(username, password):
    return username == "admin" and password == "1234"

def run():
    print("[*] Starting brute force simulation...")
    username = input("Enter target username: ")
    wordlist = ["123", "1234", "admin", "pass", "root", "password"]

    for pwd in wordlist:
        print(f"Trying: {pwd}")
        if check_login(username, pwd):
            print(f"[+] Password found: {pwd}")
            return
    print("[-] Password not found in wordlist.")
