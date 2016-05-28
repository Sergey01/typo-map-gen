#!/usr/bin/env python
"""Given a keyboard layout map (a list/tuple containing strings of character
for each row), returns a dictionary consisting of each character and the
characters around it."""

us_qwerty = [
'1234567890-',
'qwertyuiop',
'asdfghjkl',
'zxcvbnm']

# The following search operations are as follows:
# up and to the left, straight up, up and to the right
# directly to the left, directly to the right,
# below to the left, directly below, below to the right
search_operations = (
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
    )

def generate_positional_typo_map(keyboard_layout):
    """Given a keyboard layout map (a list/tuple containing strings of character
    for each row), returns a dictionary consisting of each character and the
    characters around it."""
    positional_typo_map = {}
    for row_number, row in enumerate(keyboard_layout):
        for position, character in enumerate(row):
            buffer = [] # this is going to contain the possible typos for each character
            current_pos = [row_number, position]    # curent location on keyboard_layout
            for search_op in search_operations:
                # search_position results in [row number, character index]
                # this is calculated by adding search_op values to current_pos values
                search_position = [x + y for x, y in zip(search_op, current_pos)]
                if -1 in search_position: # we don't want to use -1 as an index
                    continue
                try:
                    typo_char = keyboard_layout[search_position[0]][search_position[1]]
                    buffer.append(typo_char)
                except IndexError:
                    continue
            positional_typo_map[character] = buffer
    return positional_typo_map

if __name__ == '__main__':
    import pprint
    typo_map = generate_positional_typo_map(us_qwerty)
    pprint.pprint(typo_map)