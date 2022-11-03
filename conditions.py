p = True
q = False
print(type(p))
a = 0
if p:
    a = 9
    print('p is True')
    print('p is still True')
elif q:
    print('p is not True, q is True')
else:
    print('p is not True and q is not True')
print(a)