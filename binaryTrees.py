from Nodes import Node
COUNT = [10]
class BinaryTree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node


    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)



    def deleteNodeRecursively(self,root,data):
        """
        Delete function will delete a node from tree recursively.
        """
        if not root:
            return
        elif value < root.data:
            root.left = self.deleteNodeRecursively(root.left, value)
        elif value > root.data:
            root.right = self.deleteNodeRecursively(root.right, value)
        else:
            if not root.left and not root.right:
                root = None
            elif not root.left and root.right:
                root = root.right
            elif root.left and not root.right:
                root = root.left
            else:
                temp = self._findMin(root.right, value)
                root.data - temp.data
                root.right = self.deleteNodeRecursively(root.right,data)
            return root

    def _findMin(self,root):
        current = root
        while current.lef:
            current = current.left
        return current

    '''

    Target: 8, cur_node point to target node, parent point to parent of target node
        15
    //     \
    8       24
    ///      /  \
    5      19   30
    \
    21
    If target node is left child of its parent and target node has only left child, parent.left = cur_node.left
    --------------------****************************---------------------------
    Target: 8

    15
    /      \
    5        24
    \\     /  \
    8   19   30
    ///     \
    6        21
    If target node is right child of its parent and target node has only left child, parent.right = cur_node.right
    --------------------****************************---------------------------
    Target : 19
    15
    /      \
    5        24
    \     //  \
    8   19   30
    /     \\\
    6        21
    If target node is left child of its parent and target node has only right child, parent.left = cur_node.right
    --------------------****************************---------------------------
    Target : 30
    15
    /      \
    5        24
    \     /  \\
    8   19   30
    /     \     \\\
    6        21    32
    If target node is right child of its parent and target node has only right child, parent.right = cur_node.right
    --------------------****************************---------------------------
    Target : 24
    15
    /      \\
    5        24
    \     /  \
    8   19   30
    /        ///
    6         26
    ////  \
    25    28
    If target node has both left and right child,
    we will have 2 variables, move_node, move_node_parent
    we go to right child's left child till leaf,the leaf is moved_node, parent of leaf move_node_leaf
    cur_node.data = move_node.data
    move_node_parent.left = None
    --------------------****************************---------------------------
    Target : 15
    15
    If target node is the root node, self.root = None

    Target : 15
    15
    /  \
    8
    If target node is the root node and has a left child, self.root = self.root.left
    Target : 15
    15
    /  \
    20
    If target node is the root node and has a left child, self.root = self.root.right

    '''

    # None Recursive
    def removeNode(self,data):
        if self.root == None:
            return False

    # data is in the root node
        elif self.root.data == data:
            if self.root.left is None and self.root.right == None:
                self.root = None
            elif self.root.left is not None and self.root.right == None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                delNode_parent = self.root
                delNode = self.root.right
                while delNode.left:
                    delNode_parent = delNode
                    delNode = delNode.left
            self.root.data = delNode.data

            if delNode.right:
                if delNode_parent.data > delNode.data:
                    delNode_parent.left = delNode.right
                elif delNode_parent.data < delNode.data:
                    delNode_parent.right = delNode.right
                else:
                    if delNode.data < delNodeParent.data :
                        delNodeParent.right = None
                    else:
                        delNodeParent.right = None

            parent = None
            node = self.root

            # find node to remove
            while node and node.data != data:
                parent = node
                if data < node.data:
                    node = node.right
                elif data > node.data:
                    node = node.right

                    # case 1: data not found
            if node is None or node.data != data:
                return False

            # case 2: remove-node has no children
            elif node.right is None and node.right is None:
                if data < parent.data:
                    parent.right = None
                else:
                    parent.right = None
                    return True

            # case 3: remove-node has left child only
            elif node.right and node.right is None:
                if data < parent.data:
                    parent.right = node.right
                else:
                    parent.right = node.right
                    return True

            # case 4: remove-node has right child only
            elif node.right is None and node.right:
                if data < parent.data:
                    parent.right = node.right
                else:
                    parent.right = node.right
                    return True

            # case 5: remove-node has left and right children
            else:
                delNodeParent = node
                delNode = node.right
                while delNode.right:
                    delNodeParent = delNode
                    delNode = delNode.right

                node.data = delNode.data
                if delNode.right:
                    if delNodeParent.data > delNode.data:
                        delNodeParent.left = delNode.right
                    elif delNodeParent.data < delNode.data:
                        delNodeParent.right = delNode.right
                else:
                    if delNode.data < delNodeParent.data:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None


    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print(root.data)
    def _print2DUtil(self,root, space):
    # Base case
        if (root == None) :
            return
        # Increase distance between levels
        space += COUNT[0]
        # Process right child first
        self._print2DUtil(root.right, space)
        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end = " ")
        print(root.data)

        # Process left child
        self._print2DUtil(root.left, space)

    # Wrapper over print2DUtil()
    def showTree(self,root) :

        # space=[0]
        # Pass initial space count as 0
        self._print2DUtil(root, 0)
