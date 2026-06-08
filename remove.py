list=["Python","Java","C++","JavaScript"]
print("The original list is: ",list)
list.insert(0,"SQL")
print(list)
list.remove("Java")
print(list)
'''
2-c programming
3-JavaScript
1=-Ruby
'''
#index
list=["Python","Java","C++","JavaScript"]
print("The original list is: ",list)
print(list.index("Java"))

#reverse method:
list=["Python","Java","C++","JavaScript"]
print("The original list is: ",list)
list.reverse()
print("The reversed list is: ",list)
#extend method:
front_end=['HTML','CSS','JS','BootStrap','ReactJS']
lang=['Python','django','Flask','NodeJS','Express']
print("Front-end TECHNOLOGY: ",front_end)
print("Back-end TECHNOLOGY: ",lang)
lang.extend(front_end)
print("All TECHNOLOGY: ",lang)

