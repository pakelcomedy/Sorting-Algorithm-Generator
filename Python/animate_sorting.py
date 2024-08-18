import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

def animate_sorting(steps, output_file="Preview/sorting_animation.gif", interval=50):
    """Create and save an animation of the sorting process."""
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    fig, ax = plt.subplots()
    bar_container = ax.bar(range(len(steps[0])), steps[0])
    ax.set_ylim(0, max(max(steps, key=lambda x: max(x))) * 1.1)  # Set y-limit to accommodate all bars

    def update(frame):
        for rect, val in zip(bar_container, steps[frame]):
            rect.set_height(val)
        return bar_container

    anim = animation.FuncAnimation(
        fig, update, frames=len(steps), blit=True, repeat=False, interval=interval
    )

    # Print debug information
    print(f"Saving animation to: {output_file}")
    
    try:
        anim.save(output_file, writer='pillow')
        print("Animation saved successfully.")
    except Exception as e:
        print(f"Failed to save animation: {e}")

    plt.close(fig)  # Close the figure to prevent it from displaying
