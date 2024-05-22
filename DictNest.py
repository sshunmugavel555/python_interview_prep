users={'us01':{'fn':'shan',
               'ln':'shunmu',
               'id':45},
        'us02':{'fn':'abee',
               'ln':'tan',
               'id':55},
        'us03':{'fn':'abee',
               'ln':'tan',
               'id':55},       
        }

for k,v in users.items():
    print(f"Details of user {k} are as below :")
    for kk,vv in v.items():
        print(f"{kk} --> {vv}")
    print('\n')


