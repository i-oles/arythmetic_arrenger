
new_dict = {'kaja': 'oles', 'igor': 'oles', 'ewel': 'pankowska'}

print(list(new_dict))
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())

# double var loop
for name, surname in new_dict.items():
    print(name, surname)

"""
handle = open(test.txt)
counts = dict()
words = handle.split()
for word in words:
    counts[word] = count.get(word, 0) + 1

bigcount = None
bigword = None
for count
if bigcount == None or


# counting values in dictionary

my_dict = {}
names = ['kaja', 'igor', 'ewel']

# method 1

for name in names:
    if name not in my_dict:
        my_dict[name] = 1
    else:
        my_dict[name] = my_dict[name] + 1
        
print(my_dict)

# method 2

for name in names:
    my_dict[name] = my_dict.get(name, 0) + 1

print(my_dict)
"""
counting_words = {}
line = """In a sign sign of the severity of the backlash, House Speaker Nancy Pelosi had summoned lawmakers back from their annual summer recess to vote on legislation put forward by House Democrats that would revoke policy changes until Jan. 1, 2021, or the end of the pandemic, as well as include $25 billion in funding for the beleaguered agency"""

words_from_line = line.split()
print(words_from_line)
print("counting...")

# method get will check if word is in dict, and if not it will add an default value to it (0), we want to add 1 instead of 0
for word in words_from_line:
    counting_words[word] = counting_words.get(word, 0) + 1

print(counting_words)