# text = set(input("Please, type a text: "))
#
# print(text)
#
# vowels = {"a", "e", "i", "o", "u"}
#
# vowels_found = list(sorted(text.difference(vowels)))
#
#
#
# print(vowels_found)


# a = int(input("Please, enter with number 1: "))
# b = int(input("Please, enter with number 2: "))
# c = int(input("Please, enter with number 3: "))

a, b, c = [int(i) for i in input().split()]

bigger_ab = (a + b + abs(a-b)) // 2

bigger_abc = (bigger_ab + c + abs(bigger_ab - c))/2


print("{:.0f} eh o maior".format(bigger_abc))

