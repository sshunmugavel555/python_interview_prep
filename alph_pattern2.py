def alph_triangle_pattern2(row):
    """ Create a alphabet right triangle with x rows - var2 """
    alph=65
    raw=''
    for y in range(1,row+2):
        for z in range(1,y):
            raw=raw+f'{chr(alph)}'+' '
            alph+=1
        print(raw)
        raw=''


alph_triangle_pattern2(5)