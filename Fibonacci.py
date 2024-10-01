def fibonacci(n):
    if n < 0:
        return -1
    else:
        x, y = 0, 1
        count = 0
        while count < n:
            nth = x + y
            x = y
            y = nth
            count += 1
        return x


if __name__ == '__main__':
    start_num = int(input('Enter Nuber: '))
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')