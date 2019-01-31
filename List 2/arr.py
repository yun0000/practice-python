n, m = map(int, input().split())

mylist = [0]*n
for i in range(n):
    mylist[i] = list(map(int, input().split()))
print(mylist)
