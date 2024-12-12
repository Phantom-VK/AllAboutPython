import sys
import gc

### Reference Counting
# Creating an object
a = [1, 2, 3]
print(f"Initial reference count for 'a': {sys.getrefcount(a)}")  # Typically 2 due to `sys.getrefcount`

# Adding a new reference
b = a
print(f"Reference count after aliasing 'b = a': {sys.getrefcount(a)}")  # Increases by 1

# Deleting one reference
del b
print(f"Reference count after 'del b': {sys.getrefcount(a)}")  # Decreases


### Garbage Collection
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


# Creating circular references
node1 = Node("A")
node2 = Node("B")
node1.next = node2
node2.next = node1

# Breaking the circular reference
gc.collect()
print("Circular references are cleared.")

### Object Interning
a = 42
b = 42
print(f"Is 'a' the same object as 'b'? {a is b}")  # True, due to interning

x = "hello"
y = "hello"
print(f"Is 'x' the same object as 'y'? {x is y}")  # True, due to interning

# Larger numbers or dynamically created strings may not be interned
large_num = 1000
another_large_num = 1000
print(f"Is 'large_num' the same object as 'another_large_num'? {large_num is another_large_num}")  # May be False
