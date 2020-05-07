## Check Your Passwords Before Using Them!

check_password.py uses "have i been pwned" API to check whether your password(s) has been leaked before. Use this tool to verify your password before committing to it. The passwords you want to validate are kept in "passwords.txt" file. 

Only first five digits of the hashed password is sent to the API, which returns matching tails of the hashes. This way you don't share the full hash of your password over the nets. The script keeps your passwords local and does the compromise check also locally based on the tail values returned by the API.

The script has been written on Python 3.7.

Example: 
```
python check_password.py
```
