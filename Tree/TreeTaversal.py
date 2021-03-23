from SearchGraph import SearchingWay

def main():
    root = None
    tree = SearchingWay()
    root = tree.insert(root, 60)
    tree.insert(root, 72)
    tree.insert(root, 30)
    tree.insert(root, 10)
    tree.insert(root, 55)
    tree.insert(root, 38)
    tree.insert(root, 100)
    tree.insert(root, 68)
    # print(tree.inorderTraverse(root))
    # tree.showList(root)
    tree.showTree(root)
    l = tree.BFS(root)
    print(l)
    k = tree.BFSRecursive(root)
    print(k)
if __name__ == '__main__':
    main()



'''
                    60
                /       \
            30           72
          /    \       /   \
        10      55    68    100
              /
            38
'''
