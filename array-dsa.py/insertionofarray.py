arr=[10,20,30,40]
#append-insert at END O(1)
arr.append(50)
#insertt at index O(n)
arr.insert(2,55)
#extend -add multiple O(k)
arr.extend([60,70])
#+ operator- concatenate O(n+m)
new_arr = arr + [80,90]