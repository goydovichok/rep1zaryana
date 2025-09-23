a=list(map(int,input().split()))
max_count=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[j]==a[i]:
            count+=1
        if count>max_count:
            max_count=count
            max=a[i]
print(max)