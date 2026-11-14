 
"""
The Fibonacci sequence is an infinite integer series in mathematics
where each number is the sum of the two preceding ones.

I did two version , fibo(x) which prove its limit for integer like 100, and 
fibo_v2(x) which readily deal with 100 
"""

def fibo(x):
	"""
	F(x) = F(x-1) + F(x-2)

	Input: positive integer x
	Output: F(x)
	"""
	if type(x) is not int:
		raise TypeError("x must be an integer")

	if x < 0:
		raise ValueError("x mustn't be a negative integer")

	if x == 0:
        	return 0
	elif x == 1:
        	return 1
	else:
        	return fibo(x - 1) + fibo(x - 2)


hist = {0:0, 1:1}
def  fibo_v2(x):
	"""
	F(x) = F(x-1) + F(x-2)
	Input: positive integer x
	Output: F(x)
	"""
	if type(x) is not int:
        	raise TypeError("x must be an integer")

	if x < 0:
        	raise ValueError("x mustn't be a negative integer")

	if x in hist :
		return hist[x]
	hist[x] = fibo_v2(x-1) + fibo_v2(x-2)
	return hist[x]




if __name__ == "__main__" :
	n = int(input("Enter n: "))
	#print(f"F({n}) = {fibo(n)}")
	print(f"F({n}) = {fibo_v2(n)}")

