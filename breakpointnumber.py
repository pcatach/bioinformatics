with open('data.txt') as input_data:
    perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())

num = sum(map(lambda x,y: x - y != 1, perm+[len(perm)+1], [0]+perm))

print str(num)
with open('resp.txt', 'w') as data:
    data.write(str(num))
