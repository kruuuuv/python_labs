price = float(input());
discount = float(input());
vat = float(input());
base =  price * (1 - discount/100);
print("База после скидки:  ", base, "₽");
print("НДС:              ", base * (vat/100), "₽");
print("Итого к оплате:    ", base+ base * (vat/100), "₽");