for t in range(int(input())):
    N, M = map(int, input().split())
    list_n=list(map(int, input().split()))
    list_result = [0]*(N-M-1)
    largest = 0
    for i in range(0, M):
        largest += list_n[i]
    smallest = largest
    for i in range(0, N-M+1):
        current = 0
        for j in range(i, i+M):
            current += list_n[j]       
        if current < smallest:
            smallest = current
        if current > largest:
            largest = current            

    print("#"+str(t+1),largest-smallest)
