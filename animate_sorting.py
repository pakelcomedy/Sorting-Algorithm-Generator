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

    # Simpan animasi sebagai GIF menggunakan Pillow
    anim.save(output_file, writer='pillow')
    plt.show()

if __name__ == "__main__":
    # Menggenerate teka-teki
    puzzle = generate_puzzle(length=100)  # Menghasilkan 25.000 elemen
    print("Generated puzzle:", puzzle)

    # Menyelesaikan teka-teki menggunakan Merge Sort
    steps = []
    merge_sort(puzzle, 0, len(puzzle) - 1, steps)
    print("Sorting steps recorded.")

    # Membuat animasi penyortiran
    animate_sorting(steps)
    print(f"Sorting animation created as '{output_file}'.")
