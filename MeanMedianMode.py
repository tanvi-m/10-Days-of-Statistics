'''
Sample Input
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output
43900.6
44627.5
4978 
'''

n = int(input())
a = list(input().split())
a = list(map(int, a))

sum_of_num = 0

# Bubble Sort
for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if a[j] > a[j+1] :
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if swapped == False:
        break
        
# Mean         
for i in range(n):
    sum_of_num += a[i]

mean = sum_of_num/n
print(round(mean,1))

# Median
if n%2 == 0:
    index_1 = n//2 - 1
    index_2 = n//2
    median = (a[index_1] + a[index_2])/2
else:
    median = a[(n-1)//2]

print(round(median,1))

# Mode
counts = dict()
for key in a:
    if key in counts:
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1

mode = None
mode_count = -1

for key in sorted(counts.keys()):
    if mode == None:
        mode = key
        mode_count = counts.get(key, 0)
    elif mode_count < counts.get(key,0):
        mode = key
        mode_count = counts.get(key)

print(mode)