
#is class for basic pointer with decorators
class Node:
#constructor
    def __init__(self, value, next_node = None):
        self._value = value # not public that why we have getter and setter
        self._next_node = next_node # not public

    @property #getter
    def value(self):
        return  self._value

    @value.setter  #setter
    def value(self, new_value):
        self._value = new_value


    #getter
    @property
    def next_node(self):
        return self._next_node

    #setter
    @next_node.setter
    def next_node(self, next_no):
        self._next_node = next_no


