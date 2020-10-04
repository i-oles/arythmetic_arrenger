# sorting values from dict to list
d = {'raz' : 1, 'trzy' : 3, 'dwa' : 2}
n_list = d.items()
sorted_keys = sorted(n_list)

# loop through sorted keys
for k, v in sorted_keys:
    print(k,v)

# loop through sorted values

tmp = list()
for k, v in d.items():
    new_tup = (v,k)
    tmp.append(new_tup)

tmp = sorted(tmp, reverse=True)

print(tmp)

# top ten common words from file

counts = {}
fhand = open('test.txt')
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# longer version of this part
st = list()
for k,v in counts.items():
    new_tup = (v,k)
    st.append(new_tup)

st = sorted(st, reverse=True)

# shorter version of this part
st = sorted ( [ (v,k) for k, v in counts.items() ], reverse=True )


for v, k in st[:10]: # after sorting you can take first 10 with largest values because of reverse used before
    print(k,v)


