a=list(map(int,input().split()))
print(' '.join(map(str,a[-1:]+a[:-1])))