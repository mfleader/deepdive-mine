import sys
print('========================================')

print(f'running main.py - module name: {__name__}')

import module1
# print(module1)
# module1.pprint_dict('main.globals', globals())
# print(sys.path)
# print(sys.modules['module1'])
print('importing module again...')
del globals()['module1']

import module1
module1.pprint_dict('main.globals', globals())

print('========================================')