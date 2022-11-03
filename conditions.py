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

if not p:
    print('not p')

print('-------------')
if p and q:
    print('p and q is True')
else:
    print('p and q is not True')

print('-------------')
if p or q:
    print('p or q is True')
else:
    print('p or q is not True')

print('-------------')
if p ^ q:
    print('p xor q is True')
else:
    print('p xor q is not True')

y = 10 if p else 30
print(f'y={y}')
print('y={}'.format(y))
print('y=' + str(y))

#v = None
v = ''
if v:
    print('v is')
else:
    print('not v')

# t = 10
# tt = t + v
# print(tt)

t = '10sabab'
tt = t + v
print(tt)

w = 12.000
print(type(w))
z = 12
print(type(z))


w = 'agag'
print(type(w))
z = 'agag'
print(type(z))


if w <= z:
    print('w <= z')
else:
    print('w not <= z0')

if w == z:
    print('w = z')
else:
    print('w not = z')

