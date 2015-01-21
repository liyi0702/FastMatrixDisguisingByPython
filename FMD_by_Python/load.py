# -*- coding:utf-8 -*-
import numpy as np
import scipy.io as sio
from scipy.sparse import coo_matrix

load_path = "matrix_to_load/" 
save_path = "matrix_to_save/" 

def LoadFromNPY():
	try:
		array = np.load(load_path + "a.npy")
	except Exception, e:
		print e
	return array

def LoadFromMAT():
	try:
		mat_dict = sio.loadmat(load_path + "a.mat")
		if mat_dict.has_key("array"):
			array = mat_dict["array"]
		else:
			for value in mat_dict.values():
				if type(value) is np.ndarray and value.size >= 6:		
					array = value
	except Exception, e:
		print e
	return array

def LoadFromCSV():
	try:
		array = np.load(load_path + "a.csv")
	except Exception, e:
		print e
	return array

def LoadFromTXT():
	try:
		array = np.loadtxt(load_path + "a.txt", delimiter = ',')
	except Exception, e:
		print e
	return array

if __name__ == "__main__":
	pass

# print array
# print array.shape
# print type(array) 
# print array.size

