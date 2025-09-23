N=int(input())
a=list(map(int,input().split()))
for i in range(N):
    less_count=0
    more_count=0
    for j in range(N):
        if a[j]<a[i]:
            less_count+=1
        elif a[j]>a[i]:
            more_count+=1
    if less_count==more_count:
        print(a[i])
        break