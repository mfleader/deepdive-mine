import os.path, types, sys

module_name = 'module1'
module_file = 'module1_src.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read src from file
with open(module_rel_file_path, 'r') as code_file:
    src = code_file.read()

# create a module object()
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# set a ref in sys.modules
sys.modules[module_name] = mod

# compile src code
code = compile(src, filename=module_abs_file_path, mode='exec')

# execute compiled src code
exec(code, mod.__dict__)

# DONE!

import module1
module1.hello()