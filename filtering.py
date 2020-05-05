items = ["apple", "kiwi", "orange", "banana", "apple", "kiwi", "orange", "banana", "orange", "orange"]

counter = {} #OR counter = dict()

for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)