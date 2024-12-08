class SomeObject:
    def __init__(self, value=''):
        self.some_value = value
        self.__useless_property = None

    def __str__(self):
        return str(self.some_value)

    def __compare_some_value(self, other):
        if type(other) != SomeObject:
            raise Exception('Cannot compare objects of different types')
        self_value = str(self.some_value)
        other_value = str(other.some_value)

        if len(self_value) > len(other_value):
            return 1
        if len(self_value) < len(other_value):
            return -1

        for i in range(len(self_value)):
            if self_value[i] > other_value[i]:
                return 1
            if self_value[i] < other_value[i]:
                return -1

        return 0

    def __eq__(self, other):
        return self.__compare_some_value(other) == 0

    def __gt__(self, other):
        return self.__compare_some_value(other) > 0

    def __ge__(self, other):
        return self.__compare_some_value(other) > -1

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    @property
    def useless_property(self):
        print(f'I will return useless property value ({self.__useless_property})')
        return self.__useless_property

    @useless_property.setter
    def useless_property(self, value):
        print(f'I will set useless property to {value}')
        self.__useless_property = value

o1 = SomeObject("World")
o2 = SomeObject('world')

o1.useless_property = 'Something'

print(o1.useless_property)
