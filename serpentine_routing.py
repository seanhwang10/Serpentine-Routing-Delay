import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def plot_trace_interactive():
    # Initial parameters (units in mils)
    initial_trace_length = 50  # total trace length in mils
    initial_trace_width = 10   # trace width in mils

    # Derived parameters:
    ref_length = initial_trace_length / 2.0
    offset = initial_trace_width / 2.0

    # Create a figure with three subplots side by side.
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    plt.subplots_adjust(bottom=0.3, wspace=0.3)

    # Create slider axes (shared by all subplots)
    slider_ax_length = plt.axes([0.2, 0.2, 0.6, 0.03])
    slider_ax_width  = plt.axes([0.2, 0.15, 0.6, 0.03])
    trace_length_slider = Slider(slider_ax_length, 'Trace Length (mils)', 1, 100,
                                 valinit=initial_trace_length, valstep=1)
    trace_width_slider = Slider(slider_ax_width, 'Trace Width (mils)', 1, 50,
                                valinit=initial_trace_width, valstep=1)

    # Pre-calculate theta for a quarter circle (0° to 90°)
    theta = np.linspace(0, np.pi/2, 200)

    # ---------------------------
    # Plot 1: Combined Traces (Circular Bend in blue and Right Angle Bend in red)
    # ---------------------------
    # Blue Circular Bend (using ref_length = L/2)
    x_center_blue = ref_length * np.cos(theta)
    y_center_blue = ref_length * np.sin(theta)
    blue_centerline, = ax1.plot(x_center_blue, y_center_blue, 'b:', linewidth=2)
    x_inner_blue = (ref_length - offset) * np.cos(theta)
    y_inner_blue = (ref_length - offset) * np.sin(theta)
    blue_inner, = ax1.plot(x_inner_blue, y_inner_blue, 'b-', linewidth=1)
    x_outer_blue = (ref_length + offset) * np.cos(theta)
    y_outer_blue = (ref_length + offset) * np.sin(theta)
    blue_outer, = ax1.plot(x_outer_blue, y_outer_blue, 'b-', linewidth=1)

    # Red Right Angle Bend (for Plot 1)
    x_red_horiz = np.linspace(0, ref_length, 200)
    red_horiz_center, = ax1.plot(x_red_horiz, np.full_like(x_red_horiz, ref_length),
                                  'r--', linewidth=2)
    y_red_vert = np.linspace(0, ref_length, 200)
    red_vert_center, = ax1.plot(np.full_like(y_red_vert, ref_length), y_red_vert,
                                 'r--', linewidth=2)
    x_red_horiz_outer = np.linspace(0, ref_length + offset, 200)
    red_horiz_outer, = ax1.plot(x_red_horiz_outer, np.full_like(x_red_horiz_outer, ref_length + offset),
                                'r-', linewidth=1)
    y_red_vert_outer = np.linspace(0, ref_length + offset, 200)
    red_vert_outer, = ax1.plot(np.full_like(y_red_vert_outer, ref_length + offset), y_red_vert_outer,
                               'r-', linewidth=1)
    x_red_horiz_inner = np.linspace(0, ref_length - offset, 200)
    red_horiz_inner, = ax1.plot(x_red_horiz_inner, np.full_like(x_red_horiz_inner, ref_length - offset),
                                'r-', linewidth=1)
    y_red_vert_inner = np.linspace(0, ref_length - offset, 200)
    red_vert_inner, = ax1.plot(np.full_like(y_red_vert_inner, ref_length - offset), y_red_vert_inner,
                               'r-', linewidth=1)

    margin1 = 0.2 * ref_length
    ax1.set_xlim(0, ref_length + offset + margin1)
    ax1.set_ylim(0, ref_length + offset + margin1)
    ax1.set_aspect('equal', 'box')
    grid_step = initial_trace_length / 10.0
    ax1.set_xticks(np.arange(0, ref_length + offset + margin1 + grid_step, grid_step))
    ax1.set_yticks(np.arange(0, ref_length + offset + margin1 + grid_step, grid_step))
    ax1.grid(True)
    ax1.set_xlabel("x (mils)")
    ax1.set_ylabel("y (mils)")
    ax1.set_title("Plot 1: Combined Traces")
    # Text labels on Plot 1:
    red_center_len = initial_trace_length
    red_inner_len = initial_trace_length - initial_trace_width
    red_outer_len = initial_trace_length + initial_trace_width
    ax1.text(0.05, 0.95,
             f"Right Angle Bend:\nCenter: {red_center_len:.1f} mils\nInner: {red_inner_len:.1f} mils\nOuter: {red_outer_len:.1f} mils",
             transform=ax1.transAxes, color='r', fontsize=10, verticalalignment='top')
    blue_center_len = (np.pi/2) * ref_length
    blue_inner_len  = (np.pi/2) * (ref_length - offset)
    blue_outer_len  = (np.pi/2) * (ref_length + offset)
    ax1.text(0.55, 0.95,
             f"Circular Bend:\nCenter: {blue_center_len:.1f} mils\nInner: {blue_inner_len:.1f} mils\nOuter: {blue_outer_len:.1f} mils",
             transform=ax1.transAxes, color='b', fontsize=10, verticalalignment='top')

    # ---------------------------
    # Plot 2: Red Right Angle Bend with Green Circular Trace
    # ---------------------------
    # Draw the red right angle bend (same as in Plot 1)
    x_red_horiz2 = np.linspace(0, ref_length, 200)
    red_horiz_center2, = ax2.plot(x_red_horiz2, np.full_like(x_red_horiz2, ref_length),
                                   'r--', linewidth=2)
    y_red_vert2 = np.linspace(0, ref_length, 200)
    red_vert_center2, = ax2.plot(np.full_like(y_red_vert2, ref_length), y_red_vert2,
                                  'r--', linewidth=2)
    x_red_horiz_outer2 = np.linspace(0, ref_length + offset, 200)
    red_horiz_outer2, = ax2.plot(x_red_horiz_outer2, np.full_like(x_red_horiz_outer2, ref_length + offset),
                                 'r-', linewidth=1)
    y_red_vert_outer2 = np.linspace(0, ref_length + offset, 200)
    red_vert_outer2, = ax2.plot(np.full_like(y_red_vert_outer2, ref_length + offset), y_red_vert_outer2,
                                'r-', linewidth=1)
    x_red_horiz_inner2 = np.linspace(0, ref_length - offset, 200)
    red_horiz_inner2, = ax2.plot(x_red_horiz_inner2, np.full_like(x_red_horiz_inner2, ref_length - offset),
                                 'r-', linewidth=1)
    y_red_vert_inner2 = np.linspace(0, ref_length - offset, 200)
    red_vert_inner2, = ax2.plot(np.full_like(y_red_vert_inner2, ref_length - offset), y_red_vert_inner2,
                                'r-', linewidth=1)
    # Draw the green circular trace.
    # Use R_green = (L√2)/2.
    R_green = initial_trace_length * np.sqrt(2) / 2.0
    x_center_green = R_green * np.cos(theta)
    y_center_green = R_green * np.sin(theta)
    green_centerline, = ax2.plot(x_center_green, y_center_green, 'g:', linewidth=2)
    x_inner_green = (R_green - offset) * np.cos(theta)
    y_inner_green = (R_green - offset) * np.sin(theta)
    green_inner, = ax2.plot(x_inner_green, y_inner_green, 'g-', linewidth=1)
    x_outer_green = (R_green + offset) * np.cos(theta)
    y_outer_green = (R_green + offset) * np.sin(theta)
    green_outer, = ax2.plot(x_outer_green, y_outer_green, 'g-', linewidth=1)

    margin2 = 0.2 * (initial_trace_length * np.sqrt(2) / 2.0)
    ax2.set_xlim(0, (initial_trace_length * np.sqrt(2) / 2.0) + offset + margin2)
    ax2.set_ylim(0, (initial_trace_length * np.sqrt(2) / 2.0) + offset + margin2)
    ax2.set_aspect('equal', 'box')
    ax2.set_xticks(np.arange(0, (initial_trace_length * np.sqrt(2) / 2.0) + offset + margin2 + grid_step, grid_step))
    ax2.set_yticks(np.arange(0, (initial_trace_length * np.sqrt(2) / 2.0) + offset + margin2 + grid_step, grid_step))
    ax2.grid(True)
    ax2.set_xlabel("x (mils)")
    ax2.set_ylabel("y (mils)")
    ax2.set_title("Plot 2: R = (L·√2)/2")
    # Text labels on Plot 2:
    red_center_len2 = initial_trace_length
    red_inner_len2 = initial_trace_length - initial_trace_width
    red_outer_len2 = initial_trace_length + initial_trace_width
    ax2.text(0.05, 0.90,
             f"Right Angle Bend:\nCenter: {red_center_len2:.1f} mils\nInner: {red_inner_len2:.1f} mils\nOuter: {red_outer_len2:.1f} mils",
             transform=ax2.transAxes, color='r', fontsize=10, verticalalignment='top')
    green_center_len = (np.pi/2) * R_green
    green_inner_len  = (np.pi/2) * (R_green - offset)
    green_outer_len  = (np.pi/2) * (R_green + offset)
    ax2.text(0.55, 0.90,
             f"Circular Trace:\nCenter: {green_center_len:.1f} mils\nInner: {green_inner_len:.1f} mils\nOuter: {green_outer_len:.1f} mils",
             transform=ax2.transAxes, color='g', fontsize=10, verticalalignment='top')

    # ---------------------------
    # Plot 3: Right Angle Bend with Quarter Circle Matching Inner Length (unchanged)
    # ---------------------------
    x_red_horiz3 = np.linspace(0, ref_length, 200)
    red_horiz_center3, = ax3.plot(x_red_horiz3, np.full_like(x_red_horiz3, ref_length),
                                   'r--', linewidth=2)
    y_red_vert3 = np.linspace(0, ref_length, 200)
    red_vert_center3, = ax3.plot(np.full_like(y_red_vert3, ref_length), y_red_vert3,
                                  'r--', linewidth=2)
    x_red_horiz_outer3 = np.linspace(0, ref_length + offset, 200)
    red_horiz_outer3, = ax3.plot(x_red_horiz_outer3, np.full_like(x_red_horiz_outer3, ref_length + offset),
                                  'r-', linewidth=1)
    y_red_vert_outer3 = np.linspace(0, ref_length + offset, 200)
    red_vert_outer3, = ax3.plot(np.full_like(y_red_vert_outer3, ref_length + offset), y_red_vert_outer3,
                                 'r-', linewidth=1)
    x_red_horiz_inner3 = np.linspace(0, ref_length - offset, 200)
    red_horiz_inner3, = ax3.plot(x_red_horiz_inner3, np.full_like(x_red_horiz_inner3, ref_length - offset),
                                  'r-', linewidth=1)
    y_red_vert_inner3 = np.linspace(0, ref_length - offset, 200)
    red_vert_inner3, = ax3.plot(np.full_like(y_red_vert_inner3, ref_length - offset), y_red_vert_inner3,
                                 'r-', linewidth=1)
    # Quarter circle in Plot 3: Its arc length equals the red inner length = (trace_length - trace_width).
    R_quarter = (2/np.pi) * (initial_trace_length - initial_trace_width)
    x_quarter3 = R_quarter * np.cos(theta)
    y_quarter3 = R_quarter * np.sin(theta)
    quarter_line3, = ax3.plot(x_quarter3, y_quarter3, 'g-', linewidth=2)
    quarter_text3 = ax3.text(0.05, 0.75,
                             f"Quarter Circ: {(np.pi/2)*R_quarter:.1f} mils",
                             transform=ax3.transAxes, fontsize=10, color='g')
    margin3 = 0.2 * ref_length
    ax3.set_xlim(0, ref_length + offset + margin3)
    ax3.set_ylim(0, ref_length + offset + margin3)
    ax3.set_aspect('equal', 'box')
    ax3.set_xticks(np.arange(0, ref_length + offset + margin3 + grid_step, grid_step))
    ax3.set_yticks(np.arange(0, ref_length + offset + margin3 + grid_step, grid_step))
    ax3.grid(True)
    ax3.set_xlabel("x (mils)")
    ax3.set_ylabel("y (mils)")
    ax3.set_title("Plot 3: R = (2/π)(L – W)")
    red_text_3 = f"Right Angle Bend:\nCenter: {initial_trace_length:.1f} mils\nInner: {initial_trace_length - initial_trace_width:.1f} mils\nOuter: {initial_trace_length + initial_trace_width:.1f} mils"
    ax3.text(0.05, 0.95, red_text_3, transform=ax3.transAxes, color='r', fontsize=10, verticalalignment='top')

    # ---------------------------
    # Update Function for the Sliders
    # ---------------------------
    def update(val):
        trace_length = trace_length_slider.val
        trace_width  = trace_width_slider.val
        new_ref = trace_length / 2.0
        new_offset = trace_width / 2.0

        # Update Plot 1 (Combined Traces)
        new_x_center_blue = new_ref * np.cos(theta)
        new_y_center_blue = new_ref * np.sin(theta)
        blue_centerline.set_data(new_x_center_blue, new_y_center_blue)
        new_x_inner_blue = (new_ref - new_offset) * np.cos(theta)
        new_y_inner_blue = (new_ref - new_offset) * np.sin(theta)
        blue_inner.set_data(new_x_inner_blue, new_y_inner_blue)
        new_x_outer_blue = (new_ref + new_offset) * np.cos(theta)
        new_y_outer_blue = (new_ref + new_offset) * np.sin(theta)
        blue_outer.set_data(new_x_outer_blue, new_y_outer_blue)

        new_x_red_horiz = np.linspace(0, new_ref, 200)
        red_horiz_center.set_data(new_x_red_horiz, np.full_like(new_x_red_horiz, new_ref))
        new_y_red_vert = np.linspace(0, new_ref, 200)
        red_vert_center.set_data(np.full_like(new_y_red_vert, new_ref), new_y_red_vert)
        new_x_red_horiz_outer = np.linspace(0, new_ref + new_offset, 200)
        red_horiz_outer.set_data(new_x_red_horiz_outer, np.full_like(new_x_red_horiz_outer, new_ref + new_offset))
        new_y_red_vert_outer = np.linspace(0, new_ref + new_offset, 200)
        red_vert_outer.set_data(np.full_like(new_y_red_vert_outer, new_ref + new_offset), new_y_red_vert_outer)
        new_x_red_horiz_inner = np.linspace(0, new_ref - new_offset, 200)
        red_horiz_inner.set_data(new_x_red_horiz_inner, np.full_like(new_x_red_horiz_inner, new_ref - new_offset))
        new_y_red_vert_inner = np.linspace(0, new_ref - new_offset, 200)
        red_vert_inner.set_data(np.full_like(new_y_red_vert_inner, new_ref - new_offset), new_y_red_vert_inner)

        margin_new = 0.2 * new_ref
        ax1.set_xlim(0, new_ref + new_offset + margin_new)
        ax1.set_ylim(0, new_ref + new_offset + margin_new)
        new_grid_step = trace_length / 10.0
        ax1.set_xticks(np.arange(0, new_ref + new_offset + margin_new + new_grid_step, new_grid_step))
        ax1.set_yticks(np.arange(0, new_ref + new_offset + margin_new + new_grid_step, new_grid_step))
        new_red_center = trace_length
        new_red_inner  = trace_length - trace_width
        new_red_outer  = trace_length + trace_width
        ax1.texts[0].set_text(f"Right Angle Bend:\nCenter: {new_red_center:.1f} mils\nInner: {new_red_inner:.1f} mils\nOuter: {new_red_outer:.1f} mils")
        new_blue_center = (np.pi/2) * new_ref
        new_blue_inner  = (np.pi/2) * (new_ref - new_offset)
        new_blue_outer  = (np.pi/2) * (new_ref + new_offset)
        ax1.texts[1].set_text(f"Circular Bend:\nCenter: {new_blue_center:.1f} mils\nInner: {new_blue_inner:.1f} mils\nOuter: {new_blue_outer:.1f} mils")

        # Update Plot 2 (Red Right Angle Bend + Green Circular Trace)
        # Update red right-angle bend on Plot 2 (same as in Plot 1)
        new_x_red_horiz2 = np.linspace(0, new_ref, 200)
        red_horiz_center2.set_data(new_x_red_horiz2, np.full_like(new_x_red_horiz2, new_ref))
        new_y_red_vert2 = np.linspace(0, new_ref, 200)
        red_vert_center2.set_data(np.full_like(new_y_red_vert2, new_ref), new_y_red_vert2)
        new_x_red_horiz_outer2 = np.linspace(0, new_ref + new_offset, 200)
        red_horiz_outer2.set_data(new_x_red_horiz_outer2, np.full_like(new_x_red_horiz_outer2, new_ref + new_offset))
        new_y_red_vert_outer2 = np.linspace(0, new_ref + new_offset, 200)
        red_vert_outer2.set_data(np.full_like(new_y_red_vert_outer2, new_ref + new_offset), new_y_red_vert_outer2)
        new_x_red_horiz_inner2 = np.linspace(0, new_ref - new_offset, 200)
        red_horiz_inner2.set_data(new_x_red_horiz_inner2, np.full_like(new_x_red_horiz_inner2, new_ref - new_offset))
        new_y_red_vert_inner2 = np.linspace(0, new_ref - new_offset, 200)
        red_vert_inner2.set_data(np.full_like(new_y_red_vert_inner2, new_ref - new_offset), new_y_red_vert_inner2)
        # Update green circular trace on Plot 2:
        new_R_green = trace_length * np.sqrt(2) / 2.0
        new_x_center_green = new_R_green * np.cos(theta)
        new_y_center_green = new_R_green * np.sin(theta)
        green_centerline.set_data(new_x_center_green, new_y_center_green)
        new_x_inner_green = (new_R_green - new_offset) * np.cos(theta)
        new_y_inner_green = (new_R_green - new_offset) * np.sin(theta)
        green_inner.set_data(new_x_inner_green, new_y_inner_green)
        new_x_outer_green = (new_R_green + new_offset) * np.cos(theta)
        new_y_outer_green = (new_R_green + new_offset) * np.sin(theta)
        green_outer.set_data(new_x_outer_green, new_y_outer_green)
        ax2.set_xlim(0, new_R_green + new_offset + margin_new)
        ax2.set_ylim(0, new_R_green + new_offset + margin_new)
        ax2.set_xticks(np.arange(0, new_R_green + new_offset + margin_new + new_grid_step, new_grid_step))
        ax2.set_yticks(np.arange(0, new_R_green + new_offset + margin_new + new_grid_step, new_grid_step))
        new_green_center = (np.pi/2) * new_R_green
        new_green_inner  = (np.pi/2) * (new_R_green - new_offset)
        new_green_outer  = (np.pi/2) * (new_R_green + new_offset)
        # Place green text on the right side.
        ax2.texts[1].set_text(f"Right Angle Bend:\nCenter: {trace_length:.1f} mils\nInner: {trace_length - trace_width:.1f} mils\nOuter: {trace_length + trace_width:.1f} mils")
        ax2.texts[2].set_text(f"Circular Trace:\nCenter: {new_green_center:.1f} mils\nInner: {new_green_inner:.1f} mils\nOuter: {new_green_outer:.1f} mils")

        # Update Plot 3 (Right Angle Bend with Quarter Circle Matching Inner Length)
        new_x_red_horiz3 = np.linspace(0, new_ref, 200)
        red_horiz_center3.set_data(new_x_red_horiz3, np.full_like(new_x_red_horiz3, new_ref))
        new_y_red_vert3 = np.linspace(0, new_ref, 200)
        red_vert_center3.set_data(np.full_like(new_y_red_vert3, new_ref), new_y_red_vert3)
        new_x_red_horiz_outer3 = np.linspace(0, new_ref + new_offset, 200)
        red_horiz_outer3.set_data(new_x_red_horiz_outer3, np.full_like(new_x_red_horiz_outer3, new_ref + new_offset))
        new_y_red_vert_outer3 = np.linspace(0, new_ref + new_offset, 200)
        red_vert_outer3.set_data(np.full_like(new_y_red_vert_outer3, new_ref + new_offset), new_y_red_vert_outer3)
        new_x_red_horiz_inner3 = np.linspace(0, new_ref - new_offset, 200)
        red_horiz_inner3.set_data(new_x_red_horiz_inner3, np.full_like(new_x_red_horiz_inner3, new_ref - new_offset))
        new_y_red_vert_inner3 = np.linspace(0, new_ref - new_offset, 200)
        red_vert_inner3.set_data(np.full_like(new_y_red_vert_inner3, new_ref - new_offset), new_y_red_vert_inner3)
        new_R_quarter = (2/np.pi) * (trace_length - trace_width)
        new_x_quarter3 = new_R_quarter * np.cos(theta)
        new_y_quarter3 = new_R_quarter * np.sin(theta)
        quarter_line3.set_data(new_x_quarter3, new_y_quarter3)
        new_quarter_len = (np.pi/2) * new_R_quarter
        quarter_text3.set_text(f"Quarter Circ: {new_quarter_len:.1f} mils")
        ax3.set_xlim(0, new_ref + new_offset + margin_new)
        ax3.set_ylim(0, new_ref + new_offset + margin_new)
        ax3.set_xticks(np.arange(0, new_ref + new_offset + margin_new + new_grid_step, new_grid_step))
        ax3.set_yticks(np.arange(0, new_ref + new_offset + margin_new + new_grid_step, new_grid_step))
        ax3.texts[0].set_text(f"Right Angle Bend Center: {trace_length:.1f} mils")

        for ax in (ax1, ax2, ax3):
            ax.figure.canvas.draw_idle()

    # For Plot 2, add a red text label (for the right angle bend) and a green text label (for the circular trace).
    ax2.text(0.05, 0.90,
             f"Right Angle Bend:\nCenter: {initial_trace_length:.1f} mils\nInner: {initial_trace_length - initial_trace_width:.1f} mils\nOuter: {initial_trace_length + initial_trace_width:.1f} mils",
             transform=ax2.transAxes, color='r', fontsize=10, verticalalignment='top')
    ax2.text(0.55, 0.90,
             f"Circular Trace:\nCenter: {(np.pi/2)*R_green:.1f} mils\nInner: {(np.pi/2)*(R_green - offset):.1f} mils\nOuter: {(np.pi/2)*(R_green + offset):.1f} mils",
             transform=ax2.transAxes, color='g', fontsize=10, verticalalignment='top')

    trace_length_slider.on_changed(update)
    trace_width_slider.on_changed(update)

    plt.show()

if __name__ == '__main__':
    plot_trace_interactive()
