import time
import sys
from help_functions import *
from Matrix_mutliplication import *

def inverse(mat_A, Ident): 
    inverse_mat = duplicate_mat(mat_A)
    ident_mat = duplicate_mat(Ident)

    display_mat("Starting with: ", "\tMatrix", inverse_mat , "\t\t    Identity", Ident)
    print("\n")

    instances = len(mat_A)
    indices = list(range(instances)) 
    for diag in range(instances): 
        try:
            diag_value = 1.0 / inverse_mat[diag][diag]
            for j in range(instances): 
                inverse_mat[diag][j] *= diag_value
                ident_mat[diag][j] *= diag_value

            
            string1 = '\nScale row_{} of inverse_mat and ident_mat by '
            string2 = 'diagonal element {} of inverse_mat, which is 1/{:.2f}.\n'
            stringsum = string1 + string2
            val1, val2 = diag+1, diag+1
            Action = stringsum.format(val1,val2,round(1./diag_value,3))
            display_mat(Action, '\tMatrix', inverse_mat, "\t\t    Ident_Mat",ident_mat)
            print()

            
            for i in indices[0:diag] + indices[diag+1:]: 
                curr_row = inverse_mat[i][diag] 
                for j in range(instances): 
                    inverse_mat[i][j] = inverse_mat[i][j] - curr_row * inverse_mat[diag][j]
                    ident_mat[i][j] = ident_mat[i][j] - curr_row * ident_mat[diag][j]

                    
                string1 = '\tSubtract {:.2f} * row_{} of inverse_mat from row_{} of inverse_mat, and \n'
                string2 = '\tsubtract {:.2f} * row_{} of ident_mat from row_{} of ident_mat\n'
                val1, val2 = i+1, diag+1
                stringsum = string1 + string2
                Action = stringsum.format(curr_row, val2, val1, curr_row, val2, val1)
                display_mat(Action, "\tMatrix",inverse_mat, "\t\t    Ident_Mat",ident_mat)
                print("\nComputing... Please Wait :) ")
                time.sleep(1)
        except:
                print("\n\t\t"+"\033[4m" + "\033[1m" + "Inverse matrix doesn't exist\n" + "\033[0m")
                display_mat("Inverse does NOT exist for Matrix: ", None,mat_A, None,None)
                print("This Attempt is Terminated!")
                sys.exit()
    
    display_mat("\033[0m \t\t \033[4m\033[1mResult: Inverse Matrix is:\033[0m \n ", "\tInverse Matrix", ident_mat , None, None)  

    print("\n\t\t\033[4m\033[1mValidaing By multiplying Matrix by its Inverse!\033[0m\n \tIf Identity Matrix is given, then Our Computation is correct!\n")
    print("\nComputing... Please let the machine compute Matrix_mutliplication :) ")
    time.sleep(2)
    mat_multiplication(mat_A, ident_mat) 
    print("\nHence, our Computation is correct!!!\n")    

    return inverse_mat, ident_mat
