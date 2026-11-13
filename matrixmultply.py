def add_matrices(A,B):
    rows,cols=len(A),len(A[0])
    result=[[A[i][j]+B[i][j] for j in range(cols)]for i in range(rows)]
    return result
def transpose_matrix(A):
    rows,cols=len(A),len(A[0])
    result=[[A[j][i]for j in range(rows)]for i in range(cols)]
    return result
def multiply_matrices(A,B):
    rows_A,cols_A=len(A),len(A[0])
    rows_B,cols_B=len(B),len(B[0])
    if cols_A!=rows_B:
        raise ValueError("CAnnot multiply")
    result=[[0 for _ in range(cols_B)]for _ in range(rows_A)] 
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result+=A[i][k]*B[k][j]
    return result
def display(M):
    for row in M:
        print(row)
    print()
if __name__=="__main__":
    A=[[1,2,3],[4,5,6]]
    B=[[7,8,9],[10,11,12]]
    print("MAtrixA:")
    display(A)
    print("matrix B:")
    display(B)
    print("A+B:")
    display(add_matrices(A,B))
