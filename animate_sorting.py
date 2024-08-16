import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_sorting(steps, output_file="sorting_animation.gif"):
    fig, ax = plt.subplots()
    bar_container = ax.bar(range(len(steps[0])), steps[0])

    def update(frame):
        for rect, val in zip(bar_container, steps[frame]):
            rect.set_height(val)
        return bar_container

    anim = animation.FuncAnimation(fig, update, frames=len(steps), blit=True, repeat=False)
    anim.save(output_file, writer="imagemagick")
    plt.show()

if __name__ == "__main__":
    from solve_puzzle.py import bubble_sort
    from generate_puzzle.py import generate_puzzle

    puzzle = generate_puzzle()
    solution_steps = bubble_sort(puzzle)

    animate_sorting(solution_steps)
