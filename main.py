from linked_list import LinkedList

my_linked_list = LinkedList()

#print(my_linked_list.head)

my_linked_list.insert_node(8)
my_linked_list.insert_node(5)
my_linked_list.insert_node(6)
my_linked_list.insert_node(9)
my_linked_list.insert_node(11)

#print(my_linked_list.head.value, end=" ")
#print(my_linked_list.head.next_node.next_node.next_node.value)
#print(my_linked_list.print_list_item())

my_linked_list.print_list_item()
#print(my_linked_list.count_nodes(my_linked_list.head))
print(my_linked_list.delete_node(1))
my_linked_list.print_reverse_noarg()
print()
my_linked_list.print_list_item()