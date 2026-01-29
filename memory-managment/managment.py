import gc
class MyObject:
    def __init__(self,name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} deleted")

# create circular reference
obj1 = MyObject("obj1")
obj2 = MyObject("obj2")

obj1.ref = obj2
obj2.ref = obj1

# del obj1
# del obj2

# manually trigger the garbage collection
# gc.collect()