import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# returns Match objects
# matches = pattern.finditer(urls)

# return the matches as a list of groups; if there are no groups as a list of strings
matches = pattern.findall(urls)

# we print the Match object
for match in matches:
    print(match)

# the Match object has a group-method and we pass the  index of the group we want to see and clean up the URLs
# group 2 is our domain name
# group 3 is our top level domain
# for match in matches:
#     print(match.group(0))

# we can substitute by group
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)

sentence = 'Start a sentence and then bring it to an end'

# === CASE 1 === #
pattern = re.compile(r'Start')
# returns the first match at the beginning of a string as a Match object
matches = pattern.match(sentence)
print(matches)

# === CASE 2 === #
pattern = re.compile(r'sentence')
# returns the first match in a string as a Match object
matches = pattern.search(sentence)
print(matches)

# === CASE 3 === #
pattern = re.compile(r'start',re.IGNORECASE)
# returns the first match in a string as a Match object; in this example we use the ignore case flag
# I is alias for IGNORECASE
matches = pattern.search(sentence)
print(matches)

