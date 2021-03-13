from binaryTrees import BinaryTree

def main():
    root = None
    tree = BinaryTree()
    root = tree.insert(root, 40)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 10)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)

    print("Traverse Preorder")
    tree.traversePreorder(root)

    print("Traverse Postorder")
    tree.traversePostorder(root)
    print('Printing with Tree Structure: ')
    tree.showTree(root)

if __name__ == '__main__':
    main()
