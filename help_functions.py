def Null_mat(rows, cols):
    mat = []
    for row in range(rows):
        mat.append([])
        for col in range(cols):
            mat[-1].append(float(0)) 
    return mat


def duplicate_mat(mat):
    rows, cols = len(mat), len(mat[0])
    dup_mat = Null_mat(rows, cols)
    
    for i in range(rows):
        for j in range(cols):
            dup_mat[i][j] = mat[i][j]

    return dup_mat

def identity_mat(rows, cols):
    diag = 1.0
    elsewhere = 0.0

    ident_matrix= []
    for i in range(rows):
        sub_matrix = []
        for j in range(cols):
            if i == j: 
                sub_matrix.append(diag)
            else: 
                sub_matrix.append(elsewhere)

        ident_matrix.append(sub_matrix)

    return ident_matrix

def transpose(A):
    
    transpose = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    display_mat("Transpose ", None, transpose, None,None)
    return transpose


def display_mat(Act, String_A, mat_A, String_B, mat_B):
    
    if mat_B == None:
        print(Act)
        for row in mat_A:
            row_print = ['{0:5.3f}'.format(round(val,3)) for val in row]
            print(row_print)
    
    else:
        print(Act)
        print(String_A, '\t'*int(len(mat_A)/2)+""*len(mat_B), String_B)

        len_A = len(mat_A)
        len_B = len(mat_B)
        if len_B > len_A: 
            for row in range(len_B):
                try:
                    row_1 = ['{0:5.3f}'.format(int(x)) for x in mat_A[row]]
                    row_2 = ['{0:5.3f}'.format(int(x)) for x in mat_B[row]]
                except(IndexError):
                    
                    row_1 = ['NaA']
                    row_2 = ['{0:5.3f}'.format(x) for x in mat_B[row]]
               
                print(row_1,'\t\t', row_2, '\n')
        else:
            for row in range(len_A):
                try:
                    row_1 = ['{0:5.3f}'.format(int(x)) for x in mat_A[row]]
                    row_2 = ['{0:5.3f}'.format(int(x)) for x in mat_B[row]]
                except(IndexError):
                    row_1 = ['{0:5.3f}'.format(x) for x in mat_A[row]]
                    row_2 = ["NaA"]

                print(row_1,'\t\t', row_2)
