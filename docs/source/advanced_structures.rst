Advanced Data Structures
========================

This guide covers advanced data structures that provide sophisticated functionality and performance characteristics for complex applications.

Overview
--------

Advanced data structures build upon basic concepts to provide specialized functionality, better performance guarantees, and solutions to complex problems.

Self-Balancing Binary Search Trees
---------------------------------

Self-balancing trees automatically maintain their height to ensure efficient operations regardless of the order of insertions and deletions.

AVL Tree
~~~~~~~~

An AVL tree is a self-balancing binary search tree where the heights of the two child subtrees of any node differ by at most one.

.. automodule:: algolib.data_structures.avl_tree
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:**
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

**Space Complexity:** O(n)

**Key Features:**
- Strict height balancing
- Guaranteed O(log n) performance
- More rotations than Red-Black trees

AVL Tree Rotations
~~~~~~~~~~~~~~~~~~

AVL trees use rotations to maintain balance after insertions and deletions.

**Rotation Types:**
- **Left Rotation**: Used when the right subtree is taller
- **Right Rotation**: Used when the left subtree is taller
- **Left-Right Rotation**: Double rotation for left-right imbalance
- **Right-Left Rotation**: Double rotation for right-left imbalance

Red-Black Tree
~~~~~~~~~~~~~~

A Red-Black tree is a self-balancing binary search tree with additional properties that ensure the tree remains approximately balanced.

.. automodule:: algolib.data_structures.red_black_tree
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:**
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

**Space Complexity:** O(n)

**Properties:**
1. Every node is either red or black
2. The root is always black
3. Red nodes cannot have red children
4. Every path from root to leaves has the same number of black nodes

Red-Black Tree Fix-up Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Red-Black trees use color changes and rotations to maintain properties after insertions and deletions.

**Insertion Fix-up Cases:**
- **Case 1**: Uncle is red - recolor parent, uncle, and grandparent
- **Case 2**: Uncle is black, triangle case - rotate parent
- **Case 3**: Uncle is black, line case - rotate grandparent and recolor

**Deletion Fix-up Cases:**
- **Case 1**: Sibling is red - rotate parent and recolor
- **Case 2**: Sibling and nephews are black - recolor sibling
- **Case 3**: Sibling is black, far nephew is black - rotate sibling
- **Case 4**: Sibling is black, far nephew is red - rotate parent and recolor

Heap Data Structure
------------------

A heap is a specialized tree-based data structure that satisfies the heap property.

.. automodule:: algolib.data_structures.heap
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:**
- Insert: O(log n)
- Extract Max/Min: O(log n)
- Peek: O(1)
- Build Heap: O(n)

**Space Complexity:** O(n)

**Common Applications:**
- Priority queues
- Heap sort
- Graph algorithms (Dijkstra's, Prim's)
- Task scheduling

Disjoint Set (Union-Find)
-------------------------

A disjoint set data structure tracks a set of elements partitioned into a number of disjoint subsets.

.. automodule:: algolib.data_structures.disjoint_set
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:**
- Union: O(α(n)) amortized
- Find: O(α(n)) amortized
- Make Set: O(1)

**Space Complexity:** O(n)

**Common Applications:**
- Kruskal's minimum spanning tree algorithm
- Connected components in graphs
- Image processing
- Network connectivity

Trie (Prefix Tree)
------------------

A trie is a tree-like data structure used to store a dynamic set of strings where the keys are usually strings.

.. automodule:: algolib.data_structures.trie
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:**
- Insert: O(m) where m is key length
- Search: O(m) where m is key length
- Delete: O(m) where m is key length

**Space Complexity:** O(ALPHABET_SIZE * m * n)

**Common Applications:**
- Autocomplete systems
- Spell checkers
- IP routing tables
- Dictionary implementations

Graph Data Structure
-------------------

A graph is a collection of nodes (vertices) connected by edges, representing relationships between objects.

.. automodule:: algolib.data_structures.graph
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Representations:**
- Adjacency Matrix: O(V²) space, O(1) edge queries
- Adjacency List: O(V + E) space, O(degree) edge queries

**Common Applications:**
- Social networks
- Transportation networks
- Computer networks
- Dependency graphs

Getting Started
--------------

To use these advanced data structures:

.. code-block:: python

    from algolib.data_structures import AVLTree, RedBlackTree, Heap, DisjointSet, Trie

    # AVL Tree
    avl = AVLTree[int]()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)

    # Red-Black Tree
    rb_tree = RedBlackTree[int]()
    rb_tree.insert(15)
    rb_tree.insert(25)
    rb_tree.insert(35)

    # Heap (Max Heap)
    heap = Heap[int]()
    heap.push(10)
    heap.push(20)
    heap.push(5)
    max_value = heap.pop()  # 20

    # Disjoint Set
    ds = DisjointSet[int]()
    ds.make_set(1)
    ds.make_set(2)
    ds.union(1, 2)

    # Trie
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    contains_hello = trie.search("hello")  # True

Performance Comparison
---------------------

| Structure | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|-------|
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Red-Black Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(n) | O(log n) | O(log n) | O(n) |
| Disjoint Set | O(α(n)) | O(α(n)) | - | O(n) |
| Trie | O(m) | O(m) | O(m) | O(ALPHABET_SIZE * m * n) |

When to Use Each Structure
--------------------------

1. **AVL Tree**: When you need guaranteed O(log n) performance and can tolerate more rotations
2. **Red-Black Tree**: When you want good average performance with fewer rotations
3. **Heap**: For priority queue operations and heap sort
4. **Disjoint Set**: For tracking connected components and union-find operations
5. **Trie**: For string operations, autocomplete, and prefix matching
6. **Graph**: For representing relationships and network structures

Best Practices
-------------

1. **Choose Based on Operations**: Consider which operations you'll perform most frequently
2. **Understand Trade-offs**: Balance between time complexity, space complexity, and implementation complexity
3. **Consider Memory Usage**: Advanced structures may use more memory than simpler alternatives
4. **Profile Performance**: Test with your specific use case and data patterns

Next Steps
----------

Explore related topics:
- :doc:`../algorithms/graph/dijkstra` for graph algorithms using these structures
- :doc:`../algorithms/greedy/activity_selection` for greedy algorithms
- :doc:`../algorithms/dynamic_programming/knapsack` for dynamic programming
- :doc:`complexity_cheatsheet` for detailed performance analysis
