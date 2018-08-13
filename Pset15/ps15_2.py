def read_stations(fid):
    lines = [line.strip('\n') for line in fid]
    # lines = fid.read().strip('\n').strip(' ').split('=')
    mrt_dict = dict()
    cur_key = None
    cur_val = None
    for line in lines:
        if len(line) > 0:
            if '=' in line:
                line = line.strip('=')
                cur_key = line
                mrt_dict[cur_key] = None
            else:
                mrt_dict[cur_key] = line.split(',')
                
    return mrt_dict

f = open('./mrt_lines.txt', 'r')
result = read_stations(f)
print(result)