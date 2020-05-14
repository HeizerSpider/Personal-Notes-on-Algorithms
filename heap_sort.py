#let i be the index of current value

def parent(i):
    return i//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(arr, n, i):
    #objective: compare parent node with right and left child nodes and swap parent if it is not largest to get a max heap
    l = left(i)
    r = right(i)

    #compare left side child to parent
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    
    #compare right side child with updated 'parent'/largest, if yes then change to largest else no need to do anything
    if r < n and arr[r] > arr[largest]:
        largest = r

    #if there is a change in 'largest' ie child node found to be bigger than parent, do the actual swap in the array
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): #why n//2-1? It's because the value is the number of parent nodes with actual child nodes to max-heapify
        max_heapify(arr, n, i)
  
    # One by one extract elements, rearranging them first by doing a swap (biggest number goes to next last position in array, max heap at the root node and loop)
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        max_heapify(arr, i, 0) 


arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i])