import math

n = int(input())
arr = input().split()
ls = [int(i) for i in arr]

sum = sum(ls)
res = str(round(sum/n, 12))

point = res.split(".")[1]

len_required = 12

if len(point) < len_required:
    res += "0" * (len_required - len(point))

print(res)