#indexing:0                 1          2            3            4
Cartoons=['Tom and Jerry','Doraemon','Shinchan','Chhota Bheem','Motu Patlu']
#-ve indexing: -5                -4          -3           -2           -1
#with indexing
for i in range(len(Cartoons)):
    print(f"Index {i} : {Cartoons[i]}")  # Tom and Jerry, Doraemon, Shinchan, Chhota Bheem, Motu Patlu
print("------------------------------------------")
#without indexing
for i in Cartoons:
    print(i)