with open('input.txt', 'r') as file:
    text = file.read()
count=0
end=False
for symb in text:
    if symb == '.!?':
        if not end:
            count+=1
            end=True
    else:
        end=False
print(count)