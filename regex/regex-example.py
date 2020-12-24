import re

print('Program starts here:')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

# grab everything but bat with [^b]at # 
cat
mat
pat
bat

300-555-4321
321-555-4321
123.555.1234
123*555*1234

800-555-1234
900-555-1234

# grab all the misters with Mr\.?\s[A-Z]\w* #
# grab all the misses with M(s|rs)\.?\s[A-Z]\w* #
# grab all names with M(r|s|rs)\.?\s[A-Z]\w* #
 
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# \t prints out a tab
print('\tTab')

# this passes a raw string that bypasses python's meta-characters
print(r'\tTab')

# 'abc' is our pattern we want to search
pattern = re.compile(r'abc')

# creates an iterator that contains all of the matches
matches = pattern.finditer(text_to_search)

# this prints Match objects with span and match
# span is the beginning and end index of the match
for match in matches:
    print(match)

# we can slice the text with the help of the span returned in the Match object 
print(text_to_search[1:4])