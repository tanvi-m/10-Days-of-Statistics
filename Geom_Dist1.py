'''
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?
'''

p_def = 1/3
n = 5

p = ((1-p_def)**(n-1)) * p_def

print(round(p,3))