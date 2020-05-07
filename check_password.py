import requests
import hashlib
import sys

# API uses SHA1 hash function to secure password so that
# clear text password is not sent to API

# Check hashes that have only five first hash digits same
# the password.


# Function for hashing the password as expected by API


def hash_password(password):
    hashed_pass = hashlib.sha1(password.encode("utf-8")).hexdigest()
    checked_pass = hashed_pass[:5].upper()
    tail_pass = hashed_pass[5:].upper()
    return checked_pass, tail_pass

# Obtain the list of hashes of which 5 first values are same as password


def check_password_api(checked_pass):
    url = "https://api.pwnedpasswords.com/range/" + checked_pass
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error {res.status_code}, check the request.')
    else:
        results = res.text

    hashes = (line.split(":") for line in results.splitlines())
    return hashes

# Check if the password has been records of being compromised


def check_for_compromise(hashes, tail_pass):
    for hash, count in hashes:
        if hash == tail_pass:
            return count
    return 0

# Putting it all together to run it against multiple passwords


def main():

    with open("passwords.txt") as password_file:
        passwords = password_file.read().splitlines()

        for password in passwords:
            checked_pass, tail_pass = hash_password(password)
            hashes = check_password_api(checked_pass)
            count = int(check_for_compromise(hashes, tail_pass))
            console_pass = password[:3] + "*****"

            if count > 0:
                print(
                    f"The password {console_pass} was compromised {count} times!")
            else:
                print("No compromise detected.")

# EXECUTE


if __name__ == "__main__":
    main()
