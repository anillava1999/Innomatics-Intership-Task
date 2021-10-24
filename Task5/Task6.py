# Regex Substitution in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Regex Substitution in Python - Hacker Rank Solution START
import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

for _ in range(int(input())):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change,input()))
# Regex Substitution in Python - Hacker Rank Solution END