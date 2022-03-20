sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

w2_last_day_sales = int(input('Input sales of last day of week 2'))
sales_w2.append(w2_last_day_sales)
sales = sales_w1 + sales_w2
print(sales)
print('${}  earned on worst day.'.format(min(sales)*1.5))
print('${}  earned on best day.'.format(max(sales)*1.5))
print('${}  earned in total.'.format(sum(sales)*1.5))

