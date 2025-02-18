import math
import tkinter as tk
from tkinter import ttk

def convert_to_inches(value, unit):
    """
    Convert a given 'value' in the specified 'unit' to inches.
      - 'inches' -> 1 : 1
      - 'meters' -> 1 inch = 0.0254 m => value_in_m / 0.0254
      - 'mils'   -> 1 mil = 0.001 inch => value_in_mils * 0.001
    """
    if unit == "inches":
        return value
    elif unit == "meters":
        return value / 0.0254
    elif unit == "mils":
        return value * 0.001
    else:
        raise ValueError(f"Unknown unit: {unit}")

def compute_propagation_times(L_inch, W_inch, Er):
    """
    Returns a multi-line string describing:
      1) Effective lengths (inches => meters).
      2) Propagation speed in the dielectric.
      3) Travel times (in ps).
      4) Time differences vs. the straight line (in ps).

    Parameters
    ----------
      L_inch : float
        The nominal centerline length in inches.
      W_inch : float
        The trace width in inches.
      Er : float
        The dielectric constant (relative permittivity).
    """

    # 1) Effective Lengths (inches)
    L_straight_in   = L_inch
    L_circular_in   = L_inch - (math.pi / 4.0) * W_inch
    L_rightangle_in = L_inch - W_inch

    # 2) Convert inches to meters
    inch_to_meter = 0.0254
    L_straight_m   = L_straight_in   * inch_to_meter
    L_circular_m   = L_circular_in   * inch_to_meter
    L_rightangle_m = L_rightangle_in * inch_to_meter

    # 3) Propagation Speed in dielectric: v = c / sqrt(Er)
    c = 2.99792458e8  # speed of light in vacuum (m/s)
    v = c / math.sqrt(Er)

    # 4) Travel Times in picoseconds
    #    time = distance / speed => convert seconds => ps (1 s = 1e12 ps)
    sec_to_ps = 1e12
    t_straight_s    = L_straight_m   / v
    t_circular_s    = L_circular_m   / v
    t_rightangle_s  = L_rightangle_m / v

    t_straight_ps    = t_straight_s   * sec_to_ps
    t_circular_ps    = t_circular_s   * sec_to_ps
    t_rightangle_ps  = t_rightangle_s * sec_to_ps

    # 5) Differences vs. straight line
    dt_circular_ps   = t_straight_ps - t_circular_ps
    dt_rightangle_ps = t_straight_ps - t_rightangle_ps

    # Prepare a formatted results string (~10 significant figures)
    result = []
    result.append("---------------------------------------------------")
    result.append(f"INPUT PARAMETERS (Converted to inches internally):")
    result.append(f"  L_inch = {L_inch:.10g} inches")
    result.append(f"  W_inch = {W_inch:.10g} inches")
    result.append(f"  Er     = {Er:.10g}")
    result.append("")
    result.append("EFFECTIVE LENGTHS (inches => meters):")
    result.append(f"  Straight:    {L_straight_in:.10g} in   => {L_straight_m:.10g} m")
    result.append(f"  Circular:    {L_circular_in:.10g} in   => {L_circular_m:.10g} m")
    result.append(f"  Right-angle: {L_rightangle_in:.10g} in => {L_rightangle_m:.10g} m")
    result.append("")
    result.append("PROPAGATION SPEED:")
    result.append("  c = 2.99792458e8 m/s")
    result.append(f"  v = c / sqrt(Er) = {v:.10g} m/s")
    result.append("")
    result.append("TRAVEL TIMES (picoseconds):")
    result.append(f"  Straight line:       {t_straight_ps:.10g} ps")
    result.append(f"  Circular-bend line:  {t_circular_ps:.10g} ps")
    result.append(f"  Right-angle bend:    {t_rightangle_ps:.10g} ps")
    result.append("")
    result.append("TIME DIFFERENCE vs. STRAIGHT (ps):")
    result.append(f"  Straight - Circular:    {dt_circular_ps:.10g} ps")
    result.append(f"  Straight - Right-angle: {dt_rightangle_ps:.10g} ps")
    result.append("---------------------------------------------------")
    return "\n".join(result)

def on_compute():
    """
    Callback for the 'Compute' button.
    Reads user inputs for L, W, Er, plus the selected units from each dropdown.
    Converts L and W to inches, then calls compute_propagation_times.
    Displays the results in text_output.
    """
    try:
        # Get user inputs from the GUI
        L_value = float(entry_L.get())
        W_value = float(entry_W.get())
        Er_value = float(entry_Er.get())

        # Get the selected units from comboboxes
        L_unit = combo_L_units.get()  # "inches", "meters", or "mils"
        W_unit = combo_W_units.get()  # "inches", "meters", or "mils"

        # Convert L and W to inches
        L_inch = convert_to_inches(L_value, L_unit)
        W_inch = convert_to_inches(W_value, W_unit)

        # Perform the calculations
        output_str = compute_propagation_times(L_inch, W_inch, Er_value)

        # Show results in the text box
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, output_str)

    except ValueError:
        # If user typed invalid input
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Error: Please enter valid numeric values.")

# -----------------------------
# Tkinter GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Propagation Time Calculator (Bend-Delay)")

# Main frame for input widgets
frame_inputs = ttk.Frame(root, padding="10")
frame_inputs.grid(row=0, column=0, sticky="w")

# 1. L input
label_L = ttk.Label(frame_inputs, text="Enter L:")
label_L.grid(row=0, column=0, padx=(0,5), pady=3, sticky="e")

entry_L = ttk.Entry(frame_inputs, width=15)
entry_L.grid(row=0, column=1, pady=3, sticky="w")
entry_L.insert(0, "10.0")  # default

combo_L_units = ttk.Combobox(frame_inputs, values=["inches", "meters", "mils"], width=8)
combo_L_units.grid(row=0, column=2, padx=(5,0), pady=3, sticky="w")
combo_L_units.current(0)  # default: "inches"

# 2. W input
label_W = ttk.Label(frame_inputs, text="Enter W:")
label_W.grid(row=1, column=0, padx=(0,5), pady=3, sticky="e")

entry_W = ttk.Entry(frame_inputs, width=15)
entry_W.grid(row=1, column=1, pady=3, sticky="w")
entry_W.insert(0, "0.005")  # default

combo_W_units = ttk.Combobox(frame_inputs, values=["inches", "meters", "mils"], width=8)
combo_W_units.grid(row=1, column=2, padx=(5,0), pady=3, sticky="w")
combo_W_units.current(0)  # default: "inches"

# 3. Er input
label_Er = ttk.Label(frame_inputs, text="Dielectric Constant (Er):")
label_Er.grid(row=2, column=0, padx=(0,5), pady=3, sticky="e")

entry_Er = ttk.Entry(frame_inputs, width=15)
entry_Er.grid(row=2, column=1, pady=3, sticky="w")
entry_Er.insert(0, "3.3")   # default

# 4. Compute button
button_compute = ttk.Button(frame_inputs, text="Compute", command=on_compute)
button_compute.grid(row=3, column=0, columnspan=3, pady=8)

# Frame for results
frame_results = ttk.Frame(root, padding="10")
frame_results.grid(row=1, column=0, sticky="nsew")

# Slightly smaller horizontally, but enough lines to avoid vertical scrolling
text_output = tk.Text(frame_results, width=60, height=25)
text_output.grid(row=0, column=0, sticky="nsew")

# Keep it a fixed size rather than resizing
frame_results.columnconfigure(0, weight=0)
frame_results.rowconfigure(0, weight=0)

root.mainloop()
