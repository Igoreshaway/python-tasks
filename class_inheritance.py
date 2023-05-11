class First:

    def get_name(self):
        return 'First'

    @staticmethod
    def get_type():
        return 'Class'


class Second:

    def get_name(self):
        return 'Second'


class Third:

    def get_programming_language(self):
        return 'Python'


class Fourth(First, Second, Third):

    def get_programming_language(self):
        return 'Java'

    @classmethod
    def get_type(cls):
        return 'Class1'


first = First()
second = Second()
third = Third()
fourth = Fourth()
print(fourth.get_name())
print()
print(fourth.get_programming_language())
print()
print(fourth.get_type())
