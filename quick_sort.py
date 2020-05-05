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