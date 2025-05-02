def fibonacci(num):
	if num <= 1:
		return 1
	else:
		return fibonacci(num-2) + fibonacci(num-1)