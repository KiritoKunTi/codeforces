n = int(input())
guyX = input().split()
guyY = input().split()

guyX = list(set(guyX))
guyY = list(set(guyY))

notExists = [str(i) for i in range(1, n+1)]
res = [i for i in notExists if i in guyX or i in guyY]

res.sort()

check = res == notExists


if check:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")