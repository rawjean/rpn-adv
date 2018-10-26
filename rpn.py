#!/usr/bin/env python3
import operator

op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
def calculate(arg):
	# stack for calculator
	stack = []

	# tokenize input
	tokens = arg.split()

	# process tokens
	for token in tokens:
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			val1 = stack.pop()
			val2 = stack.pop()

			# Look up function
			func = op[token]
			result = func(val1, val2)
			
			stack.append(result)
			return stack[0]


def main():
	while True:
		result = calculate(input('rpn calc> '))
		print(result)

if __name__ == '__main__': 
	main()