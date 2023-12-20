
from pathlib import Path

path = "/path/to/your/file.txt"
filename = Path(path).name

print(filename)
 
print(not 'e' not in 'xyz')
print('xyz' not in 'uvwxyz')
print('' in 'xyz')
