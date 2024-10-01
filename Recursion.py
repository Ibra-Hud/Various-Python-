
user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor < 0:
            # Possible NameError
            # compute() is not defined
            print(compute(divisor), end=' ')
        else:
            # Possible ZeroDivisionError
            print(20 // divisor, end=' ')     # // truncates to an integer
    except ValueError:
        print('v', end=' ')
    except ZeroDivisionError:
        print('z', end=' ')
    except:
        print('x', end=' ')
    user_input = input()
print('OK')