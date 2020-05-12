import sys
import time
from help_functions import *
from Inverse_mat import *
from Matrix_mutliplication import *
from linear_system import *
from LU_factorization import * 
from determinant import *

def input_mat(num):

	rows = input("Enter number of rows for Matrix {}: ".format(num+1))
	cols = input("Enter number of columns for Matrix {}: ".format(num+1))

	while (rows.isnumeric() != True or cols.isnumeric() != True):
		print("\nError: Invalid Input. Rows and Cols can only be positive. Try Again. \n")
			
		rows = input("Enter number of rows for Matrix {}: ".format(num+1))
		cols = input("Enter number of columns for Matrix {}: ".format(num+1))

	rows = int(rows)
	cols = int(cols)

	final_matrix= []
	for i in range(rows):
	    sub_matrix = []
	    for j in range(cols):
	    	val = input("Please input Value of element {}{} of Matric {}: ".format(i+1,j+1, num+1))

	    	while val.replace(".", "", 1).lstrip('-').isdigit() != True:
	    		print("Error: Invalid! Try Again")
	    		val = input("Please input Value of element {}{} of Matric {}: ".format(i+1,j+1, num+1))

	    	val = float(val)
	    	sub_matrix.append(val)

	    final_matrix.append(sub_matrix)
	display_mat("\tMatrix_{}".format(num+1), None,final_matrix, None,None)

	return final_matrix, rows, cols

def actions(action,matrix, rows, cols):

	# final_matrix, rows, cols = input_mat(0)
	while action.lower() != "n":

		if action == "1":
			# final_matrix, rows, cols = input_mat(0)
			while rows != cols: 
				print("Mathematical Error: Non-Square Matrices Do not Have Inverse.\nPlease give Valid Inputs again")
				matrix, rows, cols = input_mat(0)

			ident = identity_mat(rows,cols)
			new_ident, inverse_final = inverse(matrix, ident)
			validity_input(matrix, rows, cols)


		elif action == "2":
			num_of_Mat = input("Num of Matrices to Multiply? ")
			while num_of_Mat.isdigit() != True:
				print("Error: Please give a positive numeric value")
				num_of_Mat = input("Num of Matrices to Multiply? ")
			
			num_of_Mat = int(num_of_Mat)
			if num_of_Mat != 2: 
				print("Error: This Code can multiply Two Matrices at a time. \nPlease Input two matrices and mutliply their resultant with the other matrices if need be.\
				\nSorry!")
				validity_input(matrix, rows, cols)
			
			mats = []
			for num in range(num_of_Mat):
				final_mat, rows, cols = input_mat(0)
				mats.append(final_mat)

			mat_multiplication(mats[0], mats[1])

			display_mat("\nMatrix_Multiplied\n", None,mats[0], None,None)
			display_mat("\nMatrix_Multiplied\n", None,matrix, None,None)

			validity_input(matrix, rows, cols)
			
		
		elif action == "3":

			(A,P,L,U) = lu_decomposition(matrix)
			mats = [A,P,L,U]
			mats_names = ['A','P','L','U']
			for i, j in zip(mats_names, mats):
				display_mat("\n\tMatrix_{}\n".format(i), None,j, None,None)
				print("\nCalculating... Please be patient with the machine :) ")
				time.sleep(1)

			validity_input(matrix, rows, cols)
		
		elif action == "5":
			
			A, B, C, total = lin_input()
			print("\n\n\t\t\033[1mFirst, solve the system using Sympy!\033[0m \n\n")
			sol = lin(C, total)
			print("\n\n\t\t\033[1mNow, we solve the system using our program.\033[0m \n\n")
			mat_A, mat_B, result = linear_system(A, B)
			
			print("\nThus, \033[1m\033[4mSymPy output\033[0m is:\n\n\t\t{}\n\nWhereas \033[1m\033[4mOur program output\033[0m is:\n\n\t\t{}\n".format(sol, result))
			validity_input(matrix, rows, cols)

		elif action == "4":
			det = determinant(matrix, det = 0)
			print("\n\t\t\tDeterminant of the given Matrix is: \033[4m\033[1m{}\033[0m \n".format(det))
			validity_input(matrix, rows, cols)

		elif action =="6": 
			t = transpose(matrix)
			validity_input(matrix, rows, cols)

		elif action == "7":
			print("You have Successfully Terminated the Program!")
			sys.exit()

		else: 
			print("Invalid input. Program Terminated.")
			sys.exit()
		
	return action

def validity_input(matrix, rows, cols):

	action = input("Do you want to continue [y/n]? ")
	while action != "y" and action != "n":
		print("Error: Invalid Input. Give either 'y' or 'n'. Try again!")
		action = input("Do you want to continue [y/n]? ")

	if action == "y":

		action = input("\n1. = Inverse \n2. = Multiplication\n3. = LU factorization\n4. = Finding Determinant \n\
5. = Solve Linear Equation System\n6. = Transpose\n7. = Quit\nPlease Input Numerical Value for Action. E.g. either '1' or '2': ")

		actions(action, matrix, rows, cols)
	else:
		print("Program Successfully Terminated")
		sys.exit()

	return action

print("================================================================================================")
print('\n\t\t\t\033[1m \033[91m \033[4m' +  "Matrix Calculator\n" + '\033[0m')
print("================================================================================================")
print("\nEnter your matrix on which you want the actions to execute: \n")
print("Directions to note \nThe Matrix that you are giving now can be used for finding \n\
1. Inverse\n2. LU factorization\n3. Finding Determinant \n4. Transpose\n\n\
This Matrix will not be used for computing \n1. Multiplication\n2. Solving Linear Equation System\nYou will have to give separate inputs, asked later\n\n\
If there is any error, please contact us! Have Fun! \n")
print("================================================================================================")
matrix, rows, cols = input_mat(0)
validity_input(matrix, rows, cols)





