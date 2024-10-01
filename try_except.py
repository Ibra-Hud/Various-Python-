# Type your code here.
# set PYTHONPATH="c:\dir1;c:\other\directory".
import Interstate Identifier

user_num = input()
div_num = input()

try:
    value = int(user_num)//int(div_num)
    print(value)
except (ZeroDivisionError):
    print(f'Zero Division Exception: integer division or modulo by zero')
except ValueError as x:
    print(f'Input Exception: {x}')