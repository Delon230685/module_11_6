def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = []
    for attr in attributes:
        attribute_value = getattr(obj, attr)
        if callable(attribute_value):
            methods.append(attr)
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': None}
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    return info

class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value

my_obj = MyClass(10)

class_info = introspection_info(my_obj)
print(class_info)

number_info = introspection_info(42)
print(number_info)