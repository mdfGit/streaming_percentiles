from __builtin__ import str

__author__ = 'maf058'

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def get_value_at_index(root, index):
    global _index
    _index = index
    global _iteration
    _iteration = 0

    return get_ordered_index_value(root)

def get_ordered_index_value(root):
    if not root:
        return
    get_ordered_index_value(root.l_child)
    global _iteration
    _iteration += 1
    global ordered_index_value
    if _index == _iteration:
        ordered_index_value = root.data
        print ordered_index_value
        return ordered_index_value
    get_ordered_index_value(root.r_child)


def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

