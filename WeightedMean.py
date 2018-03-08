'''
Sample Input
5
10 40 30 50 20
1 2 3 4 5

Sample Output
32.0
'''


n = int(input())

x = [int(x) for x in input().split()] #elements
w = [int(x) for x in input().split()] #weights

sum_weights = 0
total_sum = 0

for i in range(n):
    sum_weights += w[i]
    total_sum += x[i] * w[i]

weighted_mean = total_sum/sum_weights

print(round(weighted_mean, 1))