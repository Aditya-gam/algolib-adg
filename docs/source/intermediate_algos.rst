Intermediate Algorithms
======================

This guide covers intermediate-level algorithms that build upon basic data structures to solve common computational problems.

Overview
--------

Intermediate algorithms introduce more sophisticated problem-solving techniques including divide-and-conquer, greedy strategies, and graph traversal methods.

Sorting Algorithms
-----------------

Sorting is one of the most fundamental algorithmic problems. Different sorting algorithms offer various trade-offs between time complexity, space complexity, and stability.

Bubble Sort
~~~~~~~~~~

A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

.. automodule:: algolib.algorithms.sorting.bubble
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n²)
**Space Complexity:** O(1)
**Stable:** Yes

Insertion Sort
~~~~~~~~~~~~~

Builds the final sorted array one item at a time by repeatedly inserting a new element into the sorted portion of the array.

.. automodule:: algolib.algorithms.sorting.insertion_sort
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n²)
**Space Complexity:** O(1)
**Stable:** Yes

Selection Sort
~~~~~~~~~~~~~

Divides the input list into a sorted and unsorted region, and repeatedly selects the smallest element from the unsorted region.

.. automodule:: algolib.algorithms.sorting.selection_sort
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n²)
**Space Complexity:** O(1)
**Stable:** No

Merge Sort
~~~~~~~~~~

A divide-and-conquer algorithm that recursively breaks down a problem into smaller subproblems until they become simple enough to solve directly.

.. automodule:: algolib.algorithms.sorting.merge_sort
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)
**Stable:** Yes

Quick Sort
~~~~~~~~~~

A highly efficient, comparison-based sorting algorithm that uses a divide-and-conquer strategy with a pivot element.

.. automodule:: algolib.algorithms.sorting.quick_sort
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n log n) average, O(n²) worst case
**Space Complexity:** O(log n)
**Stable:** No

Searching Algorithms
-------------------

Searching algorithms help locate specific elements within a data structure efficiently.

Linear Search
~~~~~~~~~~~~

The simplest search algorithm that checks each element in the list sequentially until the target is found.

.. automodule:: algolib.algorithms.searching.linear
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Binary Search
~~~~~~~~~~~~

An efficient search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.

.. automodule:: algolib.algorithms.searching.binary
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Graph Algorithms
---------------

Graph algorithms solve problems involving relationships between objects represented as nodes and edges.

Breadth-First Search (BFS)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Explores all vertices at the present depth before moving on to vertices at the next depth level.

.. automodule:: algolib.algorithms.graph.traversal.breadth_first_search
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

**Common Applications:**
- Shortest path in unweighted graphs
- Web crawling
- Social network analysis
- GPS navigation systems

Depth-First Search (DFS)
~~~~~~~~~~~~~~~~~~~~~~~~

Explores as far as possible along each branch before backtracking.

.. automodule:: algolib.algorithms.graph.traversal.depth_first_search
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

**Common Applications:**
- Topological sorting
- Cycle detection
- Maze solving
- Game state exploration

Dijkstra's Algorithm
~~~~~~~~~~~~~~~~~~~~

Finds the shortest path between nodes in a weighted graph with non-negative edge weights.

.. automodule:: algolib.algorithms.graph.dijkstra
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O((V + E) log V) with binary heap
**Space Complexity:** O(V)

**Common Applications:**
- GPS navigation
- Network routing
- Social network analysis
- Game AI pathfinding

Greedy Algorithms
-----------------

Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum.

Activity Selection
~~~~~~~~~~~~~~~~~

Selects the maximum number of activities that can be performed by a single person, given start and finish times.

.. automodule:: algolib.algorithms.greedy.activity_selection
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n log n)
**Space Complexity:** O(1)

Fractional Knapsack
~~~~~~~~~~~~~~~~~~~

Solves the knapsack problem where items can be broken into smaller pieces.

.. automodule:: algolib.algorithms.greedy.fractional_knapsack
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

**Time Complexity:** O(n log n)
**Space Complexity:** O(1)

Getting Started
--------------

To use these algorithms in your code:

.. code-block:: python

    from algolib.algorithms.sorting import QuickSort
    from algolib.algorithms.searching import BinarySearch
    from algolib.algorithms.graph import Dijkstra

    # Sort a list
    sorter = QuickSort[int]()
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = sorter.sort(data)

    # Search in sorted data
    searcher = BinarySearch[int]()
    index = searcher.search(sorted_data, 25)

Algorithm Selection Guide
------------------------

1. **For Small Datasets (< 50 elements):** Use Insertion Sort or Bubble Sort
2. **For General Purpose Sorting:** Use Quick Sort or Merge Sort
3. **For Stable Sorting:** Use Merge Sort or Insertion Sort
4. **For Searching in Sorted Data:** Use Binary Search
5. **For Graph Traversal:** Use BFS for shortest path, DFS for exploration
6. **For Optimization Problems:** Consider Greedy algorithms first

Best Practices
-------------

1. **Understand Trade-offs**: Consider time vs space complexity
2. **Choose Appropriate Data Structures**: The right structure can make algorithms much more efficient
3. **Test Edge Cases**: Always test with empty arrays, single elements, and duplicate values
4. **Profile Performance**: Use benchmarking tools to measure actual performance

Next Steps
----------

Explore more advanced topics:
- :doc:`advanced_structures` for complex data structures
- :doc:`../algorithms/dynamic_programming/knapsack` for dynamic programming
- :doc:`../algorithms/backtracking/n_queens_solver` for backtracking techniques
- :doc:`complexity_cheatsheet` for detailed performance analysis
