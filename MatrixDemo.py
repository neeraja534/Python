for i in range(len(A)):
    for j in range(len(B[r])):
        for k in range(len(B)):
            C[i][j]=C[i][j]+A[i][k]*B[k][j]
    for i in C:
        print(i)
