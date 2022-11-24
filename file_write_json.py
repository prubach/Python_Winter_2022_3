from file_read_csv import m
import json

my_out_file = 'my_matrix_out.json'
# write binary file
with open(my_out_file, 'w') as f:
    json.dump(m, f)