import random
import matplotlib.pyplot as plt
import timeit

def insertion_sort(unsorted_list):
    
    list_length = len(unsorted_list)
    prev, curr, next = 0,0,0
    
    for i in range(list_length-1):
        # Compare first element to second element, and if larger, swap positions
        if unsorted_list[i+1] < unsorted_list[i]:
            unsorted_list[i+1], unsorted_list[i] = unsorted_list[i], unsorted_list[i+1]
            curr = i
            
            if(curr != 0):
                while(unsorted_list[curr] < unsorted_list[curr-1]):
                    unsorted_list[curr-1], unsorted_list[curr] = unsorted_list[curr], unsorted_list[curr-1]
                    curr -= 1
                    if curr == 0:
                        break
    
    print(unsorted_list)



insertion_sort([0,1,2,3,4,5])

preparation_insertion = """
import random
from __main__ import insertion_sort
"""


data ="""
items = list(range({}))
random.shuffle(items)
"""

preparation_sort = """
import random
"""
x_axis = [10**n for n in range(1,5)]
data_list = [data.format(x) for x in x_axis]

insertion_time = []
sort_time = []

for x in range(len(x_axis)):
	t = timeit.Timer("insertion_sort(items)",preparation_insertion + data_list[x])
	insertion_time.append(t.timeit(number=1))
	t = timeit.Timer("sorted(items)",preparation_sort + data_list[x])
	sort_time.append(t.timeit(number=1))

print(insertion_time)
print(sort_time)

x_axis = [x for x in range(1, len(insertion_time)+1)]

print(x_axis)

plt.subplot(2,1,1)
plt.plot(x_axis, insertion_time, 'g')
plt.subplot(2,1,2)
plt.plot(x_axis, sort_time, 'g') 
plt.show()