# Sorting Algorithm Visualization

This code provides a visual representation of various sorting algorithms using the Turtle graphics library. It allows you to observe how different sorting algorithms work and understand their efficiency.
 
## Supported Sorting Algorithms

1. Bubble Sort: `bubble_sort()`
2. Insertion Sort: `insertion_sort()`
3. Selection Sort: `selection_sort()`
4. Merge Sort: `merge_call()`

## Prerequisites

- Python 3.x
- Turtle (`turtle`)

## Installation

1. Make sure you have Python installed on your system. You can download it from the official website: https://www.python.org/downloads/
2. The `turtle` library is included in the Python Standard Library, so no additional installation is required.

## Usage

1. Run the script using the following command:
   ```
   python sorting_visualization.py
   ```
2. A Turtle graphics window will open with a cyan background, displaying the title "Visualizing Sorting Algorithm".
3. Instructions will be shown at the bottom of the window, indicating the key presses associated with each sorting algorithm and the option to exit.
4. Press the corresponding number key (1-4) to visualize the desired sorting algorithm.
5. The Turtle graphics will animate the sorting process, demonstrating how the algorithm works.
6. After the sorting is complete, the program will display the message "Thank You" for a brief moment and then exit.

## Customization

You can modify the code according to your preferences and requirements. Here are a few suggestions:

- Adjust the window size by changing the `sc.setup(width, height)` parameters.
- Modify the background color by modifying the `sc.bgcolor()` parameter.
- Customize the font, size, and alignment of the text using the `turtle.write()` function.
- Add more sorting algorithms or extend the existing ones by importing the necessary functions and adding key bindings using `turtle.onkey()`.

## Acknowledgments

This code was developed to facilitate understanding and visualization of sorting algorithms. It can be used for educational purposes, programming exercises, or personal exploration of sorting techniques.

Feel free to explore and learn from the code, and have fun visualizing different sorting algorithms with Turtle graphics!
