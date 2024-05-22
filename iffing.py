cars=['honda','bmw','kia','tesla','toyota']

for eachC in cars:
    if eachC == 'bmw':
        print(eachC.title())
    elif eachC =='kia':
        print(eachC.upper())
    else:
        print(eachC)

age=65

if age<1 or age>=65:
    fee=0
elif age<10:
    fee=9
elif age<18:
    fee=15
elif age<65:
    fee=20
else:
    fee=0

print(fee)



