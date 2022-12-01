import os

my_file = r'__my_matrix.csv'

if os.path.exists(my_file):
    print(f'File {my_file} exists')
else:
    print(f'File {my_file} does not exist')

home_folder = os.path.expanduser('~')
#from pathlib import Path
#home_folder = Path.home()
print(home_folder)
my_dir = os.path.join(home_folder, 'Desktop')

print(os.listdir(my_dir))

for f in os.listdir(my_dir):
    desc = 'd' if os.path.isdir(f) else '-'
    print(f'{desc} {f}')