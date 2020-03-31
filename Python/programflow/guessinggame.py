import random

highest = 1000000000000
answer = random.randint(1, highest)

print(answer)  # TODO: Remove after testing

# print("Please guess number between 1 and {0} : ".format(highest))
# guess = int(input())

exit = 1

# while exit != 0:
#
#     print("Please guess number between 1 and {0} or 0 to quit: ".format(highest))
#     guess = int(input())
#     if guess == 0:
#         break
#
#     if guess == answer:
#         print("You got it!")
#         exit = 0
#
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         else:
#             print("Please guess lower")
#

guess = 0

print("Please guess number between 1 and {0} or 0 to quit: ".format(highest))

while guess != answer:
    
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("You got it!")
        break

    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
