## Check Your Passwords Before Using Them!

check_password.py uses "have i been pwned" API to check whether your password(s) has been leaked before. Use this tool to verify your password before committing to it. 

Only first five digits of the hashed password is sent to the API, which returns matching tails of the hashes. This way you don't share the full hash of your password over the nets. The script keeps your passwords local and does the compromise check also locally based on the tail values returned by the API.

The script has been written on Python 3.7.

Use: python check_password.py admin admin123 secret ... password
