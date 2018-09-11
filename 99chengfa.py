row = 1
while row < 10:

    col = 1 
    while col <= row:
        print("%d * %d = %d" % (row, col, row * col),end='\t')
        col += 1
    row += 1
    print('')

