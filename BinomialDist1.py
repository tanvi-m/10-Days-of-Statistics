'''
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is  child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1234 format).


'''

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

n = 6
#x: 3,4,5,6

pg = 0.4784
pb = 0.5216
res = 0 

for x in range(3,7):
    res += (fact(n)/(fact(n-x)*fact(x))) * (pb**x) * (pg**(n-x))
print(round(res,3))