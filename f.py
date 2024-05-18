price = 0
ticket = (int(input('Введите количество билетов, которое хотите приобрести: ')))
for age in range(ticket):
    age = (int(input('Введите ваш возраст: ')))
    if age < 18:
        price += 0
    elif age >= 18 and age <=25:
        price += 990
    elif age > 25:
        price += 1390
if price == 0:
    print('Бесплатное посещение')
else:
    print('Сумма к оплате -', price)
    if ticket > 3:
        discount = price / 100 * 10
        print('Скидка 10% -', int(discount))
        print('Сумма к оплате -', int(price - discount))