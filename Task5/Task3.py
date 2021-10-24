# Group() Groups() Groupdict() in Python - Hacker Rank Solution
# Python 3 
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Group() Groups() Groupdict() in Python - Hacker Rank Solution START
import re

expression=r"([a-zA-Z0-9])\1+"

m = re.search(expression,input())

if m:
    print(m.group(1))
else:
    print(-1)
# Group() Groups() Groupdict() in Python - Hacker Rank Solution END