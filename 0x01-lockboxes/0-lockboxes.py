#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
     Returns True if all boxes can be opened,
     else return False
    """
    n = len(boxes)
    opened_boxes = set()
    opened_boxes.add(0)
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)
    return len(opened_boxes) == n
