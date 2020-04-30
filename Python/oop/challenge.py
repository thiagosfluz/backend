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

a, b, c = [int(i) for i in input().split()]

list_numbers = [a, b, c]


# logic using Bubble Sort

def orderLIst(list_numbers):
    for i in range(len(list_numbers) - 1, 0, - 1):
        for j in range(i):
            if list_numbers[j] > list_numbers[j + 1]:
                aux = list_numbers[j]
                list_numbers[j] = list_numbers[j + 1]
                list_numbers[j + 1] = aux


# print
list_numbers2 = list(list_numbers)

orderLIst(list_numbers)
print("{}\n{}\n{}".format(list_numbers[0], list_numbers[1], list_numbers[2]))
print("")
print("{}\n{}\n{}".format(list_numbers2[0], list_numbers2[1], list_numbers2[2]))