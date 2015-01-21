import numpy as np
# from numpy.linalg import inv
import time
import math
import judge


def extendH(right_H, n, bsize):
	assert type(right_H) is np.ndarray
	block = math.ceil(n * 1.0 / bsize)
	assert right_H.shape == (block, n)
	# print "right_H=", right_H
	right_H = right_H.repeat(bsize, axis = 0)
	if right_H.shape[0] > n:
		right_H = right_H[0:n,:]
	# print "right_H=", right_H
	return right_H

def recover(res, right_H, n, bsize):
	assert type(res) is np.ndarray
	extH = extendH(right_H, n, bsize)
	extH = np.linalg.inv(extH + np.eye(n))
	rcv = np.dot(res, extH)
	return rcv

if __name__ == "__main__":
	pass
# 	n = 6
# 	bsize = 4
# 	block = math.ceil(n * 1.0 / bsize)
# 	H = np.random.rand(block,n)
# 	res = extendH(H, n, bsize)
# 	print 'H =', H 
# 	print 'res =', res 
# 	print res.shape
	