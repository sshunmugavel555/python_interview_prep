myL=[1,2,3,'Shankar','Abi','kin',['nik','kin'],5.5]

print(myL[6][0].upper())

print(myL[-1])

autos=['honda','mazda','tesla','toyota']
print(autos[-1])

autos[-1]='kia'
print(autos[-1])
print(autos)

autos.append('bmw')
autos.append('vw')
print(autos)

autos.insert(1,'vw')
print(autos)

del autos[3]
print(autos)

temp=autos.pop(2)
print(temp)
print(autos)

autos.remove('vw')
print(autos)
