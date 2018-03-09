'''
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspections?
'''
p_def = 1/3
n = 5
p=0
for i in range(1,6):
    p += ((1-p_def)**(i-1)) * p_def

print(round(p,3))