#conding:utf-8
import numpy as np

def find_outlier(data):
	outlier = []
	q = np.percentile(data,(25,50,75),interpolation = 'midpoint')
	iqr = q[2] - q[0]
	for x in data:
		if x<q[0]-1.5*iqr or x>q[2]+1.5*iqr:
			outlier.append(x)
		

	return outlier
