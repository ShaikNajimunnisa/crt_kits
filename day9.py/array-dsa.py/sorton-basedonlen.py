arr = [64, 34, 25, 12, 22, 11, 90]
#tc:O(n  log n)
arr.sort()
arr.sort(reverse=True)
s = sorted(arr)
#sort by key
words = ["banana","apple","cherry"]
words.sort(key=len) 
#def bubble_sort()