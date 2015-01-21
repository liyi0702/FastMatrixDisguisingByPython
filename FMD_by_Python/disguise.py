# -*- coding:utf-8 -*-
import numpy as np
import time, math
from scipy import sparse
import normal, symmetry
from triangle import RightUp, LeftDown, RightDown, LeftUp

def disguise(org, coff = 0.05, mat_type = "Normal", tri_type = RightUp):
	assert coff >= 0 and coff <= 1 
	n = org.shape[0]
	bsize = int(math.ceil(n * coff))
	block = int(math.ceil(n * 1.0 / bsize))
	res = np.empty((n, n), order ='C')
	right_H = np.random.rand(block, n)

	if mat_type == "Normal":
		org_compress = normal.normal(org, n, bsize, block)
	elif mat_type == "Triangle":
		org_compress = tri_type(org, n, bsize, block)
	elif mat_type == "Symmetry":
		org_compress = symmetry.UpDown(org, n, bsize, block)	
	elif mat_type == "Sparse_coo":
		print n, bsize
		assert type(org) is sparse.coo_matrix
		org = org.toarray()
		org_compress = normal.normal(org, n, bsize, block)

	print org_compress
	res = np.dot(org_compress, right_H) + org

	return res, right_H, n, bsize

if __name__ == '__main__':
	# time1 = time.time()
	# n = 5000;
	# coff = 0.05
	# org = np.random.rand(n,n)
	# disguise(org, coff)
	# print time.time() - time1
	n = 6
	coff = 0.5
	org = np.random.rand(n, n) 
	org = np.flipud(np.tril(org))
	print org
	disguise(org, coff, "Triangle", LeftUp)
