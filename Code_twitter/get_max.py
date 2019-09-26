def get_max(column):
 	max_val = 0

 	for val in column:
 		temp = int(val)
 		if (temp > max_val) :
 			max_val = temp

 	return max_val