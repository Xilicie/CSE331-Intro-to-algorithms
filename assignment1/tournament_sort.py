class TreeNode:
    def __init__(self, value=None, left=None, right=None, is_leaf=False, index=None):
        self.value = value
        self.left = left
        self.right = right
        self.is_leaf = is_leaf
        self.index = index  # Index of the element in the original array (used in leaves)

def build_tournament_tree(arr):
    leaves = [TreeNode(value=val, is_leaf=True, index=i) for i, val in enumerate(arr)]

    # If the number of elements is not a power of 2, pad with infinity
    while (len(leaves) & (len(leaves) - 1)) != 0:
        leaves.append(TreeNode(value=float('inf'), is_leaf=True))

    current_level = leaves
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1]
            winner = left if left.value <= right.value else right
            parent = TreeNode(value=winner.value, left=left, right=right)
            next_level.append(parent)
        current_level = next_level
    return current_level[0], leaves  # root, leaves list

def replay_tree(node):
    if node.is_leaf:
        return node.value
    left_val = replay_tree(node.left)
    right_val = replay_tree(node.right)
    node.value = left_val if left_val <= right_val else right_val
    return node.value

def tournament_sort(arr):
    sorted_arr = []
    root, leaves = build_tournament_tree(arr)

    for _ in range(len(arr)):
        min_val = root.value
        sorted_arr.append(min_val)

        # Find the winning leaf and set it to infinity
        for leaf in leaves:
            if leaf.value == min_val:
                leaf.value = float('inf')
                break

        # Replay the tournament to find the next winner
        replay_tree(root)

    return sorted_arr
