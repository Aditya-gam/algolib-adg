Easy Data Structures
===================

This guide covers the fundamental data structures that form the building blocks of computer science and programming.

Overview
--------

Easy data structures are the foundation upon which more complex algorithms and data structures are built. They provide basic operations for storing, accessing, and manipulating data efficiently.

Stack
-----

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Think of it like a stack of plates - you can only add or remove from the top.

.. automodule:: algolib.data_structures.stack
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Key Operations:**
- Push: Add an element to the top
- Pop: Remove and return the top element
- Peek: View the top element without removing it
- Is Empty: Check if the stack is empty

**Common Use Cases:**
- Function call stack in programming languages
- Undo/redo functionality
- Expression evaluation
- Depth-first search

Queue
-----

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. Think of it like a line of people waiting - the first person to join is the first to be served.

.. automodule:: algolib.data_structures.queue
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Key Operations:**
- Enqueue: Add an element to the back
- Dequeue: Remove and return the front element
- Front: View the front element without removing it
- Is Empty: Check if the queue is empty

**Common Use Cases:**
- Task scheduling
- Breadth-first search
- Print spooling
- CPU scheduling

Linked List
----------

A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.

.. automodule:: algolib.data_structures.linked_list
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Key Operations:**
- Insert: Add a new node at any position
- Delete: Remove a node from any position
- Search: Find a node with a specific value
- Traverse: Visit all nodes in the list

**Common Use Cases:**
- Dynamic memory allocation
- Implementation of other data structures
- Music playlist management
- Browser history

Binary Tree
----------

A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and right child.

.. automodule:: algolib.data_structures.binary_tree
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Key Operations:**
- Insert: Add a new node
- Delete: Remove a node
- Search: Find a node with a specific value
- Traverse: Visit all nodes (inorder, preorder, postorder)

**Common Use Cases:**
- Expression trees
- File system organization
- Decision trees
- Huffman coding

Getting Started
--------------

To use these data structures in your code:

.. code-block:: python

    from algolib.data_structures import Stack, Queue, LinkedList, BinaryTree

    # Create a stack
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Pop elements (LIFO order)
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1

Best Practices
-------------

1. **Choose the Right Structure**: Consider the operations you need most frequently
2. **Memory Management**: Be aware of memory usage, especially with linked structures
3. **Error Handling**: Always check for empty structures before operations
4. **Type Safety**: Use type hints to ensure data consistency

Next Steps
----------

Once you're comfortable with these basic structures, explore:
- :doc:`intermediate_algos` for algorithms that use these structures
- :doc:`advanced_structures` for more complex data structures
- :doc:`complexity_cheatsheet` for performance characteristics
