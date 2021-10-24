# Validating and Parsing Email Addresses in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Validating and Parsing Email Addresses in Python - Hacker Rank Solution START
import re

N = int(input())

for i in range(N):
    name, email = input().split()
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)
# Validating and Parsing Email Addresses in Python - Hacker Rank So