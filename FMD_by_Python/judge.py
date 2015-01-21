import numpy as np
import math

def isEqualMat(A, B):
	assert type(A) is np.ndarray
	assert type(B) is np.ndarray
	assert A.shape == B.shape
 	res = (abs(A- B) < 1e-5).all()
 	return res
 
def isFullRank(A):
	assert type(A) is np.ndarray
	#assert A.shape[0] == A.shape[1]
 	return np.linalg.matrix_rank(A) == min(A.shape[0], A.shape[1])

if __name__ == "__main__":
	pass
# 	A = np.array([[1.3, 2.2, -2.3, 4.0], [21.4, 21.45, -12.36, 7], [72, 83.4, 912.2, 1.230], [123, 23, 3.4, -12.3]], order ='C')
# 	B = np.array([[1.3, 2.2, -2.3, 4], [21.41, 21.45, -12.36, 7], [72, 83.4, 912.2, 1.230], [123, 23, 3.4, -12.3]], order ='C')
# 	isEqualMat(A, B)
