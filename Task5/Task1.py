# Detect Floating Point Number in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Detect Floating Point Number in Python - Hacker Rank Solution START
import re

class Main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
                    
if __name__ == '__main__':
    obj = Main()
# Detect Floating Point Number in Python - Hacker Rank Solution END