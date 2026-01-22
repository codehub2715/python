#Use the os module to list all files in the current directory.

import os
file = os.listdir()
print("Files in the current directory:")
for files in file:
    print(files)
