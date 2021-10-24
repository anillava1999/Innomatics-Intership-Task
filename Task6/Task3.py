# Transpose and Flatten in Python - Hacker Rank Solution
# Python 3
# Transpose and Flatten in Python - Hacker Rank Solution START
import numpy
n, m = map(int, input().split())

storage = numpy.array([input().strip().split() for _ in range(n)], int)
print (storage.transpose())
print (storage.flatten())
# Transpose and Flatten in Python - Hacker Rank Solution