import numpy as np

def base_converter(number, base):
	num_convs = {10 : 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j'}
	string_num = ""

	if number == 0:
		string_num = "0"

	else:
		power = 0
		while base**power < number:
			power += 1
		if base**power == number:
			for i in range(0, power+1):
				if i == 0:
					string_num +="1"
				else:
					string_num += "0"

		else:
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

print(base_converter(21834,2))

