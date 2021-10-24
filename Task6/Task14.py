
# Polynomials in Python - Hacker Rank Solution
# Python 3
# Polynomials in Python - Hacker Rank Solution START
import numpy

poly = [float(x) for x in input().split()]
x = float(input())

print(numpy.polyval(poly, x))
# Polynomials in Python - Hacker Rank Solution END