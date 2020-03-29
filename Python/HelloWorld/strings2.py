#
#

parrot = "Norwegian Blue"

print(parrot[0:14:5])



print(parrot[3]+"\n"+parrot[4]+"\n\n"+parrot[3]+"\n"+parrot[6]+"\n"+parrot[8])

print()

print(parrot[-1])
print(parrot[-14])

print(parrot[-11]+"\n"+parrot[-10]+"\n\n"+parrot[-11]+"\n"+parrot[-8]+"\n"+parrot[-6])


print(parrot[0:6]) #Norweg
print(parrot[3:5])


print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])


print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = "ajshfjkhfhdspiuhfis"


print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[-14:-8])



print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223;372:036 854,775;807"
print(number[1::4])

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()

print([int(val) for val in values])






