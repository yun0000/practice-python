def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range (0, i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]


l = [7, 5, 3, 1, 2]
print(l)
bubbleSort(l)
print(l)
