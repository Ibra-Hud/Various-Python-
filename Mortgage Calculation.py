current_price = int(input('Insert the houses current price: \n'))
last_months_price = int(input('Insert last months price: \n'))

monthly_mortgage = ((current_price * .051)/12)

print(f'This house is ${current_price}. The change is ${current_price - last_months_price} since last month.\nThe estimated monthly mortgage is ${monthly_mortgage:.2f}.')