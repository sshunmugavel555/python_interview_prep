def star_triangle_pattern2(row):
    """ Create a star equilateral triangle with x rows """
    z=0
    for x in range(row+1,0,-1):
        raw=''
        for y in range(x,0,-1):
            raw+=' '
        raw+=z*(' *')
        print(raw)
        z+=1

star_triangle_pattern2(5)