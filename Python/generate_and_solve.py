import os
import time
from generate_puzzle import generate_puzzle
from solve_puzzle import merge_sort
from animate_sorting import animate_sorting

def update_readme(merge_sort_time):
    """Update the README file with the sort duration and animation link."""
    with open("README.md", "w") as f:
        f.write(
            '<h1 align="center"></h1>\n'
            '<p align="center" style="font-weight: Bold;">Merge Sort</p>\n'
            '<p align="center">\n'
            '  <img src="Preview/merge_sort_animation.gif" alt="Merge Sort Animation" width="600"/>\n'
            '  <p align="center" style="font-weight: normal;">Sorting completed in {:.10f} seconds</p>\n'
            '</p>\n'
            '<h1 align="center"></h1>\n'
            .format(merge_sort_time)
        )

if __name__ == "__main__":
    # Print working directory for debugging
    print("Current working directory:", os.getcwd())

    # Ensure the 'Preview' directory exists
    output_dir = "Preview"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directory '{output_dir}' created.")
    else:
        print(f"Directory '{output_dir}' already exists.")

    # Generate a consistent dataset
    puzzle = generate_puzzle(length=100)  # Generate 100 elements

    # Perform Merge Sort
    steps = []
    start_time = time.perf_counter()
    merge_sort(puzzle, 0, len(puzzle) - 1, steps)
    end_time = time.perf_counter()
    merge_sort_time = end_time - start_time
    print(f"Merge Sort completed in {merge_sort_time:.10f} seconds")

    # Create sorting animation for Merge Sort
    animate_sorting(steps, output_file=os.path.join(output_dir, "merge_sort_animation.gif"))

    # Update README with sort time and animation
    update_readme(merge_sort_time)

    print("Sorting animation created as 'merge_sort_animation.gif' and README.md updated.")
