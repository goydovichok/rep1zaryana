with open('input.txt','r') as file:
    text=file.read()
letters='уеоаыяиюэё'
x=0
ret=[]
while x<len(text):
    if text[x] in letters:
        if x==0:
            prev=True
        else:
            prev=text[x-1] not in letters
        if x==len(text)-1:
            next=True
        else:
            next=text[x+1] not in letters
        if prev and next:
            ret.append('c'+text[x])
    x+=1
print(' '.join(ret))