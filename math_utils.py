def add(a, b):

 return a + b

def subtract(a, b):

 return a - b

2. Crie um arquivo `test_math_utils.py` com os testes:

from math_utils import add, subtract

def test_add():

 assert add(2, 3) == 5

def test_subtract():

 assert subtract(5, 2) == 3


