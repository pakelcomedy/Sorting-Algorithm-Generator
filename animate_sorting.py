import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
