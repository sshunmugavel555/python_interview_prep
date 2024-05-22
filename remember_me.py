from pathlib import Path
import json

def get_stored_username(path):
    contents=path.read_text()
    infoDict=json.loads(contents)
    print(f"Welcome back {infoDict['user']} -> we remember you !!")
    for k,v in infoDict.items():
        print(f"{k}-->{v}")

def get_new_username(path):
    user=input(f"Enter your username.. we will remember you next time you come :")
    age=input(f"Enter your age.. we will remember you next time you come :")
    sex=input(f"Enter your sex.. we will remember you next time you come :")
    infoDict={'user':user,'age':age,'sex':sex}
    contents=json.dumps(infoDict)
    path.write_text(contents)

def greet_user():
    path=Path('username.json')
    if path.exists():
        print(f"The current user logged in is {json.loads(path.read_text())['user']}")
        cho=input("Is this you ? y or n ")
        if cho=='y':
            get_stored_username(path)
        else:
            get_new_username(path)
    else:
        get_new_username(path)


greet_user()