"""
You have a number of building blocks
that can be used to build a valid structure. 
There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.
Write a program that, given the number of available blocks, 
calculates the number of blocks left over 
after building the tallest possible valid structure.

Problem
- Input: integer for a specific amount of blocks
- Output: integer for left over blocks after building the tallest
  possible valid structure

- Explicit Rules:
    - Structures are built with blocks:
        - Blocks are cubes.
        - Cubes are six-sided, have square faces, and have equal
        lengths on all sides.
    - The top layer in the structure consists of a single block.
    - Upper layer blocks must be supported by four lower layer blocks.
    - Lower layer blocks can support more than one upper layer block.
    - Layers are solid structures -- there are no gaps between blocks.

Examples and test cases:
- print(calculate_leftover_blocks(0) == 0)  # True
- print(calculate_leftover_blocks(1) == 0)  # True
- print(calculate_leftover_blocks(2) == 1)  # True
- print(calculate_leftover_blocks(4) == 3)  # True
- print(calculate_leftover_blocks(5) == 0)  # True
- print(calculate_leftover_blocks(6) == 1)  # True
- print(calculate_leftover_blocks(14) == 0) # True

Data Structure
- Working with nested list.

Algorithm
1. Start with:
     - The "number of blocks remaining" is equal to the input.
     - The "current layer number" is layer 0.

2. Calculate the "current layer number" for the next layer by 
   adding 1 to the "current layer number".

3. Using the new "current layer number", calculate the "number of
   blocks required in this layer" by multiplying the "current
   layer number" by itself.

4. Determine whether the "number of blocks remaining" is greater
   than or equal to the "number of blocks required in this layer".
    - Use a `while` loop.
    - For the condition, check whether "number of blocks
      remaining" is greater than or equal to the "number of
      blocks required".
    - Calculating the blocks for the next layer, use `*` operator?
    - For example: `(current_layer * current_layer)`.
        - If there are enough blocks:
            - Subtract the "number of blocks required in this layer"
            from the "number of blocks remaining".
            - Go to step 2.
        - If there aren't enough blocks:
            - Return the "number of blocks remaining".

Code
"""
def calculate_leftover_blocks(blocks):
    number_of_block_remaining = blocks
    current_block_layer = 0
    number_of_block_needed = current_block_layer * current_block_layer

    while number_of_block_remaining >= number_of_block_needed:
        #print(current_block_layer)
        number_of_block_remaining -= number_of_block_needed
        #print(number_of_block_remaining)
        current_block_layer += 1
        number_of_block_needed = current_block_layer * current_block_layer

    return number_of_block_remaining

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

