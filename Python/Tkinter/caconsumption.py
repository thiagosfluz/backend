
# x = int(input())
# y = float(input())
#
# total = x/y
#
# print("{:.3f} km/l".format(total))


# from math import sqrt
#
# x1, y1 = [float(i) for i in input().split()]
# x2, y2 = [float(i) for i in input().split()]
#
# distance = sqrt((x2-x1)**2 + (y2-y1)**2)
#
# print("{:.4f}".format(distance))


# km = int(input())
#
# time = 2*km
#
# print("{} minutos".format(time))

# spendttime = int(input())
# speedtime = int(input())
#
# necessaryliters = (spendttime * speedtime) / 12
#
# print("{:.3f}".format(necessaryliters))


# cash = int(input())
#
# if cash % 100 >= 1 or cash % 100 == 0:
#     bill100 = int(cash/100)
# else:
#     bill100 = 0
#
# cash = cash - bill100 *100
#
# if cash % 50 >= 1 or cash % 50 == 0:
#     bill50 = int(cash/50)
# else:
#     bill50= 0
#
# cash = cash - bill50 *50
#
# if cash % 20 >= 1 or cash % 20 == 0:
#     bill20= int(cash /20)
# else:
#     bill20 = 0
#
# cash = cash - bill20 *20
#
# if cash % 10 >= 1 or cash % 10 == 0:
#     bill10 = int(cash /10)
# else:
#     bill10 = 0
#
# cash = cash - bill10 *10
#
# if cash % 5 >= 1 or cash % 5 == 0:
#     bill5 = int(cash /5)
# else:
#     bill5 = 0
#
# cash = cash - bill5 *5
#
# if cash % 2 >= 1 or cash % 2 == 0:
#     bill2 = int(cash /2)
# else:
#     bill2 = 0
#
# cash = cash - bill2 * 2
#
# if cash % 1 >= 1 or cash % 1 == 0:
#     bill1 = int(cash/1)
# else:
#     bill1 = 0
#
# cash = bill100 * 100 + bill50 * 50 + bill20 * 20 + bill5 * 5 + bill2 * 2 + bill1 * 1
#
# print(cash)
# print("{} nota(s) de R$ 100,00".format(bill100))
# print("{} nota(s) de R$ 50,00".format(bill50))
# print("{} nota(s) de R$ 20,00".format(bill20))
# print("{} nota(s) de R$ 10,00".format(bill10))
# print("{} nota(s) de R$ 5,00".format(bill5))
# print("{} nota(s) de R$ 2,00".format(bill2))
# print("{} nota(s) de R$ 1,00".format(bill1))

# # read integer
# eventseconds = int(input())
#
# #transform to hours:minutes:seconds
#
# hour = int(eventseconds/3600)
# minute = int(eventseconds/60) - hour * 60
# second = int(eventseconds) - (minute * 60 + hour * 3600)
#
# #print the result
#
# print("{}:{}:{}".format(hour, minute, second))


#read person's age

# ageindays = int(input())
#
# #convert days to year:month:days
#
# year = int(ageindays/365)
#
# month = int((ageindays%365/30))
#
# days = int(ageindays%365%30)
#
# print("{} ano(s)".format(year))
# print("{} mes(es)".format(month))
# print("{} dia(s)".format(days))


#read input
realamount = float(input())

#read bills and coins
bills = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

#print out bills and coins

print("NOTAS:")
for bill in bills:
    amountbills = realamount//bill
    realamount -= amountbills*bill
    print("{:.0f} nota(s) de R$ {}.00".format(amountbills, bill))


print("MOEDAS:")

for coin in coins:
    amountcoins = realamount//coin
    realamount -= amountcoins*coin
    print("{:.0f} moeda(s) de R$ {:.2f}".format(amountcoins, coin))