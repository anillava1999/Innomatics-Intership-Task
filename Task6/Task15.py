# Linear Algebra in Python - Hacker Rank Solution
# Python 3
# Linear Algebra in Python - Hacker Rank Solution START
import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
print(round(numpy.linalg.det(A),2))
# Linear Algebra in Python - Hacker Rank Solution END