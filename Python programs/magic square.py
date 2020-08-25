mat = []
sumrow = []
sumcol = 0
for i in range(3):
    mat.append(list(map(int, input().rstrip().split())))
    summ = sum(mat[i])
    sumrow.append(summ)
for j in range(3):
    for i in range(3):
        sumcol = sumcol + mat[i][j]
    sumrow.append(sumcol)
    sumcol = 0   



print(sumrow)
