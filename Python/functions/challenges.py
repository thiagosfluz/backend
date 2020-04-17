a, b, c, d = [int(i) for i in input().split()]
acceptedvalues = [0, 0, 0, 0]
counter=0
# ifs statements

if b > c and d > a:
    acceptedvalues[0] = 1
else:
    acceptedvalues[0] = 0
if c+d > a+b:
    acceptedvalues[1] = 1
else:
    acceptedvalues[1] = 0
if c and d > 0:
    acceptedvalues[2] = 1
else:
    acceptedvalues[2] = 0
if a%2 == 0:
    acceptedvalues[3] = 1
else:
    acceptedvalues[3] = 0

for i in acceptedvalues:
    if acceptedvalues[counter] == 1:
        counter+=1
    else:
        print("Valores nao aceitos")
        break
    if counter == len(acceptedvalues):
        print("Valores aceitos")

