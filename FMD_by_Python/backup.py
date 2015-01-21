	
		for i in xrange(0, block-1):
			left_compress[:, i] = np.dot(org[:, i * bsize : (i+1) * bsize], one)


		left_compress[:, block-1] = np.dot(org[:, (block-1) * bsize : n], np.ones(n - (block-1) * bsize))
	

		# assert type(org) is np.ndarray 
		# assert org.shape[0] == org.shape[1]

		# n = org.shape[0]
		# bsize = int(math.ceil(n * coff))
		# assert bsize >= 1

		# if coff == 1:
		# 	right_H = np.random.rand(1, n)
		# 	org_compress = org.sum(axis = 1).reshape(n, 1)

		# else:
		# 	block = int(math.ceil(n * 1.0 / bsize))
		# 	right_H = np.random.rand(block, n)
			
		# 	org_compress = np.zeros((n, block))

		# 	# one = np.ones(bsize)

		# 	if bsize * block > n:
		# 		for i in xrange(0, block-1):
		# 			org_compress[:, i] = org[:, i*bsize:(i+1)*bsize].sum(axis = 1)

		# 		org_compress[:, block-1] = org[:, (block-1)*bsize:n].sum(axis = 1)
		# 	else:
		# 		for i in xrange(0, block):
		# 			org_compress[:, i] = org[:, i*bsize:(i+1)*bsize].sum(axis = 1)