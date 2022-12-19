tickets = int(input("какое количество билетов хотите приобрести?"))
totalprice = 0
for i in range(tickets):
    i += 1
    customer_age = int(input("введите возраст посетителя"))
    if customer_age < 18:
           totalprice += 0
    elif 18 <= customer_age < 25:
           totalprice += 990
    else: totalprice += 1390

if tickets > 3:
    totalprice = totalprice - ((totalprice/100*10))
    print("сумма к оплате", int(totalprice), str("руб."))
else:
    print("сумма к оплате", int(totalprice), str("руб."))










