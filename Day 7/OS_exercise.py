import os
print(os.listdir())
for item in os.listdir():
    if os.path.isdir(item):
        print(f"File: {item}")
    elif os.path.isfile(item):
        print(f"Directory: {item}")
