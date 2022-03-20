import sys
sys.path.append(".")
from nest import obj
def test_json1():
    test1 = obj('{"a":{"b":{"c":"d"}}}', 'a/b/c')
    assert test1.json_value() == 'd', 'Should be d'
def test_json2():
    test2 = obj('{"x":{"y":{"z":"a"}}}', 'x/y/z')
    assert test2.json_value() == 'a', 'Should be a'
