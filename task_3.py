from avl_tree import tree, empty_tree, tree_with_one_node, AVLNode

# Рекурсивна функція для знаходження суми всіх значень в AVL-дереві


def sum_tree(root: AVLNode) -> int:
    if root is None:
        return 0

    return root.key + sum_tree(root.left) + sum_tree(root.right)


print("The sum of all values is:", sum_tree(tree))
print("The sum of all values in empty tree:", sum_tree(empty_tree))
print("The sum of all values in a tree with one node:",
      sum_tree(tree_with_one_node))
