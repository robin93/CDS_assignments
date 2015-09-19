#user input for program objective
objective = input("Please select on of the following:\
	\nLinear search  - 1\
	\nBinary Search  - 2\
	\nInsertion Sort - 3\
	\nSelection Sort - 4\
	\nBubble Sort    - 5\
	\nQuick Sort     - 6\
	\nMerge Sort     - 7\
	\nShell Sort     - 8\
	\nInput : ")

print objective

def clean_list(input_list):
	user_input_list = []
	for i in input_list:
		if not i.isalpha():
			if float(i)%1>0:
				user_input_list.append(float(i))
			else:
				user_input_list.append(int(i))
	return user_input_list

def input_for_Linear_search():
	numbers = raw_input("Enter a comma seperated list of numbers to be searched in :").split(",")  #https://www.daniweb.com/software-development/python/threads/352467/converting-input-into-a-list
	return clean_list(numbers)

def input_for_Binary_search():
	numbers = raw_input("Enter a comma seperated and sorted list of numbers to be searched in :").split(",")
	return clean_list(numbers)

def input_number_for_search():	
	while True:
		search_number = raw_input("Enter the number you have to search: ")
		if search_number.isalpha():
			print "Enter a valid number :"
			continue
		else:
			break
	if float(search_number)%1>0:
		return float(search_number)
	else:
		return int(search_number)
	
def input_for_sorting():
	numbers = raw_input("Enter a comma seperated list of numbers to be sorted :").split(",")
	return clean_list(numbers)

def linear_search(input_list,input_number):
	print input_list,input_number
def binary_search(input_list,input_number):
	print input_list ,input_number
def insertion_sort(input_list):
	print input_list
def selection_sort(input_list):
	print input_list
def bubble_sort(input_list):
	print input_list
def quick_sort(input_list):
	print input_list
def merge_sort(input_list):
	print input_list
def shell_sort(input_list):
	print input_list

if objective ==1:
	linear_search(input_for_Linear_search(),input_number_for_search())
elif objective ==2:
	binary_search(input_for_Binary_search(),input_number_for_search())
else:
	if objective == 3:
		insertion_sort(input_for_sorting())
	elif objective == 4:
		selection_sort(input_for_sorting())
	elif objective == 5:
		bubble_sort(input_for_sorting())
	elif objective == 6:
		quick_sort(input_for_sorting())
	elif objective == 7:
		merge_sort(input_for_sorting())
	elif objective == 8:
		shell_sort(input_for_sorting())

