# ipaddress = input("Please enter an IP address: ")
# print(ipaddress.count("."))

# parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
#
# parrot_list.append("A norwegin Blue")
# for state in parrot_list:
#     print("This parrot is "+state)
#
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
#
# # numbers.sort()
#
# numbers_in_order = sorted(numbers)
#
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("The list are equal")
# else:
#     print("The list are not equal")
#
# if numbers_in_order == sorted(numbers):
#     print("The list are equal")
# else:
#     print("The list are not equal")

# list_1 = []
# list_2 = list()
#
# print("list 1: {}".format(list_1))
# print("List 2 : {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

#
# even = [2, 4, 6, 8]
#
# another_even = list(even)
#
# print(another_even == even)
#
# another_even.sort(reverse =True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]


for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)