from pathlib import Path
import os

#path=os.path("C:/Users/SShunmugavel/Downloads/Python_Crash_Course/Chap_01/pi_digits.txt")

fileName="C:/Users/SShunmugavel/Downloads/Python_Crash_Course/Chap_01/pi_million_digits.txt"
#C:\Users\SShunmugavel\Downloads\Python_Crash_Course\Chap_01\pi_million_digits.txt
#path="C:\Users\SShunmugavel\Downloads\Python_Crash_Course\Chap_01\pi_digits.txt"

bday=input("Enter your bday in the form of mmddyy : ")


pi_string=''
with open(fileName,'r') as f:
    data=f.read()
    lines=data.splitlines()
    for line in lines:
        pi_string+=line.strip()
        #print(line)

print(pi_string[:50])
print(len(pi_string.strip()))

if bday in pi_string:
    print(f"Your bday {bday} appears in the first 1 million digits of pi")
else:
    print(f"Your bday {bday} does NOT occur in the first 1 million digits of pi")
    
