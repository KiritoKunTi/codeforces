scan = input()
obj = scan[1:-1].split(', ')

if obj[0] == '':
    print (0)
else:
    print(len(set(obj)))