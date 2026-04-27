import numpy as np

array_1D = np.random.randint(1,30,(1,21))

matrix_2D_first = np.array([[2,4,5],[7,3,1],[6,4,9]])
matrix_2D_second = np.array([[2,4,5],[7,3,1],[6,4,9]])

result_1 = np.add(matrix_2D_first,matrix_2D_second)
result_2 = np.multiply(matrix_2D_first,matrix_2D_second)
ans= np.sqrt(result_1)
print(ans) 