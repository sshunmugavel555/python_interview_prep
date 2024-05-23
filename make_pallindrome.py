def make_pallindrome(word):
    """ If the given word has an odd letter that can be removed to make the word a pallindrome - find that odd letter
     Return None if no such letter is odd - cannot be made into a pallindrome / if the word is already a pallindrome  """
    
    can_b_pal=False

    if word==word[::-1]:
        print("No Odd Letter : Word is already a pallindrome ")
    else:
        wl=list(word)
        for x in range(len(wl)):
            p=wl.pop(x)
            if ''.join(wl)==''.join(wl[::-1]):
                print(f"{p} at index {x} has to be removed to make a pallindrome -> {''.join(wl)} : Input -> {word}")
                can_b_pal=True
                break
            else:
                wl.insert(x,p)
        if can_b_pal:
            pass
        else:
            print(f"{word} cannot be made into a pallindrome after removing any of its odd letters")

make_pallindrome('rotator')


