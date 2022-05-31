import math

n = int(input())
outer = []
# res = []

for i in range(n):
    outer.append(input().split())

for i in range(n):
    a = int(outer[i][0])
    b = int(outer[i][1])

    ceil = math.ceil(a / b)
    temp = b*ceil - a
    # res.append(temp)
    print(temp)



# print(res)