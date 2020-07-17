"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):

        # if self.length == 0:
        #     new_node = ListNode(value)
        #     self.head = new_node
        #     self.tail = new_node
        #     self.length += 1
        # else:
        #     current_head = self.head
        #     new_node = ListNode(value)
        #     new_node.next = current_head
        #     current_head.prev = new_node
        #     self.head = new_node
        #     self.length += 1

        # if self.length == 0:
        #     self.tail = new_node
        # else:
        #     current_head = self.head
        #     new_node.next = current_head
        #     current_head.prev = new_node


        # Wrap the given value in a ListNode called 'new_node'
        new_node = ListNode(value)

        # check to see if there's no head (AKA: empty list)
        if not self.head:
            # if no head, set tail to 'new_node'
            self.tail = new_node
        else:
            # if head does exist, old head becomes new head's next pointer
            new_node.next = self.head
            # and old head's previous pointer is the new node
            self.head.prev = new_node

        # insert 'new_node' as the new head of the list
        self.head = new_node
        # increase length of list by 1 each time
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):

        # if self.length == 0:
        #     return None

        # elif self.length == 1:
        #     current_head = self.head
        #     self.head = None
        #     self.tail = None
        #     self.length -= 1
        #     self.delete(current_head)
        #     value = current_head.value
        #     return value
        # else:
        #     current_head = self.head
        #     self.head = current_head.next
        #     self.length -= 1
        #     self.delete(current_head)
        #     value = current_head.value
        #     return value


        # assign old head's value to a variable so we can return it
        value = self.head.value
        # call delete function on the head (this will also make old head's
        #. next pointer the new head)
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):

        # if self.length == 0:
        #     new_node = ListNode(value)
        #     self.head = new_node
        #     self.tail = new_node
        #     self.length += 1
        # else:
        #     current_tail = self.tail
        #     new_node = ListNode(value)
        #     new_node.prev = current_tail
        #     current_tail.next = new_node
        #     self.tail = new_node
        #     self.length += 1


        # Wrap given value in a ListNode
        new_node = ListNode(value)

        # Check to see if list has no head (AKA: if it's an empty list)
        if not self.tail:
            # if no tail, 'new_node' becomes head as well as tail
            self.head = new_node
        else:
            # if tail exists, old tail becomes the new_node's previous pointer
            new_node.prev = self.tail
            # old tail's next pointer is the new node
            self.tail.next = new_node

        # insert 'new_node' as the new tail of the list
        self.tail = new_node
        # increase length of list by 1 each time
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):

        # if self.length == 0:
        #     return None
        # elif self.length == 1:
        #     current_tail = self.tail
        #     self.head = None
        #     self.tail = None
        #     self.length -= 1
        #     self.delete(current_tail)
        #     value = current_tail.value
        #     return value
        # else:
        #     current_tail = self.tail
        #     self.tail = current_tail.prev
        #     self.length -= 1
        #     self.delete(current_tail)
        #     value = current_tail.value
        #     return value


        # assign old tail's value to a variable so we can return it
        value = self.tail.value
        # call delete function on the tail (this will also make old tail's
        #. prev pointer the new tail)
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        
        # check to see if the node given is the head. If it is, do nothing.
        if node == self.head:
            return None
        # Otherwise:
        else:
            # save the value of the given node to a variable
            value = node.value
            # delete the node given
            self.delete(node)
            # use value above to make a new node and add it as the head
            self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        
        # check to see if the node given is the tail. If it is, do nothing.
        if node == self.tail:
            return None
        # Otherwise:
        else:
            # save the value of the given node to a variable
            value = node.value
            # delete the node given
            self.delete(node)
            # use value above to make a new node and add it as the tail
            self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):

        # if self.length == 0:
        #     return None
        # elif self.length == 1:
        #     self.head = None
        #     self.tail = None
        #     self.length -= 1
        # elif node == self.head:
        #     self.head = node.next
        #     self.length -= 1
        # elif node == self.tail:
        #     self.tail = node.prev
        #     self.length -= 1
        # else:
        #     node.delete()
        #     self.length -= 1


        # Check to see if there's no head (AKA: empty list). If so, do nothing.
        if not self.head:
            return None

        # if the head equals the tail (AKA: 1 node in list), both head and tail 
        #. will not be None
        elif self.head == self.tail:
            self.head = self.tail = None

        # if the node given is the head, set the new head to the given node's
        #. next pointer
        elif node == self.head:
            self.head = node.next

        # if the node given is the tail, set the new tail to the given node's
        #. prev pointer
        elif node == self.tail:
            self.tail = node.prev

        # Otherwise, delete that node and the functionality in the ListNode
        #. class delete() functionality will take care of the rest
        else:
            node.delete()

        # Decrease the length of the linked list by 1 every time.
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        if not self.head:
            return None

        # reference to the largest value we've seen so far
        max_value = self.head.value

        # reference to our current node as we traverse the list
        current = self.head.next

        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next

        return max_value