def romanGenerator(digit,placeVal):
    """ Returns the roman equivalent of the digit based on the place value -> units,tens,hundreds or thousands """
    romanSnip=''

    if digit*10 in numLookup:
        romanSnip += romanLookup[numLookup.index(digit*placeVal)]
    elif (numLookup[0] < digit) and (digit < numLookup[1]):
        if placeVal==1:
            romanSnip += digit*(romanLookup[0])
        elif placeVal==10:
            romanSnip += digit*(romanLookup[4])
        elif placeVal==100:
            romanSnip += digit*(romanLookup[8])
        elif placeVal==1000:
            romanSnip += digit*(romanLookup[12])

    elif (numLookup[2] < digit) and (digit < numLookup[3]):
        if placeVal==1:
            romanSnip += romanLookup[2]+(digit-numLookup[2])*(romanLookup[0])
        if placeVal==10:
            romanSnip += romanLookup[6]+(digit-numLookup[2])*(romanLookup[0])
        if placeVal==100:
            romanSnip += romanLookup[10]+(digit-numLookup[2])*(romanLookup[0])
    
    return romanSnip

def number_to_roman(number,romanLookup,numLookup):
    """ Return the roman numeral equivalent of the given number 1 to 3999 permissible numbers """
    roman=[]

    if number in numLookup:
        roman += romanLookup[numLookup.index(number)]
        return roman
    else:
        placeVal=1
        while number>0:

            digit=number % 10
            number = number // 10

            romanSnip=romanGenerator(digit,placeVal)

            roman.append(romanSnip)

            placeVal *= 10

        return ''.join(roman[::-1])

romanLookup=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
numLookup=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
print(number_to_roman(3455,romanLookup,numLookup))