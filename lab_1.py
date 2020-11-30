def filling_list(tmp_list):
    new_variable=''
    while True:
    # Ask the user for a name.
        new_variable = input("Please enter veriable, or press enter to end list: ")

    # Add the new name to our list.
        if new_variable == '':
            return tmp_list
        tmp_list.append(new_variable)




print("Enter data for the list")
list1=[]
filling_list(list1)

ver=input("Enter the desired variable: ")

if len(list1)==0:
    print("!!!ERROR: empty list!!!")
else:
    position=[]
    for i in range (0,len(list1)):
        if ver==list1[i]:
            position.append(i)
    if len(position)==0:
        print(0)
    else:
        print (position)