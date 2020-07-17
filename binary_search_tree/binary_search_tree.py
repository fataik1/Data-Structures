from queue import Queue

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to root's value to determine which direction
        # . to go
        # if value < root
        if value < self.value:
            # go left
            # Check if there is a left node already
            if self.left:
                # if there is, run insert on self.left
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else value >= root
        else:
            # go right
            # Check if there is a right node already
            if self.right:
                # if there is, run insert on self.right
                self.right.insert(value)
            else:
                # no right node and we can park the value here
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check to see if the root is the target
        if self.value == target:
            return True
        # Otherwise, there is a root Node but it isn't the target,
        # go left or right
        else:
            # if target < root, go left
            if target < self.value:
                # Check to see if there is a left node already
                if self.left:
                    # if there is, run contains (recur) on self.left
                    return self.left.contains(target)

            else:
                # Check to see if there is a right node already
                if self.right:
                    # if there is, run contains (recur) on self.right
                    return self.right.contains(target)

            # if there is no left or right node and target hasn't been found
            #. yet, return False
            return False
    
    
    # Return the maximum value found in the tree

    def get_max(self):
        # Check to see if there is a right node. If there isn't, return the
        #. value
        if not self.right:
            return self.value
        # Otherwise: recur on right side
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call the function 'fn' on the current value
        fn(self.value)
        # Check to see if there is a left node
        if self.left:
            # if there is, make the left node the current value
            self.left.for_each(fn)
        # Check to see if there is a right node
        if self.right:
            # if there is, make the right node the current value
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):

        if node:
            # recur on left child of the node
            node.in_order_print(node.left)
            # print the value of the left child
            print(node.value)
            # recur on right child of the node
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        # breadth first traversal follows FIFO ordering of its nodes
        # init a deque 
        q = []
        # add the first node to our q 
        q.insert(0, node)

        while len(q) > 0:
            # current node is the first node in the q
            current_node = q.pop()
            # print current nodes value
            print(current_node.value)
            
            # if current node has a left child, add it to the beginning of the
            #. queue
            if current_node.left:
              q.insert(0, current_node.left)
            # if current node has a right child, add it to the beginning of the
            #. queue
            if current_node.right:
              q.insert(0, current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # print base case
        print(node.value)
        # Check to see if there is a left node
        if node.left:
            # if there is, run dft_print on left child node
            node.dft_print(node.left)
        # Check to see if there is a right node
        if node.right:
            # if there is, run dft_print on right child node
            node.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass