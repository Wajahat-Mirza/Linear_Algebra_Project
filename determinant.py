import sys
from help_functions import *
import time 

def determinant(mat, det = 0):

    if len(mat) != len(mat[0]):
        wrong = "No determinant because matrix is not square."
        return wrong
   
    indices = list(range(len(mat)))

    if len(mat) == 2 and len(mat[0]) == 2:
        det = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        print("\nComputing... Please Wait for the answer at the end :) ")
        time.sleep(1)
        display_mat("Making 2x2 matrix: ", None, mat, None, None)
        return det

    for size in indices:
        cmat = duplicate_mat(mat)
        cmat = cmat[1:]
        h = len(cmat)

        for i in range(h):
            cmat[i] = cmat[i][0:size] + cmat[i][size+1:]

        sign = (-1) ** (size % 2)  
        ldet = determinant(cmat)  
        det += sign * mat[0][size] * ldet

    return det
