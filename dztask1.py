#проверка на палиндром
def pal(s):
    return s==s[::-1]

#ввожу словарь + проверка на наличие символа в словаре
def mirror_symbol(p):
    dict={'U':'U','A':'A','M':'M','V':'V','W':'W','T':'T','X':'X','Y':'Y','H':'H','I':'I','O':'O','S':'2','Z':'5','5':'Z','2':'S','1':'1','8':'8','E':'3','3':'E','L':'J','J':'L'}
    return dict.get(p, None)

def mirrored(s):
    listsymb=[]
    for symb in s:
        msymb=mirror_symbol(symb)
        if msymb==None:
            return False
        listsymb.append(msymb)
    return s==''.join(listsymb[::-1])

#условия вывода
def check_string(s):
    a=pal(s)
    b=mirrored(s)
    if not a and not b:
        return f"{s} is not a palindrome."
    elif not a and b:
        return f"{s} is a mirrored string."
    elif not b and a:
        return f"{s} is a regular palindrome."
    else:
        return f"{s} is mirrored a palindrome."

#основной код
print(check_string(input()))#вставьте свой вариант