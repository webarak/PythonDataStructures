from stack import Stack
import time
import math

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            return
        else:
            new_pointer = self.head
            while (new_pointer.next):
                new_pointer = new_pointer.next
            new_pointer.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_pointer = self.head
        new_node.next = new_pointer
        self.head = new_node


    def insert_after_node(self, prev_node, data):
        if (prev_node is None):
            print("there is not a prev node")
            return
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_node(self, value):
        temp_node = self.head
        if (temp_node and temp_node.data == value):
            self.head = temp_node.next
            temp_node = None
            return

        prev = None
        while (temp_node and temp_node.data!=value):
            prev = temp_node
            temp_node = temp_node.next

        if (temp_node == None):
            return

        prev.next = temp_node.next
        temp_node = None

    def delete_node_at_pos(self, pos):
        temp_node = self.head
        if (pos == 0 and temp_node):
            self.head = temp_node.next
            return
        elif (pos == 1 and temp_node.next):
            self.head.next = temp_node.next.next
            return

        count = 2
        prev_node = self.head
        if (temp_node):
            temp_node = temp_node.next
        while (count<pos and temp_node):
            temp_node = temp_node.next
            prev_node = prev_node.next
            count+=1
        if (temp_node):
            prev_node.next = temp_node.next
        else:
            print("pos isn't exist")

    def len_iterative(self):
        count = 0
        temp_node = self.head
        while(temp_node):
            count+=1
            temp_node = temp_node.next
        return count

    def len_recursive(self, node):
        if (not node):
            return 0
        return self.len_recursive(node.next) + 1


    def swap_nodes(self, key_1, key_2):
        node_1 = LinkedList()
        node_2 = LinkedList()
        temp_node = self.head
        while(temp_node):
            if (temp_node.data==key_1):
                node_1 = temp_node
            elif (temp_node.data == key_2):
                node_2 = temp_node
            temp_node = temp_node.next
        if (node_1 and node_2 and key_2!=key_1):
            node_1.data = key_2
            node_2.data = key_1
        else:
            print("one of the keys doesnt exsist")

    def swap_nodes_not_me(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next


    def reverse_iterative(self):
        original_node = self.head
        reverse_order = Stack()
        temp_node = None

        while (original_node):
            reverse_order.push(Node(original_node.data))
            original_node = original_node.next

        if (not reverse_order.is_empty()):
            temp_node = reverse_order.pop()
        original_node = temp_node

        while(not reverse_order.is_empty()):
            temp_node.next = reverse_order.pop()
            temp_node = temp_node.next

        self.head = original_node

    def get_data(self):
        return self.head.data

    def get_next(self):
        return self.head.next

    def set_next(self, node):
        self.head.next = Node(node)

    def merge_sorted(self, LLIST):
        original = self.head
        another_list = LLIST.head
        merge = LinkedList()
        merge.append(Node(-1))
        temp = merge.head

        while original and another_list:
            if another_list.data > original.data:
                temp.next = Node(original.data)
                original = original.next
            elif another_list.data < original.data:
                temp.next = Node(another_list.data)
                another_list = another_list.next
            else:
                temp.next = Node(original.data)
                another_list = another_list.next
                original = original.next
            temp = temp.next
        if original:
            while original:
                temp.next = Node(original.data)
                temp = temp.next
                original = original.next
        if another_list:
            while another_list:
                temp.next = Node(another_list.data)
                temp = temp.next
                another_list = another_list.next

        self.head = merge.get_next()

    def remove_duplicates(self):
        original = self.head
        list_of_no_duplicates = []

        while original:
            if not original.data in list_of_no_duplicates:
                list_of_no_duplicates.append(original.data)
            original = original.next
        original = LinkedList()
        for i in list_of_no_duplicates:
            original.append(i)
        self.head = original.head

    def print_nth_from_last(self, num_from_end):
        num = self.len_iterative()
        if num_from_end>num or num_from_end<=0 or self.head == None:
            print("there isn't such node as asked")
        else:
            original = self.head
            for i in range(num-num_from_end):
                original = original.next
            print(original.data)

    def count_occurences_iterative(self, data):
        count = 0
        original = self.head
        while original:
            if original.data == data:
                count+=1
            original = original.next
        return count

    def count_occurences_recursive(self, data, node):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(data, node.next)
        return self.count_occurences_recursive(data, node.next)

    def rotate(self, pos):
        pivot = self.head
        end = self.head
        count = 0
        if self.len_iterative() < pos or pos <= 0 :
            print("pos isn't ok")
        else:
            while end.next:
                count+=1
                if count == pos:
                    pivot = end
                end = end.next
            end.next = self.head
            self.head = pivot.next
            pivot.next = None

    def is_palindrome_string(self):
        original = self.head
        pilandrom = ""
        while original:
            pilandrom += str(original.data)
            original = original.next
        if pilandrom == pilandrom[::-1]:
            return True
        return False

    def is_palindrome_stack(self):
        original = self.head
        length = self.len_iterative()
        palindrome = Stack()
        if not original:
            return True
        if length%2 == 0:
            for i in range(int(length/2)):
                palindrome.push(original.data)
                original = original.next
            for i in range(int(length/2)):
                if (palindrome.peek() != original.data):
                    return False
            return True
        else:
            for i in range(int(length/2)):
                palindrome.push(original.data)
                original = original.next
            original = original.next
            for i in range(int(length/2)):
                if (palindrome.peek() != original.data):
                    return False
            return True

    def is_palindrome_Two_Pointers(self):
        original = self.head
        self.reverse_iterative()
        temp = self.head
        self.reverse_iterative()
        if not original:
            return True
        while original:
            if temp.data != original.data:
                return False
            original = original.next
            temp = temp.next
        return True

    def move_tail_to_head(self):
        length = self.len_iterative()
        self.rotate(length-1)

    def calculate_sum_by_tens_power(self):
        count = 0
        sum = 0
        original = self.head
        while original:
            sum += original.data*math.pow(10, count)
            original = original.next
            count+=1
        return sum

    def sum_two_lists(self, llist):
        original = self
        temp = llist
        sum_node = LinkedList()
        sum = int(original.calculate_sum_by_tens_power() + temp.calculate_sum_by_tens_power())
        length_sum = len(str(sum))
        for i in range(length_sum):
            sum_node.append(sum%10)
            sum = int(sum / 10)
        sum_node.print()

    def print(self):
        new_pointer = self.head
        while (new_pointer):
            print(new_pointer.data)
            new_pointer = new_pointer.next



llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365 + 248)
print(365 + 248)
llist1.sum_two_lists(llist2)
