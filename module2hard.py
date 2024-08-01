from random import randint
import math

#разделение числа на сумму 2х слагаемых
def get_summands( number):
    summands = []
    for ii in range(1, number):
        sum1 = number - ii #одно слагаемое
        if [sum1, ii] in summands or sum1 == ii: #одинаковые числа в парах недопустимы
            continue
        else:
            summands.append([ii, sum1])
    return summands

def get_dividers(number): #список делителей числа number
    dividers = []
    for ii in range(1, int(math.sqrt(number))+1):
        if number % ii == 0:
            if ii > 1: #единицу не представить как сумму 2х чисел
                dividers.append(ii)
            result = number // ii
            if ii != result:
                dividers.append(result)
    return dividers

num = randint(3, 20)
print('Первое число ', num)
div_list = get_dividers(num) #нашли делители числа
print(f"Делителя числв {num} отличные от 1:", *div_list)
result = ''
for each in div_list:
    couples = get_summands(each) #раскладываем каждый делитель на сумму 2х чисел
    if len(couples) > 0:
        for item in couples:
            result += str(item[0]) + str(item[1])
            #print(*item)

print('Пароль :', result)






