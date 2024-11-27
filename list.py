color=input("Enter colors seperated by commas : ")
color_list=color.split(',')
print(color_list)
print("First color ",color_list[0])
print("Last color ",color_list[-1])
color_list1=["orange","white","cyan","Teal"]
print("color list not contained in colorlist2 are :")
diff=list(set(color_list)-set(color_list1))
print(diff)
color_int_list=[]
for color in color_list:
    color_int_list.append(len(color))
print(f" : list of integers corresponding to each color: {color_int_list}")