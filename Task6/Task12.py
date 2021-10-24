# Dot and Cross in Python - Hacker Rank Solution
# Python 3
# Dot and Cross in Python - Hacker Rank Solution START
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))
# Dot and Cross in Python - Hacker Rank Solution END