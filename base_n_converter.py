import numpy as np

# function takes in as parameters the number to convert and the base to convert into
# the output will be a string of the given number in the given base
def base_converter(number, base):
	# allows for conversion up to base 35
	num_convs = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j',
	 			 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't',
	 			 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}
	# string that holds the output
	string_num = ""


	if base > 35 or base < 2:
		string_num = "invalid base entered"
	else:
		# zero will always be zero
		if number == 0:
			string_num = "0"
		else:
			power = 0
			while base**power < number:
				power += 1

			# if n^p == num then the output will be 1 at the pth pos. followed by zeros
			if base**power == number:
				for i in range(0, power+1):
					if i == 0:
						string_num +="1"
					else:
						string_num += "0"
			else:
				#find the vales positions (p-1) to zero
				for q in range(1, power+1):
					j = 0
					while j < base and j*(base**(power-q)) <= number:
						j += 1
					j -= 1	

					if j >= 10:
						string_num += num_convs[j]
					else:
						string_num += str(j)

					number -= j*(base**(power-q))

	return string_num

#examples
if __name__ == "__main__":
	print(base_converter(89,6))
	print(base_converter(63,12))
	print(base_converter(1111, 20))
	print(base_converter(152769, 33))

