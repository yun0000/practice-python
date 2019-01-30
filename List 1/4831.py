for t in range(int(input())):
    K, N, M = map(int, input().split())
    M = list(map(int, input().split()))
    start = 0
    chance = 0
    end = start+K
    print(M)
    while end<N:
        print("start is", start, "end is", end)
        if end == start:
            print("2")
            chance=0
            break
        elif end in M:
            chance+=1
            start = end
            end = start+K
            
        else:
            print("3", end)
            end-=1
    print('#%d'%(t+1),chance)
