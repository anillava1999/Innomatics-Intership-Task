import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    # Arrays in Python - Hacker Rank Solution START
    return(numpy.array(arr[::-1], float))
    # Arrays in Python - Hacker Rank Solution END


arr = input().strip().split(' ')
result = arrays(arr)
print(result)