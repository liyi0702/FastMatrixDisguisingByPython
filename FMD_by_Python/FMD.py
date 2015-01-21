# -*- coding:utf-8 -*-
import time, math
import numpy as np
from scipy import sparse
import scipy.io as sio  

import disguise, judge, recover
import load, save

# n = 1000
# # coff = 0.05
# org = np.random.rand(n,n)
org = load.LoadFromTXT()

# bsize = int(math.ceil(n * coff))
# assert bsize >= 1

time1 = time.time()
print org
print org.shape
res, right_H, n, bsize = disguise.disguise(org)
print res
print res.shape

time2 = time.time()

# del left_compress
# del org

print time2 - time1

# print res
# save.SaveAsNPY(res)
# save.SaveAsTXT(res)
# # save.SaveAsCSV(res)
# # save.SaveAsMAT(res)

# # load.LoadFromNPY()
# # load.LoadFromMAT()
# load.LoadFromTXT()

# rcv = np.empty((n,n))
# rcv = recover.recover(res, right_H, n, bsize)

# # print judge.isEqualMat(org, rcv)
# print np.allclose(org, rcv)
# print 'org=', org
# print 'rcv=', rcv