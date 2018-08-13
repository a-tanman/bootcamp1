import os

def get_nodes(fid):
    
    lines = [line.rstrip('\n') for line in fid]
    tuple_list = []
    for line in lines:
        num_pair = tuple(line.split(' '))
        if str(num_pair[0]).isdigit():
            tuple_list.append(num_pair)
        else:
            raise ValueError('Non numeric node id!')
    return tuple_list

f = open('./facebook_combined.txt', 'r')
result = get_nodes(f)
print(result)