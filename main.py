from red_black_trees import RedBlackTree as RBTree

if __name__ == '__main__':

    red_black_trees = RBTree()

    red_black_trees.insert(1)
    red_black_trees.insert(2)
    red_black_trees.insert(3)
    red_black_trees.insert(4)
    red_black_trees.insert(5)
    red_black_trees.insert(6)
    red_black_trees.insert(7)
    red_black_trees.insert(8)
    red_black_trees.insert(9)
    red_black_trees.insert(10)

    red_black_trees.print_tree()

    red_black_trees.delete_node(4)

    red_black_trees.print_tree()



