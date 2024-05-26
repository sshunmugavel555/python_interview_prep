def low_high_vv(word):
    """ Convert the case from lower to higher / higher to lower in a given word """

    conv=[]

    for eL in word:
        if ord(eL) >=65 and ord(eL) <=90:
            low=ord(eL) + 32
            conv.append(chr(low))
        elif ord(eL) >=97 and ord(eL) <=122:
            high=ord(eL) - 32
            conv.append(chr(high))
    
    return ''.join(conv)


print(low_high_vv('sHaNkAr'))