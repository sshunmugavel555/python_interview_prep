def alph_triangle_pattern1(row):
    """ Create a alphabet right triangle with x rows """
    z=1
    raw=''
    for y in range(65,65+row):
        raw=raw+f'{z*chr(y)}'+' '
        print(raw)
        z+=1
        raw=''


alph_triangle_pattern1(10)