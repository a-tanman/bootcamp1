import os

def get_nodes(fid):
    lines = [line.rstrip('\n') for line in fid]
    tuple_list = []
    for line in lines:
        tuple_list.append(tuple(line.split(' ')))
    return tuple_list

f = open('./facebook_combined.txt', 'r')
result = get_nodes(f)
print(result)