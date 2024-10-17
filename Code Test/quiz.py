#!/usr/bin/env python
# coding: utf-8

# 1.Solve reverse_list without using built_in function

# In[ ]:


import numpy as np 

#In this case, we have two solutions.
#Solution 1: reverse the list in place
def reverse_list_sol1(l:list):

    n = len(l)

    #iterate through the list. we only need to iterate n//2 times
    for i in range(n//2):

        #Swap the elements inplace
        l[i], l[n - 1- i] = l[n - 1- i], l[i]
    
    # Sort the reversed list without using built-in function
    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                # Swap if the elements are in the wrong order
                l[j], l[j + 1] = l[j + 1], l[j]
    return l
    
    
#solution 2: create a new list to store the elements from original list in reverse order
def reverse_list_sol2(l:list):
        
    # Create an empty list to store the elements from roiginal list reversely
    result = []
    
    # Iterate through the original list in reverse order
    for i in range(len(l) - 1, -1, -1):

        # Append each element to the reversed list
        result.append(l[i])

    # Sort the reversed list without using built-in function
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                # Swap if the elements are in the wrong order
                l[j], l[j + 1] = l[j + 1], l[j]

    return result
   

 

 


# 2. Solve sudoku matrix.

# In[ ]:


#Helper functions are needed in this case.
#Helper function that check if there is any empty cell to fill.
def is_empty(matrix):

    #loop through every
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return i, j  #return the corrdinates of an empty cell
                
    return None #The matrix is solved already if there is no empty cell to fill

#function that check if the given number can be palced at the given cell
def is_valid(matrix, num, row, col):
    
        # Check the row for duplicates
        for c in range(9):
            if matrix[row][c] == num:
                return False
                
        # Check the column for duplicates
        for r in range(9):
            if matrix[r][col] == num:
                return False
        # Check duplicates in a 3 by 3 section
        box_row = row // 3 * 3  
        box_col = col // 3 * 3  
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if matrix[r][c] == num:
                    return False
                    
        return True  # The number can be placed in the given cell
    
#function that determine if the sudoku is solved.
def is_solved(matrix):
    cells = is_empty(matrix)
    if not cells:
            return True  # The sudoku is solved when there is no empty cell to fill

    row, col = cells

    for num in range(1, 10):
        if is_valid(matrix, num, row, col):
            matrix[row][col] = num
            
            #recur the function to solve for next cell untill all done
            if is_solved(matrix):
                return True

            matrix[row][col] = 0 #Backtrack if no possible answer for current cell
    

    return False

#Print the matrix if is solved, priint out error message otherwise
def solve_sudoku(matrix):

    if is_solved(matrix):
        print(matrix)
    else:
         print("There is no solution exists")
    

