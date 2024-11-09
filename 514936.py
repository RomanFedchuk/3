import requests

def my_function():
    pass


print(__name__)
print(requests.__name__)
print(my_function.__name__)

for item in dir():
    print(item)

    word = 'hello'
    print(hasattr(word, 'upper'))
    print(hasattr(word, 'uppercase'))
    print(word.upper())

    print(callable(my_function))
    print(callable(word))

    class A:
        pass

class B(A):
    pass

print(issubclass(B, A))
print(issubclass(A, B))

if isinstance(word, int):
    print(це число)
elif isinstance(word, str):
    print('це стрічка')

import inspect

print(
    inspect.ismodule(requests),
    inspect.isfunction(my_function),
    inspect.isclass(B)
)

import sys

print(sys.version)
print(sys.platform)
print(sys.executable)
print(sys.argv)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)

    for item in dir(__builtins__):
        print(item)


        class C(B)
            pass


        print(issubclass(B, A, C))
        print(issubclass(A, B, C))
        print(issubclass(C, A, B))
        print(issubclass(C, B, A))
