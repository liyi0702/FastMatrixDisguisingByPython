# -*- coding:utf-8 -*-
import numpy as np
import math
import time

def UpDown(org, n, bsize, block):
	block = int(math.ceil(n * 1.0 / bsize))
	
	# right_H = np.random.rand(block, n)
	mid = int(math.ceil(n * 1.0 / 2))
	up_compress = np.zeros((mid, block))
	# res = np.empty((n, n), order ='C')

	if bsize * block > n:
		for i in xrange(0, block-1):
			up_compress[0:mid, i] = org[0:mid, i*bsize:(i+1)*bsize].sum(axis = 1)

		up_compress[0:mid, block-1] = org[0:mid, (block-1)*bsize:n].sum(axis = 1)
	else:
		for i in xrange(0, block):
			up_compress[0:mid, i] = org[0:mid, i*bsize:(i+1)*bsize].sum(axis = 1)

	lw_compress = np.flipud(up_compress[:n/2])
	org_compress = np.vstack((up_compress, lw_compress))
	# lw_compress = np.flipud(up_compress)
	# if n % 2 == 0:
	# 	org_compress = np.vstack((up_compress, lw_compress))
	# else:
	# 	org_compress = np.vstack((up_compress, lw_compress[1:]))

	return org_compress

def TestofUpDown(n, bsize):

	block = int(math.ceil(n*1.0/bsize))
	if n % 2 == 0:
		upper = np.random.rand(n/2, n)
		lower = np.flipud(upper)
	else:
		upper = np.random.rand(n/2+1, n)
		lower = np.flipud(upper[0:n/2, :])

	org = np.vstack((upper, lower))
	# print org
	org_compress = UpDown(org, n, bsize, block)
	assert org_compress.shape[0] == org.shape[0]
	# print org_compress
	return

if __name__ == "__main__":
	time1 = time.time()
	TestofUpDown(10000, 4)
	print time.time() - time1


