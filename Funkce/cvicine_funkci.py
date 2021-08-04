import random


# 1
def mult(a, b):
    c = a * b
    return c


# 2
def total_price(persons, breakfast=False):
    if breakfast:
        price = persons * 1000
    else:
        price = persons * 850
    return price


print(total_price(3))
print(total_price(2, True))


# 3
def month_of_birth(rodne_cislo):
    month = rodne_cislo[2] + rodne_cislo[3]
    if int(month) > 12:
        women_month = int(month) - 50
        return women_month
    else:
        return month


print(month_of_birth("9562125899"))


# 4
def rouleta(users_serial_number, rate):
    users_serial_number = int(users_serial_number)
    win_number = random.randint(1, 36)
    if users_serial_number != 0:
        if win_number % 3 == 1 and users_serial_number % 3 == 1:
            rate *= 2
            print("vyhrála prvni")
        elif win_number % 3 == 2 and users_serial_number % 3 == 2:
            rate *= 2
            print("vyhrála druha")
        elif win_number % 3 == 0 and users_serial_number % 3 == 0:
            rate *= 2
            print("vyhrála treti")
        else:
            rate = 0
    else:
        rate = 0
    return rate


game_result = rouleta(input("Na kterou ze tří řad sázes "), int(input("výši sázky ")))
print(game_result)