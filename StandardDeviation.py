'''
Sample Input
5
10 40 30 50 20

Sample Output
14.1
'''

n = int(input())
x = list(map(int, input().split()))

tot = 0

for i in range(n):
    tot += x[i]

mean = tot/n

tot_sd = 0

for i in range(n):
    x[i] -= mean
    x[i] = x[i] * x[i]
    tot_sd += x[i]
    
tot_sd /= n

sd = tot_sd **(1/2.0)

print(round(sd,1))