# Re.start() & Re.end() in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Re.start() & Re.end() in Python - Hacker Rank Solution START
import re

S, k = input(), input()
matches = re.finditer(r'(?=(' + k + '))', S)

anymatch = False
for match in matches:
    anymatch = True
    print((match.start(1), match.end(1) - 1))

if anymatch == False:
    print((-1, -1))
# Re.start() & Re.end() in Python - Hacker Rank Solution END