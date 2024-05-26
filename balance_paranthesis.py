def is_paranthesis_bal(paranStr):
    """ Return if a given string of open and closed paranthesis are properly balanced 
    True -> Balanced
    False -> Not Balanced / Empty String / String with Non-Paranthesis Characters """

    oP=['{','(','<','[']
    cP=['}',')','>',']']

    p=[]
    isBal=True

    if paranStr=='':
        isBal=False

    for eP in paranStr:
        if eP in oP:
            p.append(eP)
        elif eP in cP:
            if p:
                if p[-1]==oP[cP.index(eP)]:
                    p.pop()
                else:
                    isBal=False
                    break
            else:
                isBal=False
                break
        else:
            isBal=False

    if isBal==False:
        return False
    else:
        if p:
            return False
        else:
            return True
        
print(is_paranthesis_bal("{[<<<<>>>>]}"))