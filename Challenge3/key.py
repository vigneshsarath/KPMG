import sys
sys.path.append(".")
from nest import obj
tst1 = obj("Test 1", '{"a":{"b":{"c":"d"}}}', 'a/b/c')
tst2 = obj("Test 2", '{"x":{"y":{"z":"a"}}}', 'x/y/z')
print("The Key is", tst1.json_value())
print("The Key is", tst2.json_value())
