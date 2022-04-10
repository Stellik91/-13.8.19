num_tickets = int(input("введите количество билетов: "))
tickets = 0
for i in range(num_tickets):
        age = int(input("введите возраст: "))
        i += 1
        if age <18:
            print("0")
        elif 18 < age < 25:
            tickets += 990
            print("990")
        else:
            tickets += 1390
            print("1390")
if num_tickets > 3:
    tickets = tickets*0.9
    print("скидка 10% для 3+ человек: ", tickets)
else:
    print("сумма к оплате: ", tickets)