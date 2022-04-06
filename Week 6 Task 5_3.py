#!/usr/bin/env python
# coding: utf-8

# In[4]:


# input Matrics
def inpMatrix(m,n):
    mat = []
    for i in range(m):  # A for loop for row entries
        a = [item for item in input().split()]
        del a[n:]
        mat.append(a)
    return mat

# transpose Matrics
def reversMatrix(mat_A, mat_B):
    for i in range(n):
        for j in range(m):
            mat_B[i][j] = mat_A[j][i]
    return mat_B

# print transpose matrics 
#def printMatrix(mat):
    #for i in range(int(n)):
        #for j in range(int(m)):
            #print(mat[i][j], end=" ")
        #print()

# m - number of rows
# n - number of columns

m, n = list(map(int, input().split()))

matrix_A = inpMatrix(m,n)
matrix_B = [[0 for x in range(m)] for y in range(n)]
matrix_B = reversMatrix(matrix_A,matrix_B)


i = 0
while i < n:
    print(*matrix_B[i])
    i+=1
#for i in len(matrix_B):
    
#printMatrix(matrix_B)

#if m%2 == 0:
    #for i in range (m): 
        #print(*matrix_B[i])

#else: 
    #for i in range (m+1): 
        #print(*matrix_B[i])
        #print(*matrix_B[i])

