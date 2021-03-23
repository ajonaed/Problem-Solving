from Nodes import Node
from collections import deque
COUNT = [10]

class SearchingWay:


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

    def BFS(self,root):
        result = []
        q = deque()
        if root is None:
            return 'No Tree Found!'
        else:
            q.append(root)
            while q:
                cur = q.popleft()
                result.append(cur.data)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            return result

    def BFSRecursive(self,root):
        if root is None:
            return 'No Tree Found!'
        else:
            # Initiate the Queue
            Q = deque()
            # Push the root into Queue
            Q.append(root)
            # Initiate the List (Optional)
            l= []
            #call the helper Function
            return self._helpBFS(Q,l)

    def _helpBFS(self,q,l):
        # Base Case = if Queue is empty then return or return the list
        if (not q):
            return l
        else:
            # Pop the first item and store it to a Node
            cur = q.popleft()
            # append the Node value in the list, we can just print here
            l.append(cur.data)
            #Now Check whether if cur node has a left child
            if cur.left:
                #if yes, push the left child into the Queue
                q.append(cur.left)
            #Now Check whether if cur node has a right child
            if cur.right:
                #if yes, push the right child into the Queue
                q.append(cur.right)
            # Call Start Recursive call
            return self._helpBFS(q,l)

    def DFS(self,root):

        return
    def inorderTraverse(self,root):
        if root is not None:
            self.inorderTraverse(root.left)
            print(root.data, end=" -> ")
            self.inorderTraverse(root.right)


    def showList(self,root):
        self._printList(root)

    def _printList(self,root):
        if root is not None:
            print(root.data, end = " ")
            self._printList(root.left)
            self._printList(root.right)

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
