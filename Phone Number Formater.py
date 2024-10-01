phone_number = int(input('Enter your phone number: \n'))
print(f'({phone_number // 10000000}) {(phone_number // 10000) % 1000}-{phone_number % 10000}')