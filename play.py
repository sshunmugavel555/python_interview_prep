# fileName="C:/Users/SShunmugavel/Downloads/Python_Crash_Course/Chap_01/python.txt"
# with open(fileName,'r') as fp:
#     data=fp.read()
#     lines=data.splitlines()

#     for line in lines:
#         print(line.replace('Python','GO'))


fileName="C:/Users/SShunmugavel/Downloads/Python_Crash_Course/Chap_01/bogo.txt"

try:
    with open(fileName,'r') as fp:
        fp.read()
except FileNotFoundError:
    print(f"File Not Found in given location ")

# with open(fileName,'r') as fp:
#     print(fp.read())