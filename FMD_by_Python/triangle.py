# -*- coding:utf-8 -*-
import numpy as np
import math

# ********************* 右上三角矩阵 **********************

def RightUp(org, n, bsize, block):
	org_compress = np.zeros((n, block))
	if bsize * block > n:
		for i in xrange(0, block-1):
			org_compress[0:(i+1)*bsize, i] = org[0:(i+1)*bsize, i*bsize:(i+1)*bsize].sum(axis = 1)

		org_compress[:, block-1] = org[:, (block-1)*bsize:n].sum(axis = 1)
	else:
		for i in xrange(0, block):
			org_compress[0:(i+1)*bsize, i] = org[0:(i+1)*bsize, i*bsize:(i+1)*bsize].sum(axis = 1)
	return org_compress

def TestofRightUp(n, bsize):
	block = int(math.ceil(n * 1.0 / bsize))
	org = np.random.rand(n, n)
	org = np.triu(org)
	print org
	print RightUp(org, n, bsize, block)

# **********************************************************

# ********************* 左下三角矩阵 ***********************

def LeftDown(org, n, bsize, block):
	org_compress = np.zeros((n, block))
	if bsize * block > n:
		for i in xrange(0, block-1):
			org_compress[i*bsize:n, i] = org[i*bsize:n, i*bsize:(i+1)*bsize].sum(axis = 1)

		org_compress[block-1:n, block-1] = org[block-1:n, (block-1)*bsize:n].sum(axis = 1)
	else:
		for i in xrange(0, block):
			org_compress[i*bsize:n, i] = org[i*bsize:n, i*bsize:(i+1)*bsize].sum(axis = 1)
	return org_compress

def TestofLeftDown(n, bsize):
	block = int(math.ceil(n * 1.0 / bsize))
	org = np.random.rand(n, n)
	org = np.tril(org)
	print org
	print LeftDown(org, n, bsize, block)

# **********************************************************

# ***********************左上三角矩阵***********************

def LeftUp(org, n, bsize, block):
	org_compress = np.zeros((n, block))
	if bsize * block > n:
		for i in xrange(0, block-1):
			org_compress[0:n-i*bsize, i] = org[0:n-i*bsize, i*bsize:(i+1)*bsize].sum(axis = 1)

		org_compress[0:bsize, block-1] = org[0:bsize, (block-1)*bsize:n].sum(axis = 1)
	else:
		for i in xrange(0, block):
			org_compress[0:n-i*bsize, i] = org[0:n-i*bsize, i*bsize:(i+1)*bsize].sum(axis = 1)
	return org_compress

def TestofLeftUp(n, bsize):
	block = int(math.ceil(n * 1.0 / bsize))
	org = np.random.rand(n, n) 
	org = np.flipud(np.tril(org))
	print org
	print LeftUp(org, n, bsize, block)

# **********************************************************

# ***********************右下三角矩阵***********************

def RightDown(org, n, bsize, block):
	org_compress = np.zeros((n, block))
	if bsize * block > n:
		for i in xrange(0, block-1):
			org_compress[n-(i+1)*bsize:n, i] = org[n-(i+1)*bsize:n, i*bsize:(i+1)*bsize].sum(axis = 1)

		org_compress[:, block-1] = org[:, (block-1)*bsize:n].sum(axis = 1)
	else:
		for i in xrange(0, block):
			org_compress[n-(i+1)*bsize:n, i] = org[n-(i+1)*bsize:n, i*bsize:(i+1)*bsize].sum(axis = 1)
	return org_compress

def TestofRightDown(n, bsize):
	block = int(math.ceil(n * 1.0 / bsize))
	org = np.random.rand(n, n)
	org = np.flipud(np.triu(org))
	print org
	print RightDown(org, n, bsize, block)

# **********************************************************

if __name__ == "__main__":
	func = TestofRightUp
	# TestofRightUp(6, 2)
	# TestofLeftDown(6 ,2)
	# TestofLeftUp(6 ,4)
	# TestofRightDown(6, 3)
	func(6, 2)