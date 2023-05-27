def sum_dig(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    diagonal=0
    for i in range(rows):
        for j in range(cols):
            if i==j or i+j==rows-1:
                diagonal+=matrix[i][j]
    return diagonal
n,m=map(int,input().split())
matrixA=[]
for k in range(n):
    row=list(map(int,input().split()))
    matrixA.append(row)
result=sum_dig(matrixA)
print(result)