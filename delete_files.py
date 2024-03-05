import os
if os.path.exists('First.txt'):
    os.remove('First.txt')
    print("The file is deleted")
else:
    print("The file is not found")
