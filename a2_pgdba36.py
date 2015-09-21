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
			user_input_list.append(float(i))
	return user_input_list

#def float to int and cleaning with the list or the array as the input and the simplified list as the output 

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
	return float(search_number)
	
def input_for_sorting():
	numbers = raw_input("Enter a comma seperated list of numbers to be sorted :").split(",")
	return clean_list(numbers)

def mid_element_index(input_list):
		size = len(input_list)
		if size%2 == 0:
			return ((size/2)-1)
		else:
			return ((size+1)/2)-1

def linear_search(input_list,input_number):
	steps = 0	
	#loop through the list
	for element in input_list:
		steps = steps + 1
		if element == input_number:
			break
	
	#print output to console
	if steps == len(input_list):
		print "\nNumber is not an element of the list"
	else:
		print "\n\nNumber found in the list at %d position in %d number of steps"%(steps,steps) 

def binary_search(input_list,input_number):
	
	#inplementing the terminating condition for the binary search
	if len(input_list) == 1:
		if input_list[0] == input_number:
			print "Number found in the list"	
			return
		else:
			print "Number not found in the list"
			return
	#if the above terminating condition is false then the function goes into recursion
	else: 
		mid_index = mid_element_index(input_list)
		mid_val = input_list[mid_index]
		print "The number in this step is compared to: ",mid_val

		#recursive part of the function
		if input_number == mid_val:
			print "Number found in the list in list"
		elif input_number > mid_val:
			binary_search(input_list[mid_index+1:len(input_list)],input_number)
		else:
			binary_search(input_list[0:mid_index+1],input_number)


def insertion_sort(input_list):
	sorted_list = [input_list[0]]
	outer_loop_count = 0
	for element in input_list[1:len(input_list)]:
		print "Sorted list in the step %d is : "%outer_loop_count,sorted_list
		outer_loop_count = outer_loop_count + 1
		loop_count = 0
		for i in sorted_list:
			loop_count = loop_count + 1
			ind = sorted_list.index(i)
			if element <= i:
				sorted_list.insert(ind,element)
				break
		if loop_count == len(sorted_list):
		 	sorted_list.append(element)
	print "\nFinal sorted list : ",sorted_list



def selection_sort(input_list):
	#function to identify the minimum and remove it from the list
	def min_element(input_list):
		rolling_min_element = input_list[0]
		for element in input_list[1:len(input_list)]:
			if element < rolling_min_element:
				rolling_min_element = element
		input_list.remove(rolling_min_element)
		return rolling_min_element

	#running the min_function over the input list and adding the output to a new list
	sorted_list = []
	for i in range(len(input_list)):
		sorted_list.append(min_element(input_list))
		print "Sorted list in the step %d is : "%i,sorted_list

	print "\nFinal sorted list : ",sorted_list

#Function to write the bubble sort algorithm
def bubble_sort(input_list):
	count_check = 1   #variable to keep track of the quality of the final sorted list. when the final list is sorted this will be zero
	steps = 0
	while count_check>0:
		count_check = 0
		steps = steps + 1
		for i in range(len(input_list)-1):
			if input_list[i]>input_list[i+1]:
				count_check = count_check + 1
				temp = input_list[i]
				input_list[i] = input_list[i+1]
				input_list[i+1] = temp
		print "Sorted list in the step %d is : "%steps,input_list

	print "\nFinal sorted list : ",input_list

def quick_sort(input_list):
	print input_list

def merge_sort(input_list):
	if len(input_list)==1:
		#print input_list
		return input_list
	elif len(input_list) == 2:
		if input_list[0]>input_list[1]:
			temp = input_list[0]
			input_list[0] = input_list[1]
			input_list[1] = temp
		#print input_list
		return input_list	
	else:
		parting = mid_element_index(input_list)
		#print parting 
		print "length of input",len(input_list)
		sorted_list = []
		part1 = merge_sort(input_list[0:parting+1])
		print "part1",part1
		part2 = merge_sort(input_list[parting+1:len(input_list)])
		print "part2",part2
		while (len(part1)>0 and len(part2)>0):
			if part1[0]>part2[0]:
				sorted_list.append(part2[0])
				part2.remove(part2[0])
			else:
				sorted_list.append(part1[0])
				part1.remove(part1[0])

		if len(part1)==0:
			sorted_list = sorted_list + part2
		else:
			sorted_list = sorted_list + part1
		
		print sorted_list
		return sorted_list		



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

