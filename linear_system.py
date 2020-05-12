import time
import sys
import sympy as sp
from sympy.interactive import printing
printing.init_printing(use_latex = True)
from sympy import Eq, solve_linear_system, Matrix
from sympy import *
from help_functions import *
from Matrix_mutliplication import *

def valid_input():
    num_equ = input("No. of Equations to Solve: ")
    while num_equ.isnumeric() != True: 
        num_equ = input("No. of Equations to Solve: ")
    num_equ = int(num_equ)

    total = input("Total Distinct Variables in Equations: ")
    while total.isdigit() != True: 
        print("Invalid input. Try again.")
        total = input("Total Distinct Variables in Equations: ")
    total = int(total)

    return num_equ,total 


def lin_input(): 

    num_equ,total = valid_input()

    while total != num_equ: 
        print("Coefficients Matrix i.e. 'A' Matrix must be a Square. Your input is not square.\nRe-enter Values!")
        num_equ,total = valid_input()
    
    A = []
    B = []
    C = []
    equ_set = []
    for i in range(num_equ):
        ans = []
        print("Please give all Coefficients of Equ_{}. If there is no variable, add '0' as Coefficient for that variable. \nGive input with space in between as '2 -3 3': ".format(i+1))
        coeff = input("Coefficients of Equ_{} are: ".format(i+1))
        
        nums = [float(i) for i in coeff.split() if i.replace(".", "", 1).lstrip('-').isdigit()]
        while total != len(nums):
            print("There was some invalid entry. Try again. ")
            coeff = input("Coefficients of Equ_{} are: ".format(i+1))
            nums = [float(i) for i in coeff.split() if i.replace(".", "", 1).lstrip('-').isdigit()]

        A.append(nums)

        value = input("Please input the Answer Value of Equ_{}: ".format(i+1))
        while value.replace(".", "", 1).lstrip('-').isdigit() != True:
            print("Invalid")
            value = input("Please input the Answer Value of Equ_{}: ".format(i+1))
        value = float(value)
        
        ans.append(value)
        B.append(ans)

        nums.append(value)
        C.append(nums)

    return A, B, C, total

def linear_system(mat_A, mat_B): 
    new_mat_A = duplicate_mat(mat_A)
    new_mat_B = duplicate_mat(mat_B)

    display_mat("Starting with: ", "\tCoefficient Matrix", new_mat_A , "\tValues Matrix", mat_B)
    print("\n")

    instances = len(mat_A)
    indices = list(range(instances)) 
    for diag in range(instances): 
        try:
            diag_value = 1.0 / new_mat_A[diag][diag]
            for j in range(instances): 
                new_mat_A[diag][j] *= diag_value
            new_mat_B[diag][0] *= diag_value

            
            string1 = '\nScale row_{} of Coefficient Matrix and Values_mat by '
            string2 = 'diagonal element {} of Coefficient Matrix, which is 1/{:.2f}.\n'
            stringsum = string1 + string2
            val1, val2 = diag+1, diag+1
            Action = stringsum.format(val1,val2,round(1./diag_value,3))
            display_mat(Action, '\tCoefficient Matrix', new_mat_A, "\tValues_Mat",new_mat_B)
            print()

            
            for i in indices[0:diag] + indices[diag+1:]: 
                curr_row = new_mat_A[i][diag] 
                for j in range(instances): 
                    new_mat_A[i][j] = new_mat_A[i][j] - curr_row * new_mat_A[diag][j]
                new_mat_B[i][0] = new_mat_B[i][0] - curr_row * new_mat_B[diag][0]

                    
                string1 = '\tSubtract {:.2f} * row_{} of Coefficient Matrix from row_{} of Coefficient Matrix, and \n'
                string2 = '\tsubtract {:.2f} * row_{} of Values_mat from row_{} of Values_mat\n'
                val1, val2 = i+1, diag+1
                stringsum = string1 + string2
                Action = stringsum.format(curr_row, val2, val1, curr_row, val2, val1)
                display_mat(Action, "\tCoefficient Matrix",new_mat_A, "\tValues_Mat",new_mat_B)
                print("\nComputing... Please Wait :) ")
                time.sleep(1)
        except:
                print("\n\t\t"+"\033[4m" + "\033[1m" + "No Solution: Inverse of Coefficient Matrix doesn't exist\n" + "\033[0m")
                display_mat("Inverse does NOT exist for Coefficient Matrix: ", None,mat_A, None,None)
                print("\nTherefore, there is no solution to the given system of linear equations. This Attempt is Terminated!")
                sys.exit()
    
    result = new_mat_B
    display_mat("\033[0m \t\t \033[4m\033[1mResult: Values of the given Variables are:\033[0m \n ", None, result , None, None)  

    # print("\n\t\t\033[4m\033[1mValidaing: By multiplying Coefficient Matrix with Result Matrix!\033[0m\n \tIf Value Matrix is obtained, then Our Computation is correct!\n")
    # print("\nComputing... Please let the machine compute :) ")
    # time.sleep(1)

    # mat_multiplication(mat_A, new_mat_B) 
    # print("\nHence, our Computation is correct!!!\n")    

    return mat_A, mat_B, result

def lin(equations, total):

    eq1 = sp.Function('eq1')
    eq2 = sp.Function('eq2')
    eq3 = sp.Function('eq3')
    s,t,w,x,y,z = sp.symbols('s,t,w,x,y,z')

    system = Matrix(([equations[i] for i in range(len(equations))]))

    if total == 2:
        sol = solve_linear_system(system, x,y)
    elif total == 3: 
        sol = solve_linear_system(system, x,y,z)
    elif total == 4:
        sol = solve_linear_system(system, w,x,y,z)
    elif total == 5:
        sol = solve_linear_system(system, t,w,x,y,z)
    elif total == 6:
        sol = solve_linear_system(system, s,t,w,x,y,z)
    else: 
        print("Our Program Cannot compute for so many variables. Sorry.")
        sys.exit()

    if sol == "None": 
        print("No Solution for the given equations. ")
    else:
        print("Solution is: ",sol)

    return sol

# A, B, C = lin_input()
# linear_system(A, B)
# sol = lin(C)

