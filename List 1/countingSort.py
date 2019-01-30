def countingSort(data, sortedData, k):
    counts = [0]*k
    for i in range(0, len(data)):
        counts[data[i]]+=1
        
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
        
    for i in range(len(data)-1, -1, -1):
        sortedData[counts[data[i]]-1] = data[i]
        counts[data[i]] -= 1
        
    


l = [7, 5, 3, 1, 2]
sort = [0]*len(l)                          
print(l)
countingSort(l, sort, 8)
print(sort)
