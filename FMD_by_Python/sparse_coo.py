# -*- coding:utf-8 -*-
import time, math, random
import numpy as np
from scipy import sparse
import disguise

def GenCooSparse(size, coff):
	num = int(math.ceil(size * size * coff))
	lst = range(0, size * size)
	pos = sorted(random.sample(lst, num))
	row = [i / size for i in pos]
	col = [i % size for i in pos]
	data = np.random.rand(num)
	coo_sparse = sparse.coo_matrix((data, (row, col)), shape = (size, size))
	return coo_sparse

if __name__ == "__main__":
	n = 6
	coff = 0.5
	time1 = time.time()
	sps = GenCooSparse(n, coff)
	print time.time() - time1
	print type(sps) is sparse.coo_matrix

	time1 = time.time()
	# s = sps.toarray()
	res = disguise.disguise(sps, coff, "Sparse_coo")

	print time.time() - time1

	# print s
	#print sps.shape



















































print sparse








