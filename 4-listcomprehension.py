List=[i for i in range(2,10,2) ]
Set={i  for i in range (2,10,2) }
print(List)
print(sorted(Set))

#shallow copy:original list and new list will be same.and share same locations.
import copy
original=[1,2,3,4,5]
print(original)
new = original#shallow
print(new)
new[0]=100
print(original)
print(new)

#deep copy: original list and new list be diff. and share diff locations.
import copy
original=[1,2,3,4,5]
print(original)
new = copy.deepcopy(original)#deepcopy
print(new)
new[0]=100
print(original)
print(new)