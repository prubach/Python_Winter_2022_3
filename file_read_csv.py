my_file = 'my_matrix.csv'

m = []
with open(my_file, 'r') as f:
    i = 0
    while line:=f.readline():
        r = []
        i += 1
        print(f'{i}: {line}', end='')
        for c in line.split(';'):
            print(c)
            r.append(int(c))
            #print(type(c))
        m.append(r)

print(m)
print(type(m[0][1]))
