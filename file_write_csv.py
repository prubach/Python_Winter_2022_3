from file_read_csv import m
print(m)

my_out_file = 'my_matrix_out.csv'
with open(my_out_file, 'w') as f:
    for r in m:
        print(r)
        cells = [str(i) for i in r]
        print(cells)
        f.write('\t'.join(cells) + '\n')
