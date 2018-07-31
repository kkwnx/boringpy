def collatz(number):
	mod_result = number % 2
	if mod_result == 0:
		return number/2
	else:
		return 3 * number + 1

try:		
	indata = input()
	outdata = collatz(int(indata))
	print("%d" % outdata)
except ValueError:
	print("Input number!")
	
