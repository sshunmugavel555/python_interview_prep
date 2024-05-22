from pathlib import Path
import json

def get_stored_fav(path):
    """ Retrieves the fav food already stored """
    contents=path.read_text()
    fav=json.loads(contents)
    print(f"We remember your fav food --> {fav}")

def store_fav(path):
    """ Store the fav food for the first time """
    fav=input("Enter your favorite food. We will remember this for you next time ")
    contents=json.dumps(fav)
    path.write_text(contents)


def call_out_fav():
    path=Path('fav_food.json')
    if path.exists():
        get_stored_fav(path)
    else:
        store_fav(path)

call_out_fav()
