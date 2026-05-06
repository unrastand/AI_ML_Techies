import numpy as np 

mat_a = np.array([[1, 4, 3], [4, 5, 6], [7, 8, 9]])
mat_b = np.array([[9, 4, 7], [6, 5, 4], [3, 2, 1]])

mat_c = mat_a + mat_b

new = np.arange(1,20,2)

zeros = np.zeros((4,4))

mat = np.array([[1, 2 ], [4, 5 ], [7, 8 ], [10, 11]])
 
answer = np.dot(mat_a, mat_b)
 

a = mat.sum(axis=0)
print(a)
