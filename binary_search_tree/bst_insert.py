class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < Node's value
        if value < self.value:
            # we need to go left 
            # if we see that there is no left child, 
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the left child's `insert` method 
                self.left.insert(value)
        # otherwise, value >= Node's value 
        else:
            # we need to go right 
            # if we see there is no right child, 
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it 
                self.right = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the right child's `insert` method 
                self.right.insert(value)