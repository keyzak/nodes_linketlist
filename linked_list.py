
# class with linked list with all methods

from node import Node

class LinkedList:
    #constructor
    def __init__(self):
        #no argument then self
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        #descending order
        elif self.head.value >= value:  # its same as value <= self.head.value 9 > 1
            new_node.next_node = self.head
            self.head = new_node

        else :
            previous = self.head
            runner = self.head.next_node

            #we dont know how many iterration
            while (runner != None) and (runner.value < value) :
                previous = runner
                runner = runner.next_node

            new_node.next_node = runner
            previous.next_node = new_node



    def print_list_item(self):
        if self.head == None:
            print("empty")

        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end="  ")
                runner = runner.next_node
            print()

 # also another method for count_nodes
    # def count_nodes(self):
    #
    #     count = 0
    #     runner = self.head
    #     while runner is not None:
    #         count +=1
    #         runner = runner.next_node
    #     return count

    # I use that helping method to omit argument 'node'
    def count_nodes(self):
        return self.count_nodes_recursive(self.head)

    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recursive(node.next_node)


    def find_node(self, target_value):
        runner = self.head
        while runner is not None:
            if runner.value is target_value:
                return True
            else:
                runner = runner.next_node
        return False


    def delete_node(self, target_value):
        if self.head is None:
            return False

        #if I want to delete head
        elif self.head.value is target_value:
            self.head = self.head.next_node
            return True
        # if node is in the middle OR on the end
        else:
            previous = self.head
            runner = self.head.next_node
            while (runner is not None) and runner.value != target_value:
                previous = runner
                runner = runner.next_node

            if runner is not None:
                previous.next_node = runner.next_node
                return True

            else:
                return False # dont find value




    def print_reverse(self, node):

        if node is not None:
            self.print_reverse(node=node.next_node)
            print(node.value, end=" ")

    def print_reverse_noarg(self):
        self.print_reverse(self.head)