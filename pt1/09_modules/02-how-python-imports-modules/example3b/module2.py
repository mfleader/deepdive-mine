
print('initial run of module2.py')
import module1

def hello():
    print('module2 says hello\nand...')
    print(module1.hello())

