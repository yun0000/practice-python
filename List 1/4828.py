T = int(input())
results = []

for test_case in range(1, T + 1):
    number = int(input())
    inputList = input()
    caseList = list(map(int, inputList.split()))
    biggest = caseList[0]
    smallest = caseList[0]
    for each in caseList:
        if each < smallest:
            smallest = each
        if each > biggest:
            biggest = each
    results.append(biggest-smallest)
    
for i in range(0, T):
    print('#%d'%(i+1),results[i])
