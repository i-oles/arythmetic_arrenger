import re
"""

^           matches the beginning of a line
$           matches the end of the line
.           matches any character
\s          matches whitespace
\S          matches any non-whitespace character
*           repeats a character zero or more times
*?          repeats a character zero or more times (non-greedy)
+           repeats a character one or more times
+?          repeats a character one or more times (non-greedy)
[aeiou]     matches a single character in the listed set
[^XYZ]      matches a single character not in the listed set
[a-z0-9]    the set of characters include a range
(           indicates where string extraction is to start
)          indicates where string extraction is to start

"""
sentence = ['abrakadabra', '123', '!!']
for line in sentence:
    # re.search returns true or false
    if re.search('^abra', line):
        print('true')

# re.findall match the strings
x = 'i like 5370'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[AEIOU]+', x) # if it will not find anything returns empty string
print(y)






if __name__ == '__main__':
    pass
