from binaryTrees import BinaryTree

def main():
    root = None
    tree = BinaryTree()
    root = tree.insert(root, 60)
    tree.insert(root, 72)
    tree.insert(root, 30)
    tree.insert(root, 10)
    tree.insert(root, 55)
    tree.insert(root, 38)
    tree.insert(root, 44)
    tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)
    #
    # print("Traverse Preorder")
    # tree.traversePreorder(root)
    #
    # print("Traverse Postorder")
    # tree.traversePostorder(root)
    # print('Printing with Tree Structure: ')
    tree.showTree(root)
    '''Remove Node Recursively '''
    tree.deleteNodeRecursively(root,72)
    '''Remove Node Non-recursively '''
    tree.remove(root,30)
    tree.showTree(root)

if __name__ == '__main__':
    main()
