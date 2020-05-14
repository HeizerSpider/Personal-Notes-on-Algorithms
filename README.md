# Personal-Notes-on-Algorithms

Compilation of notes for Basic Algorithms (SUTD curriculum), adapted from various sources: [Introduction to Algorithms notes](https://github.com/HeizerSpider/Personal-Notes-on-Algorithms/blob/master/SUTD_notes/Algo_notes.md)

Here's a compilation of python codes for the different algorithms:

1) Bubble sort
2) Merge sort
3) Quick sort
4) Binary Search
5) Filtering
6) Greatest common divisor
7) Insertion sort
8) Heap sort
9) Couting sort
10) Radix sort
11) Bucket sort

1) Bubble sort
```
from random import randint

def bubble(list):
    length = len(list)
    while length>2:
        for i in range(0, length-1):
            if list[i]>list[i+1]:
                buffer  = list[i]
                list[i] = list[i+1]
                list[i+1] = buffer
        length-=1
    return list

def make_list(length):
    list = []
    for i in range(0,length):
        num = randint(0, 1000)
        list.append(num)
    return list
        

list = make_list(100)
# list = [10, 3, 4, 1, 6, 9, 5]
print(list)
print(bubble(list))
```

2) Merge sort
```
def merge_sort(data):
    if len(data)>1:
        mid = len(data)//2
        leftarray = data[:mid]
        rightarray = data[mid:]

        merge_sort(leftarray)
        merge_sort(rightarray)

        i = 0
        j = 0
        k = 0

        while i<len(leftarray) and j<len(rightarray):
            if leftarray[i]<rightarray[j]:
                data[k] = leftarray[i]
                i+=1
                k+=1
            else:
                data[k]=rightarray[j]
                k+=1
                j+=1
        
        while i<len(leftarray):
            data[k] = leftarray[i]
            k+=1
            i+=1

        while j<len(rightarray):
            data[k] = rightarray[j]
            k+=1
            j+=1


list = [4 ,1, 5, 34, 1, 56]
print(list)
merge_sort(list)
print(list)
```

3) Quick sort
```
from random import randint

def quicksort(dataset, first, last):
    if first<last:
        pivotIdx= partition(dataset, first, last)
        quicksort(dataset, first, pivotIdx-1)
        quicksort(dataset, pivotIdx+1, last)

def partition(datavalues, first, last):
    pivotvalue = datavalues[first]
    lower = first + 1
    upper = last
    done = False

    #finding the split point
    while not done:
        #advance the lower index
        while lower <= upper and datavalues[lower] <=pivotvalue:
            lower+=1

        #advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        #index found when upper and lower index crosses each other
        if upper < lower:
            done = True
        else:
            #else we would exchange the upper and lower index
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    #split point found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    #return split point index
    return upper

def make_list(length):
    list = []
    for i in range(0,length):
        num = randint(0, 1000)
        list.append(num)
    return list
        

list = make_list(100)
# list = [10, 3, 4, 1, 6, 9, 5]
print(list)
quicksort(list, 0 , len(list)-1)
print(list)
```

4) Binary search
```
def binarySearch(item, itemList):
    listsize = len(itemList)-1

    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:

        midPt = (upperIdx+lowerIdx) // 2

        if itemList[midPt] == item:
            return midPt

        if item > itemList[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None





#ordered list
list = [1, 11, 20, 29, 46, 53, 64, 77, 81, 84, 84, 86, 95, 103, 106, 139, 141, 143, 158, 158, 164, 176, 176, 205, 244, 246, 264, 284, 291, 302, 304, 311, 311, 317, 327, 335, 349, 352, 364, 369, 369, 390, 398, 400, 405, 441, 463, 486, 504, 506, 514, 520, 521, 542, 589, 592, 612, 619, 631, 632, 633, 637, 642, 642, 654, 699, 705, 712, 723, 728, 728, 743, 748, 756, 777, 812, 815, 829, 842, 865, 865, 880, 882, 888, 896, 903, 921, 941, 942, 951, 962, 965, 970, 980, 986, 992, 992, 994, 997, 999]
print(binarySearch(103, list))
```

5) Filtering
```
items = ["apple", "kiwi", "orange", "banana", "apple", "kiwi", "orange", "banana", "orange", "orange"]

counter = {} #OR counter = dict()

for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)
```

6) Greatest common divisor
```
def gcd(a, b):
    while b!=0:
        buffer = a
        a = b
        b = buffer%b
    return a



print(gcd(11,10))
print(gcd(20,8))
```