class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result


def merge_two_sorted_lists(list1, list2):
    merged_list = LinkedList()
    merged_list.head = merged_list._sorted_merge(list1.head, list2.head)
    return merged_list


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')

    print("Створення першого списку:")
    llist1 = LinkedList()
    llist1.insert_at_end(5)
    llist1.insert_at_end(1)
    llist1.insert_at_end(8)
    llist1.insert_at_end(3)
    llist1.print_list()

    print("\nРеверсування списку:")
    llist1.reverse()
    llist1.print_list()

    print("\nСортування списку:")
    llist1.merge_sort()
    llist1.print_list()

    print("\nСтворення другого списку (вже відсортованого для прикладу):")
    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)
    llist2.print_list()

    print("\nОб'єднання двох відсортованих списків:")
    merged = merge_two_sorted_lists(llist1, llist2)
    merged.print_list()
