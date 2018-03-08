'''
Sample Input
9
3 7 8 5 12 14 21 13 

Sample Output
6
12
16
'''


def find_median(a):
    n = len(a)
    if n%2 == 0:
        index_1 = n//2 - 1
        index_2 = n//2
        median = (a[index_1] + a[index_2])/2
    else:
        median = a[(n-1)//2]
    return median

n = int(input())
a = list(input().split())
a = list(map(int, a))

for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if a[j] > a[j+1] :
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if swapped == False:
        break
        
if n%2 == 0:
    q2 = find_median(a)
    q1 = find_median(a[:(n//2)])
    q3 = find_median(a[(n//2):])
else:
    q2 = find_median(a)
    q1 = find_median(a[:(n-1)//2])
    q3 = find_median(a[(n+1)//2:])   

print(int(q1))
print(int(q2))
print(int(q3))