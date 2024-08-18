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
            '<p align="center" style="font-weight: bold;">Merge Sort</p>\n'
            '<p align="center">\n'
            '  <img src="Preview/merge_sort_animation.gif" alt="Merge Sort Animation" width="600"/>\n'
            '  <p align="center" style="font-weight: normal;">Sorting completed in {:.10f} seconds</p>\n'
            '</p>\n'
            '<h1 align="center"></h1>\n'
            .format(merge_sort_time)
        )

if __name__ == "__main__":
    # Print the current working directory
    print("Current working directory:", os.getcwd())

    # Ensure the 'Preview' directory exists
    output_dir = "Preview"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Directory '{output_dir}' is ready.")

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
    animation_path = os.path.join(output_dir, "merge_sort_animation.gif")
    print(f"Saving animation to {animation_path}")
    animate_sorting(steps, output_file=animation_path)

    # Update README with sort time and animation
    update_readme(merge_sort_time)

    print(f"Sorting animation created as '{animation_path}' and README.md updated.")
