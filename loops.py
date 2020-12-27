import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nums2 = range(1,6)
nums2 = [2,5,7]
# does the same as nums = [1,2,3,4,5]

beta = [ 3.07615033e-07, -1.89392449e-04,  8.20886302e-02,  2.70495053e+00]

# iterate over the VALUES in the list
for num in nums2:
    print(num)

print('\n')

for num in nums2:
    if num == 3:
        print("Found 3's position!")
        break
    print(num)

print('\n')

for num in nums2:
    if num == 3:
        print("Found 3's position!")
        continue
    print(num)

print('\n')

for num in nums2:
    for letter in 'abc': 
        print(num,letter)

print('\n')

total = 0

for num in [2,5,7]: 
    total += num
    print(total)

print('\n')

# do we need the index of the item or the item itself (value)? 

# pot_spend = np.linspace(0,500,101)

# beta3 = [ 3.07615033e-07, -1.89392449e-04,  8.20886302e-02,  2.70495053e+00]

# pred_sales3 = np.zeros(len(pot_spend))

# for i in range(len(beta3)): 
#     pred_sales3 += beta3[i]*pot_spend**(3-i)

# plt.plot(pot_spend, pred_sales3) 