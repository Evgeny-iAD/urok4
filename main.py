from RedBlackTree import RedBlackTree

if __name__ == '__main__':
    rb_tree = RedBlackTree()
    rb_tree.add_node(10)
    rb_tree.add_node(5)
    rb_tree.add_node(20)
    rb_tree.add_node(22)
    rb_tree.add_node(29)

    rb_tree.inorder_traversal(rb_tree.root)
