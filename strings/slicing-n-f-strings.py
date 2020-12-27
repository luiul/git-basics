# import sys
# print(sys.version)

# --- Slicing Lists --- #
# my_list = list(range(0,10,1))
# print(my_list[::-1 ])

# --- Slicing Strings --- #
# sample_url = 'https://google.com'
# print(sample_url)
# reverse the url
# print(sample_url[::-1])
# get the top level domain
# print(sample_url[-4:])
# get the url without the https://
# print(sample_url[8:])
# get the url without the https:// or the top level domain
# note that regex is prob a better alternative for this task
# print(sample_url[8:-4])

# --- F-Strings --- #
# first_name = 'Albert'
# last_name = 'Einstein'
# Example 1: format method vs f-string: formatting # 
# the curly braces are placeholder (see string formatting; https://www.youtube.com/watch?v=vTX3IwquFkc)
# sentence = 'My name is {} {}'.format(first_name,last_name)
# print(sentence)

# sentence = f'My name is {first_name.upper()} {last_name.upper()}'
# print(sentence)

# Example 2: format method vs f-string: dictionaries# 
# person = {'name':'Albert','age':'23'}

# sentence = 'My name is {} and I am {} years old'.format(person['name'],person['age'])
# print(sentence)

# sentence = f"My name is {person['name']} and I am {person['age']} years old"
# print(sentence)

# Example 3: format method vs f-string: calculations # 
# calculation = f'4 times 11 is equal to {4*11}'
# print(calculation)

# for i in range(1,11):
#     sentence = f'the value is {i}'
#     print(sentence)

# we can also zero pad the values if neccesary (https://stackoverflow.com/questions/339007/how-to-pad-zeroes-to-a-string)
# for i in range(1,11):
#     sentence = f'the value is {i:02}'
#     print(sentence)

# Example 4: format method vs f-string: floating point values # 
# import numpy as np

# sentence = f'Pi is equal to {np.pi:.4f}'
# print(sentence)

# Example 4: format method vs f-string: dates # 
from datetime import datetime

bd = datetime(1990,1,1)
sentence = f'Albert has a birthday on {bd:%B %d, %Y}'
print(sentence)