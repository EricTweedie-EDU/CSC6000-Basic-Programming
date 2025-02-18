# program multiplies 2 matrices together to compute:
# 1) if they are inverses of each other
# 2) if the result is not an identity matrix they are not inverses
# 3) if the matrices can even be multiplied together
# Hard coding matrices instead of asking for input

#Checking to see if the matrices can be multiplied

def matrix_multiply(A,B):
    if len(A[0]) != len(B):
        return print('Matrices can not be multiplied!')
    

# result matrix starting with zeroes
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

# recursive multiplicaton of matrices
    def multiply(A,B,result,i,j,k):
      if i >= len(A):
          return
      if j >= len(B[0]):
          return multiply(A,B,result,i+1,0,0)
      if k >= len(B):
          return multiply(A,B,result,i,j+1,0)
      result[i][j] += A[i][k] * B[k][j]
      multiply(A,B,result,i,j,k+1)

# matrix multiplication
    multiply(A,B,result,0,0,0)
    return result

#Matrices
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
B = [[12,7,3],[4,5,6],[7,8,9]]

result = matrix_multiply(A,B)
print(result)

if result == [[1, 0.0, 0.0],[0, 1.0, 0.0],[0, 0.0, 1.0]]:
    print("The matrices are inverses of each other!")
else:
    print("The matrices are not inverses of each other!")

