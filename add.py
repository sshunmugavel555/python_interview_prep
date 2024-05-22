while True:
    a=input('Enter A / quit')
    if a=='quit':
        break
    b=input('Enter B / quit')
    if b=='quit':
        break


    try:
        c=int(a)+int(b)
    except ValueError:
        pass
        #print(f"One of your inputs was not a number. Pls check ")
    else:
        print(f"{a}+{b}={c}")

