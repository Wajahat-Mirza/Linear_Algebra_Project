import sys
from help_functions import *
import time
def mat_multiplication(mat_A,mat_B):
    row_A, col_A = len(mat_A), len(mat_A[0])
    row_B, col_B = len(mat_B), len(mat_B[0])
    
    print("Dimensions of Matrix A: ({},{})\nDimensions of Matrix B: ({},{})".format(row_A, col_A,row_B, col_B))
    # display_mat("Input Matrix For Multiplication","Matrix A", mat_A, "Matrix B", mat_B)
    
    if col_A != row_B:
        print("Error: No. of Columns of A DO NOT match the no. of rows in B. Please Give Correct Input")
        sys.exit()
        
    mat_C = Null_mat(row_A, col_B)
    
    for row in range(row_A):
        for col in range(col_B):
            mat_C[row][col] = sum(mat_A[row][col2] * mat_B[col2][col] for col2 in range(col_A))
    
    print("Dimensions of Resultant Matrix: ({},{})".format(len(mat_C), len(mat_C[0])))
    
    time.sleep(1)
    display_mat("Resultant Matrix by product of Matrix A and B is: ", None, mat_C, None, None)
    return mat_C