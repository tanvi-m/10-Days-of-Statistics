'''
Task 
A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.

Output Format
Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
'''

import math

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

mean = 2.5  #lambda
X = 5

sol = ((mean**X)*math.exp(-mean))/fact(X)

print(round(sol,3))