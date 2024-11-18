# Alyssa was asked to write an implementation of a rolling buffer. 
# You can add and remove elements from a rolling buffer. 
# However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.
# She wrote two implementations of the code for adding elements to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# Is there a difference between these implementations, other than the way she is adding an element to the buffer?

# Yes, there is a difference. In the first code, 
# buffer.append(new_element) invokes the append() method which mutates the elements pointed to by the variable called buffer.

# In the second code, 
# buffer = buffer + [new_element] reassign buffer to a new variable called buffer that is local to function.
# This does not mutate original object the buffer variable points to. 
# Instead, this buffer points to a new object in memory that is returned.