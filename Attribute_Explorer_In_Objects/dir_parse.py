from pprint import pprint
from faker import Faker
obj = Faker()

for attr in dir(obj):
    val = eval(f'obj.{attr}')
    print(attr)
    pprint(val)
    print()
    print('explanation :')
    val2 = eval(f'obj.{attr}.__doc__')
    print(val2)
    print('--------------------------------------------------')
