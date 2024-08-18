import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from generate_puzzle import generate_puzzle
from solve_puzzle import merge_sort

def animate_sorting(steps, output_file="sorting_animation.gif", interval=50):
    fig, ax = plt.subplots()
    bar_container = ax.bar(range(len(steps[0])), steps[0])

    def update(frame):
        for rect, val in zip(bar_container, steps[frame]):
            rect.set_height(val)
        return bar_container

    anim = animation.FuncAnimation(
        fig, update, frames=len(steps), blit=True, repeat=False, interval=interval
    )

    anim.save(output_file, writer='pillow')
    plt.show()

if __name__ == "__main__":
    # Generate puzzle
    puzzle = generate_puzzle(length=100)  # Generate 100 elements
    print("Generated puzzle:", puzzle)

    # Measure sorting time using time.perf_counter for high precision
    steps = []
    start_time = time.perf_counter()
    merge_sort(puzzle, 0, len(puzzle) - 1, steps)
    end_time = time.perf_counter()

    sorting_time = end_time - start_time
    duration_str = f"Sorting completed in {sorting_time:.10f} seconds"
    print(duration_str)

    # Update the README.md with the sorting duration
    with open("README.md", "r") as f:
        lines = f.readlines()

    with open("README.md", "w") as f:
        for line in lines:
            if "Sorting completed in" in line:
                continue  # Remove the old line with duration
            f.write(line)
        f.write(f"\n## Sorting Speed\n\n{duration_str}\n")

    # Create sorting animation
    animate_sorting(steps)
    print("Sorting animation created as 'sorting_animation.gif'.")
