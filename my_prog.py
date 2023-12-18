!#/usr/bin/python3

ls = [int(i) for i in input.split()]

ls[:] = [i//2 for i in ls if i%2] 

print(ls)

