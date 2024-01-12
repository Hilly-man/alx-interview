#!/usr/bin/python3
"""BOXES BOXES"""


def canUnlockAll(boxes):
    """
    Pick up boxes
        make a set of keys
            proceed to box 0

                Obtain each key and add it.
                    setofkeys: begin opening boxes using setofkeys
                Proceed to every key box, extract the keys,
                    and add them to the collection of keys.
                Continue going over each set of keys.
            Disregard keys without a box. 
                Track the number of boxes opened using a counter.
                If the total number of boxes at the end
                equals the number of boxes,
                then all of the boxes are unlocked.
            OPTIMIZE IDEA:
            If setofkeys is increased by 0 in the beginning,
            there is no need for in 23

    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
