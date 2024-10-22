from avl_tree import tree, empty_tree, tree_with_one_node, AVLNode

# Рекурсивна функція для знаходження найменшого значення в AVL-дереві


def find_min(root: AVLNode) -> int | None:
    if root is None:
        return None
    if root.left is not None:
        return find_min(root.left)
    else:
        return root.key


print("The smallest value is:", find_min(tree))
print("The smallest value in empty tree:", find_min(empty_tree))
print("The smallest value in a tree with one node:", find_min(tree_with_one_node))
