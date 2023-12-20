import time

# get the start time
st = time.time()

array = ["abc", "1a3", "de6", "456"]
newArray = []

"""  
def getNewArray(x):
    newArray.add(x)

for i in array:
    for elem in i:
        if elem.isdecimal() and i not in newArray:
            newArray.append(i)
            continue
"""
newArray = filter(lambda x: x.isalnum(), array)

for i in newArray:
    print(i, end=' ')

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

# newArray = filter(map(lambda x: x.isalnum(), array))
print(newArray)
