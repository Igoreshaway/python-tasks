class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


singleton = Singleton()
singleton2 = Singleton()
print(singleton is singleton2)

print()


class AnotherSingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AnotherSingleton, cls).__new__(cls)
        return cls.instance


another_singleton = AnotherSingleton()
another_singleton2 = AnotherSingleton()
print(another_singleton is another_singleton2)

NewClass = type('NewClass', (Singleton,), {})


class TestMetaClass(type):
    attr1 = 1


class TestClass(metaclass=TestMetaClass):
    attr2 = 2


test = TestClass()
print(type(TestClass))
