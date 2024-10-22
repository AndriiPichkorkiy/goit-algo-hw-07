from avl_tree import tree, empty_tree, tree_with_one_node, AVLNode

# Ітераційна функція для знаходження найбільшого значення в AVL-дереві


def find_max(root: AVLNode) -> int | None:
    if root is None:
        return None

    pointer = root
    while pointer.right is not None:
        pointer = pointer.right

    return pointer.key


print("The largest value is:", find_max(tree))
print("The largest value in empty tree:", find_max(empty_tree))
print("The largest value in a tree with one node:", find_max(tree_with_one_node))
