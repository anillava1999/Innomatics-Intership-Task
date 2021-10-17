 #Find Angle MBC in python - Hacker Rank Solution 
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Find Angle MBC in python - Hacker Rank Solution START
import math

AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)
H = H/2.0
adj = BC/2.0

Output = int(round(math.degrees(math.acos(adj/H))))

Output = str(Output)

print(Output+"°")
# Find Angle MBC in python - Hacker Rank Solution END