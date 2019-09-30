class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def getdistinctelements(llist_1):

    set1 = set()
    if llist_1 is None:
        return set1

    node = llist_1.head

    while node:
        set1.add(node.value)
        node = node.next

    return set1


def union(llist_1, llist_2):
    # Your Solution Here

    if llist_1 is None and llist_2 is None:
        return

    set1 = getdistinctelements(llist_1)
    set2 = getdistinctelements(llist_2)

    union_elements = set1.union(set2)

    #print(union_elements)

    union_llist = LinkedList()

    for i in union_elements:
        union_llist.append(i)

    return union_llist


def intersection(llist_1, llist_2):

    if llist_1 is None and llist_2 is None:
        return

    set1 = getdistinctelements(llist_1)
    set2 = getdistinctelements(llist_2)

    int_elements = set1.intersection(set2)

    #print(int_elements)

    result_llist = LinkedList()
    for key in int_elements:
        result_llist.append(key)

    return result_llist


print("Testcase 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

print("Test case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
#
print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

#
print("Test case 3")
print(union(LinkedList(), LinkedList()))
print(intersection(LinkedList(), LinkedList()))

print("Test case 4")
print(union(None, None))
print(intersection(None, None))

print("Test case 5")
print(union(linked_list_3, None))
print(intersection(linked_list_3, None))
