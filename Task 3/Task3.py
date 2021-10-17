


'''
Therefore, .
Point  is the midpoint of hypotenuse .
You are given the lengths  and . 
Your task is to find  (angle , as shown in the figure) in degrees.
Input Format
The first line contains the length of side .
The second line contains the length of side .
Constraints


Lengths  and  are natural numbers.
Output Format
Output  in degrees. 
Note: Round the angle to the nearest integer.
Examples: 
If angle is 56.5000001°, then output 57°. 
If angle is 56.5000000°, then output 57°. 
If angle is 56.4999999°, then output 56°.

Sample Input
10
10
Sample Output
45°

'''




# Enter your code here. Read input from STDIN. Print output to STDOUT
# Find Angle MBC in python - Hacker Rank Solution START
# -*- coding: UTF-8 -*-

import math
import sys
l1 = float(input())
l2 = float(input())
a = math.degrees(math.atan(l1/l2))
a = round(a)
print ("%.0f" % a,)
sys.stdout.softspace=0
print(u"\u00b0".encode('utf-8'))