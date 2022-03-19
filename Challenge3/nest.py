import json
class obj:
    def __init__(self, testName, object, key):
        self.testName = testName
        self.object = object
        self.key = key
    def json_value(self):
        keys = self.key.split('/')
        dict = json.loads(self.object)
        for self.key in keys:
            dict = dict[self.key]
        return dict 
