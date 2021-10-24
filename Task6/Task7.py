# Array Mathematics in Python - Hacker Rank Solution
# Python 3
# Array Mathematics in Python - Hacker Rank Solution START
import numpy

N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
# Array Mathematics in Python - Hacker Rank Solution END