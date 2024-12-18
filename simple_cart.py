items = []
prices = []
total = 0

item = items.append(input('Please input items, (q for quit): '))
price = prices.append(float(input('Please fill out the price: $')))


print('--- Your CART ---')
for item in items:
    print(item, end=' ')

for price in prices:
    total += price

print(f', Your Total Price is: {total}')
