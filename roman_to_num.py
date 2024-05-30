def roman_to_num(roman,romanLookup,numLookup):
    """ Return the numeral equivalent of the given roman num. 1 to 3999 permissible numbers range inclusive"""

    numeral=0
    prev=''

    for eR in roman:
        if eR=='V' or eR=='X':
            if prev=='I':
                numeral+=numLookup[romanLookup.index(eR)]-2
                continue
        if eR=='L' or eR=='C':
            if prev=='X':
                numeral+=numLookup[romanLookup.index(eR)]-20
                continue
        prev=eR
        numeral+=numLookup[romanLookup.index(eR)]
    
    return numeral


romanLookup=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
numLookup=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
print(roman_to_num('MMMDCCXXIV',romanLookup,numLookup))