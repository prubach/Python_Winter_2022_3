import _pickle
my_out_file = 'my_matrix_out.dat'
# read binary file
with open(my_out_file, 'rb') as f:
    m = _pickle.load(f)
print(m)
print(type(m[0][2]))