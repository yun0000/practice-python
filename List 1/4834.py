for t in range(int(input())):
    N = int(input())
    list_a=list(map(int, input()))
    list_number=[0]*10
    for a in list_a:
        list_number[a]+=1

    if list_number.count(max(list_number)) != 1:
        list_number.reverse()
        index = 9-list_number.index(max(list_number))
    else:
        index = list_number.index(max(list_number))

        
    print("#"+str(t+1),index, max(list_number))
