import sys
sys.path.append(".")
from nest import obj
input1 = obj('{"a":{"b":{"c":"d"}}}', 'a/b/c')
input2 = obj('{"x":{"y":{"z":"a"}}}', 'x/y/z')
print("The Key is", input1.json_value())
print("The Key is", input2.json_value())
