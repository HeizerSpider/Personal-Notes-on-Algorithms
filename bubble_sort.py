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