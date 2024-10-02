
def even_odd(numbers: list) -> list:
	# result_list = []
	# for number in numbers:
	# 	if number % 2 == 0:
	# 		result_list.append('even')
	# 	else:
	# 		result_list.append('odd')
	# return result_list
	return ['even' if number % 2 == 0 else 'odd' for number in numbers]


print(even_odd([4])) #== ['even']
print(even_odd([145, -24442, 317])) #== ['odd', 'even', 'odd']
