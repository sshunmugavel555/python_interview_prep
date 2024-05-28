def star_triangle_pattern(row):
    """ Create a star right triangle with x rows """
    for x in range(row+1):
        raw=''
        for y in range(x):
            raw=raw+'*'+' '
        print(raw)


star_triangle_pattern(5)