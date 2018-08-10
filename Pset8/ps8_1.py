import random
import matplotlib.pyplot as plt
import timeit

def merge_sort(unsorted_list):
    
    list_length = len(unsorted_list)
    if list_length > 1:
        first_half = unsorted_list[:((list_length // 2))]
        # print(first_half)
        merge_sort(first_half)
        second_half = unsorted_list[(list_length // 2):]
        # print(second_half)
        merge_sort(second_half)

        left_pos, right_pos, result_pos = 0,0,0
        len_left = len(first_half)
        len_right = len(second_half)
        
        while left_pos < len_left and right_pos < len_right:
            if first_half[left_pos] < second_half[right_pos]:
                unsorted_list[result_pos] = first_half[left_pos]
                left_pos += 1
            else:
                unsorted_list[result_pos] = second_half[right_pos]
                right_pos += 1
            result_pos += 1
        
        while left_pos < len_left:
            unsorted_list[result_pos] = first_half[left_pos]
            left_pos += 1
            result_pos += 1
        
        while right_pos < len_right:
            unsorted_list[result_pos] = second_half[right_pos]
            right_pos += 1
            result_pos += 1


# unsorted_list = [5, 4, 3, 2, 1]
# merge_sort(unsorted_list)
# print(unsorted_list)

preparation_merge = """
import random
from __main__ import merge_sort
"""


data ="""
items = list(range({}))
random.shuffle(items)
"""

preparation_sort = """
import random
"""
x_axis = [10**n for n in range(1,7)]
data_list = [data.format(x) for x in x_axis]

merge_time = []
sort_time = []

for x in range(len(x_axis)):
	t = timeit.Timer("merge_sort(items)",preparation_merge + data_list[x])
	merge_time.append(t.timeit(number=1))
	t = timeit.Timer("sorted(items)",preparation_sort + data_list[x])
	sort_time.append(t.timeit(number=1))

print(merge_time)
print(sort_time)

x_axis = [x for x in range(1, len(merge_time)+1)]

print(x_axis)

plt.subplot(2,1,1)
plt.plot(x_axis, merge_time, 'g')
plt.subplot(2,1,2)
plt.plot(x_axis, sort_time, 'g') 
plt.show()