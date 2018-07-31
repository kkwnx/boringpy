def listprint(s_list):
	print_string = ""
	for i in range(len(s_list)):
		print_string = print_string + s_list[i]
		if i < len(s_list)-2:
			print_string = print_string + ", "
		elif i == len(s_list)-2:
			print_string = print_string + " and "
	return print_string

l = []
input_num = int(input('何個文字列を入力しますか:'))
for i in range(input_num):
	add_string = input('文字列を入力してください:')
	l.append(add_string)
print(listprint(l))
	
