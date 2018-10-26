#!/usr/bin/env python3

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
			result = val1 + val2
			stack.append(result)
			return stack[0]


def main():
	while True:
		result = calculate(input('rpn calc> '))
		print(result)

if __name__ == '__main__': 
	main()