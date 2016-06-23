def help_command():
	print("Type 'DONE' to stop adding items")
	print("Type 'SHOW' to view current shopping list")
	print("Type 'HELP' to view commands")

def show_command():
	print("your list: " + str(shopping_list))

def add_to_list(new_item):
	shopping_list.append(new_item)
	print("Successfully added {} to the list. Shopping list now has {} items.".format(new_item, len(shopping_list)))

#make a list to hold onto our items
shopping_list = []

#print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter DONE to stop adding items")

while True:
	new_item = raw_input("Add: ")
	if new_item == "DONE":
		break
	elif new_item == "SHOW":
		show_command()
	elif new_item == "HELP":
		help_command()
	else:
		add_to_list(new_item)
	
	

print("Here's your list: ")
for item in shopping_list:
	print(item)
