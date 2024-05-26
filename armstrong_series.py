def armstrong_series_until(cap):
    """ Print armstrong numbers until the given cap limit """

    for x in range(1,cap):
        num=x
        bck=x
        digCnt=0
        while num>0:
            dig = num % 10
            num = num // 10
            digCnt+=1
        

        num=bck
        cumu=0
        while num>0:
            dig = num % 10
            num = num // 10
            cumu += dig**digCnt
        
        if cumu==bck:
            print(cumu)



armstrong_series_until(70000)