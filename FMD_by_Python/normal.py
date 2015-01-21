# -*- coding:utf-8 -*-
import numpy as np

def normal(org, n, bsize, block): 
	assert type(org) is np.ndarray 
	assert org.shape[0] == org.shape[1]

	if bsize == n:
		org_compress = org.sum(axis = 1).reshape(n, 1)

	else:	
		org_compress = np.zeros((n, block))

		if bsize * block > n:
			for i in xrange(0, block-1):
				org_compress[:, i] = org[:, i*bsize:(i+1)*bsize].sum(axis = 1)

			org_compress[:, block-1] = org[:, (block-1)*bsize:n].sum(axis = 1)
		else:
			for i in xrange(0, block):
				org_compress[:, i] = org[:, i*bsize:(i+1)*bsize].sum(axis = 1)

	return org_compress

