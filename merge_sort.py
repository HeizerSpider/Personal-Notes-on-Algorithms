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

print(list[:2])
print(list[2:])