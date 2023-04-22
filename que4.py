def count_trees(forest):
    tree_count = 0
    for row in forest:
        for tree in row:
            if tree == "tree":
                tree_count += 1
    return tree_count
# Example usage
forest = [
    ["tree", "tree", "rock", "tree"],
    ["tree", "rock", "tree", "tree"],
    ["tree", "tree", "tree", "tree"],
    ["rock", "rock", "rock", "rock"]
]

num_trees = count_trees(forest)
print("Number of trees:", num_trees)