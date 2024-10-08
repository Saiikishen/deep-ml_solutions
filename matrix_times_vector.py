#Q1 
#Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0])!=len(b):
		return -1
	final = []
	for i in a:
		   temp = 0
		   for j in range(len(i)):
			   temp+=(i[j]*b[j])
		   final.append(temp)
	
	return final
