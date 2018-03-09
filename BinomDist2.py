'''
Objective 
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task 
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?
'''


def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

p_rej = 0.12
p_nrej = 0.88
n = 10

#No more than 2 rejects?  0,1,2 rejects
res = 0
for x in range(0,3):
    res += (fact(n)/(fact(n-x)*fact(x))) * (p_rej**x) * (p_nrej**(n-x))
print(round(res,3))

#At least 2 rejects? 2....10
res = 0
for x in range(2,11):
    res += (fact(n)/(fact(n-x)*fact(x))) * (p_rej**x) * (p_nrej**(n-x))
print(round(res,3))