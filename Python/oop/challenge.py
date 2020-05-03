# #create a table for within a dictionary
#
# price_table = {1: ("Cachorro Quente", 4.00),
#                2: ("X-Salada", 4.50),
#                3: ("X-Bacon", 5.00),
#                4: ("Torrada simples", 2.00),
#                5: ("Refrigerante", 1.50)}
#
# #get user's input
# x, y = [int(i) for i in input().split()]
#
# for fast_food in price_table:
#     if x == fast_food:
#         total = (price_table.get(x)[1] * y)
#         print("Total: R$ {:.2f}".format(total))

# Read four numbers (N1, N2, N3, N4), which one with 1 digit after
# the decimal point, corresponding to 4 scores obtained by a student.
# Calculate the average with weights 2, 3, 4 e 1 respectively,
# for these 4 scores and print the message "Media: " (Average),
# followed by the calculated result. If the average was 7.0 or more,
# print the message "Aluno aprovado." (Approved Student).
# If the average was less than 5.0, print the message: "Aluno reprovado."
# (Reproved Student). If the average was between 5.0 and 6.9, including
# these, the program must print the message "Aluno em exame."
# (In exam student).
#
# In case of exam, read one more score. Print the message "Nota do exame: " \
# "" (Exam score) followed by the typed score. Recalculate the average
# (sum the exam score with the previous calculated average and divide by 2)
# and print the message “Aluno aprovado.” (Approved student) in case of average 5.0 or more)
# or "Aluno reprovado." (Reproved student) in case of average 4.9 or less. For these 2 cases
# (approved or reproved after the exam) print the message "Media final: "
# (Final average) followed by the final average for this student in the last line.

# #read number
#
# N1, N2, N3, N4 = [float(i) for i in input().split()]
#
# #Calculate average
#
# average = (N1*2 + N2*3 + N3*4 + N4*1) / 10
#
# #Print result
#
# print("Media: {:.1f}".format(average))
# if average >= 7.0:
#     print("Aluno aprovado.")
# if average < 5.0:
#     print("Aluno reprovado.")
# if 5.0 <= average <= 6.9:
#     print("Aluno em exame.")
#     exame = float(input())
#     print("Nota do exame: {}".format(exame))
#     average2 = (exame+average)/2
#     if average2 >= 5:
#         print("Aluno aprovado.")
#         print("Media final: {:.1f}".format(average2))
#     else:
#         print("Aluno reprovado.")
#         print("Media final: {:.1f}".format(average2))

# Write an algorithm that reads two floating values (x and y), which should represent
# the coordinates of a point in a plane. Next, determine which quadrant the point belongs,
# or if you are over one of the Cartesian axes or the origin (x = y = 0).
#
#
#
# If the point is at the origin, write the message "Origem".
#
# If the point is over X axis write "Eixo X", else if the point is over Y axis write "Eixo Y".
#
# Input
# The input contains the coordinates of a point.
#
# Output
# The output should display the quadrant in which the point is.

# read float number

# x, y = [float(i) for i in input().split()]
#
# #logic
#
# if x == 0 and y == 0:
#     print("Origem")
# elif x == 0:
#     print("Eixo Y")
# elif y == 0:
#     print("Eixo X")
# elif y > 0 and x > 0:
#     print("Q1")
# elif y > 0 and x < 0:
#     print("Q2")
# elif y < 0 and x > 0:
#     print("Q4")
# elif y < 0 and x < 0:
#     print("Q3")

# Read three integers and sort them in ascending order.
# After, print these values in ascending order, a blank line and then
# the values in the sequence as they were readed.
#
# Input
# The input contains three integer numbers.
#
# Output
# Present the output as requested above.

# Read three integers

# a, b, c = [int(i) for i in input().split()]
#
# list_numbers = [a, b, c]


# logic using Bubble Sort

# def orderLIst(list_numbers):
#     for i in range(len(list_numbers) - 1, 0, - 1):
#         for j in range(i):
#             if list_numbers[j] > list_numbers[j + 1]:
#                 aux = list_numbers[j]
#                 list_numbers[j] = list_numbers[j + 1]
#                 list_numbers[j + 1] = aux
#
#
# # print
# list_numbers2 = list(list_numbers)
#
# # orderLIst(list_numbers)
# # print("{}\n{}\n{}".format(list_numbers[0], list_numbers[1], list_numbers[2]))
# print("")
# print("{}\n{}\n{}".format(list_numbers2[0], list_numbers2[1], list_numbers2[2]))

#
# Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange
# them in decreasing order, so that the side A is the biggest of the three sides.
# Next, determine the type of triangle that they can make, based on the following
# cases always writing an appropriate message:
# if A ≥ B + C, write the message: NAO FORMA TRIANGULO
# if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
# if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
# if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
# if the three sides are the same size, write the message: TRIANGULO EQUILATERO
# if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
# Input
# The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).
#
# Output
# Print all the classifications of the triangle presented in the input.


#read three numbers
#
# a, b, c = [float(i) for i in input().split()]
#
# #rearrange in decreasing order
# list_sorted = sorted([a, b, c], reverse=True)
#
# a, b, c = list_sorted[0], list_sorted[1], list_sorted[2]
#
# #print
#
# if a >= b + c:
#     print("NAO FORMA TRIANGULO")
# else:
#     if pow(a, 2) == pow(b, 2) + pow(c, 2):
#         print("TRIANGULO RETANGULO")
#     if pow(a, 2) > pow(b, 2) + pow(c, 2):
#         print("TRIANGULO OBTUSANGULO")
#     if pow(a, 2) < pow(b, 2) + pow(c, 2):
#         print("TRIANGULO ACUTANGULO")
#     if a == b and a == c and b == c:
#         print("TRIANGULO EQUILATERO")
#     if a == b and a != c or a == c and a != b or b == c and a != b:
#         print("TRIANGULO ISOSCELES")


# read

n = int(input())

# store in a list

words_list = []

for i in range(n):
    words_list.append(list(input()))

# logic

for words in words_list:
    for i in range(len(words)):
        if 64 < ord(words[i]) < 123:
            words[i] = chr(ord(words[i]) + 3)
    words.reverse()

    for i in range(len(words)//2, len(words)):
        words[i] = chr(ord(words[i]) - 1)
    print("".join(words))


































