

def sum(a=20, b=10):
    return a + b

c = 5
d = 8

print(f'sum(c,d)={sum(c, d)}')
print(f'sum(c,d)={sum(c)}')
print(f'sum(c,d)={sum()}')
print(f'sum(c,d)={sum(b=d)}')
print(f'sum(c,d)={sum(a=c, b=d)}')