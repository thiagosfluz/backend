# #read number
#
# n = int(input())
# numbers  = []
#
# for i in range(n):
#     numbers.append(int(input()))
#
# #function for Fibonacci sequence
# d = {}
#
# def fibonacci(n):
#     global count, call
#     if n == 0:
#         count += 1
#         return 0
#     if n == 1:
#         count += 1
#         call += 1
#         return 1
#     else:
#         count += 1
#         return   fibonacci(n - 1) + fibonacci(n - 2)
#
# for number in numbers:
#     count = 0
#     call = 0
#     res =  fibonacci(number)
#     print("fib({}) = {} calls = {}".format(number, count - 1, call))

# read hours

# a, b = [int (i) for i in input().split()]
#
# #logic
#
# if a > 12 and b < 12:
#     time = (24 - a) + b
# elif a < 12 and b > 12:
#     time = b - a
# elif a == b:
#     time = 24
#
# #print
#
# print("O JOGO DUROU {} HORA(S)".format(time))



#get input

# words = []
#
# for i in range(3):
#
#     words.append(input())
#
# #logic
#
# animals = {'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'},
#                          'mamifero': {'onivoro': 'homem', 'herbivoro':'vaca'}},
#            'invertebrado':{'inseto': {'hematofago': 'pulga', 'herbivoro': 'lagarta'},
#                            'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}}
#
#
# #print
#
# print(animals[words[0]][words[1]][words[2]])




# #get the user's input
#
# ddd = int(input())
#
# #logic
#
# cities = {61:'Brasilia', 71:'Salvador', 11:'Sao Paulo',
#           21:'Rio de Janeiro', 32:'Juiz de Fora', 19:'Campinas',
#           27:'Vitoria', 31:'Belo Horizonte'}
#
# #print
#
# if ddd in cities:
#     print("{}".format(cities[ddd]))
# else:
#     print("DDD nao cadastrado")


#get the user's input
#logic

# numbers = []
# numbers2 = []
# count = 0
# soma = 0
#
# for i in range(6):
#     numbers.append(float(input()))
#     if numbers[i] >=0:
#         count +=1
#         numbers2.append(numbers[i])
#
# for j in range(len(numbers2)):
#     soma += numbers2[j]
#
# print("{} valores positivos".format(count)+"\n{:.1f}".format(soma/len(numbers2)))

#read data

# numbers = []
# counter = 0
#
# for i in range(5):
#     numbers.append(int(input()))
#     if numbers[i] % 2 == 0:
#         counter += 1
#
# #print
#
# print("{} valores pares".format(counter))

# read data
#
# number = int(input())
#
# #logic
# def fibonnaci2(number):
#     number1 = 0
#     number2 = 1
#
#     if number == 1:
#         print(number - 1)
#     elif number == 2:
#         print(number -1, number)
#     else:
#         print("0 1", end= ' ')
#         number1 = 1
#         number2 = 0
#         for i in range (number-2):
#             rest = number1 + number2
#             number2 = number1
#             number1 = rest
#             if i == number-3:
#                 print(rest)
#                 break
#             print(rest, end=' ')
# if number > 0 and number < 47:
#     fibonnaci2(number)

# get values
#
# x, y = [int(i) for i in input().split(" ")]
#
# # logic
#
# numbers = []
#
# while(x != 0 or x < 0 or y !=0 or y <0):
#     numbers
#
#     if x < y:
#         for i in range(y - (x - 1)):
#             #print("{}".format(x), end=' ')
#             x += 1
#             numbers.
#     elif y < x:
#         for i in range(x - (y-1)):
#             #print("{}".format(y), end=' ')
#             y += 1
#     x, y = [int(i) for i in input().split(" ")]



#get values

true = True

counter = 0

while true:
    try:
        c = int(input())
    except (EOFError):
        break

