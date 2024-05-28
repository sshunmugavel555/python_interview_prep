def num_triangle_pattern2(row):
    """ Create a number right triangle with x rows """
    cnt=0
    for x in range(1,row+2):
        raw=''
        for y in range(1,x):
            cnt+=1
            raw=raw+f'{cnt}'+' '
        print(raw)


num_triangle_pattern2(10)