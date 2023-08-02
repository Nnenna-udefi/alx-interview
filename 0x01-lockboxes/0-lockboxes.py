#!/usr/bin/python3
"""Lock boxes"""


def canUnlockAll(boxes):
    """ """
    n = len(boxes)
    if n == 0:
        return True

    # Create a list to keep track of visited boxes
    visited = [False] * n
    visited[0] = True  # The first box is unlocked

    # Use a queue to perform BFS
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        # Loop through keys in the current box
        for key in boxes[current_box]:
            # Check if the key is within the valid range of boxes
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes are visited
    return all(visited)
