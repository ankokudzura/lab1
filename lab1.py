def filling_list(tmp_list):
    new_variable=''
    while True:
        new_variable = input("Please enter veriable, or press enter to finish: ")
        if new_variable == '':
            return tmp_list
        tmp_list.append(new_variable)




print("Enter data for the first list")
list1=[]
filling_list(list1)
print("Enter data for the second list")
list2=[]
filling_list(list2)


# sort-preserving algorithm for joining two lists
merge_list=[]
while len(list1)>0 or len(list2)>0:
    if len(list2)==0 :
        merge_list.append(list1[0])
        del list1[0]
    elif len(list1)==0:
        merge_list.append(list2[0])
        del list2[0]
    elif list1[0]<list2[0]:
        merge_list.append(list1[0])
        del list1[0]
    else:
        merge_list.append(list2[0])
        del list2[0]
        
        
print("---------------------------------------")
print(merge_list)