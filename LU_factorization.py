import copy
import sys
from help_functions import *

def lu_decomposition(A):
    n = len(A)

    #Eliminating possibility of entering anything else but a square matrix
    if len(A)<=1:
        sys.exit("Error: Your have entered a number, not a matrix. Program Terminated.")

    for i in range(n):
        if len(A[i])!=len(A):
            sys.exit("Error: You have entered a non square matrix. Program Terminated.")


    #Check that the diagonal of the matrix is not zeroes
    for i in range(n):
        checkRow = 0
        checkColumn = 0
        for k in range (i, n):
            if A[i][k]!=0:
                checkRow +=1
            if A[k][i]!=0:
                checkColumn +=1
        if checkRow == 0 or checkColumn == 0:
            sys.exit("Error: There is a row/column full of zeroes in your matrix. Program Terminated.")

    #Generating P, L, and U matrices        
    L = [[0 for i in range(0,n)] for i in range(0,n)]
    for i in range(0,n):
        L[i][i] = 1 

    U = copy.deepcopy(A)

    P = [[0 for i in range(0,n)] for i in range(0,n)]
    for i in range(0,n):
        P[i][i] = 1
        
    #Checking the pivots
    for i in range(0,n):
        if U[i][i] == 0:
            for k in range(i, n):
                if U[k][i]!=U[i][i] and U[k][k]!=0:
                    U[k], U[i] = U[i], U[k]
                    P[k], P[i] = P[i], P[k]
                else: 
                    continue

    #Eliminating elements
    for i in range(0,n):
        for j in range(i+1,n):
            mult = U[j][i]/(U[i][i])
            L[j][i] = mult
            for k in range(i, n):
                U[j][k] += -mult*U[i][k]
                

    return (A,P,L,U)

        
            
    


