'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 91
Zero Matrix
----------------------------------------
Problem Statement: Write an algorithm such that if an element in an M x N matrix is 0, its entire row and colum are set to o
example
    input: 
    1 1 1     
    1 0 1    
    1 1 1           
    output: 
    1 0 1
    0 0 0
    1 0 1
Constraits or Questions you need to ask:

Solution notes:

'''
def zeroMatrix(matrix):
    #Storing which rows and colums need to become 0s
    zeroRow = set()
    zeroCol = set()

    #Number of rows and colums saved
    numRows = len(matrix)
    numCols = len(matrix[0])

    #Grabbing all rows and columns where the matrix has a 0
    for i in range(numRows):
        for j in range(numCols):
            if matrix[i][j] == 0:
                zeroRow.add(i)
                zeroCol.add(j)
    #Changing the rows and colums we saved to 0
    for i in range(numRows):
        for j in range(numCols):
            if i in zeroRow or j in zeroCol:
                matrix[i][j] = 0




def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()




matrix = [[1,1,1],[1,0,1],[1,1,1]]

print("Matrix before zero matrix function")
printMatrix(matrix)
zeroMatrix(matrix)
print("Matrix after zero matrix function")
printMatrix(matrix)



