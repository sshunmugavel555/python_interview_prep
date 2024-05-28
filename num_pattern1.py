def num_triangle_pattern1(row):
    """ Create a number right triangle with x rows """
    for x in range(1,row+2):
        raw=''
        for y in range(1,x):
            raw=raw+f'{y}'+' '
        print(raw)


num_triangle_pattern1(5)