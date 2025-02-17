# 90 Degree and Circular Bend in Serpentine Routing

![](https://github.com/seanhwang10/Serpentine-Routing-Delay/blob/main/2025-02-16_23-09-12.png)

![](https://github.com/seanhwang10/Serpentine-Routing-Delay/blob/main/2025-02-16_23-09-12.png)

This interactive Python script visualizes various trace geometries using Matplotlib and NumPy. The visualization features three subplots that update in real time as you adjust two parameters: **Trace Length (mils)** and **Trace Width (mils)**.

## Overview

The script displays three subplots:

1. **Plot 1: Combined Traces**  
   
   - **Blue Circular Bend:** A quarter‐circular trace computed using a reference length of L/2 (where L is the trace length).  
   - **Red Right Angle Bend:** An L-shaped (90°) trace representing the bend.
   - **Text Labels:** Blue text shows the computed lengths for the circular bend (center, inner, and outer lengths), and red text shows the corresponding lengths for the right angle bend.

2. **Plot 2: Right Angle Bend with Circular Trace (Green)**  
   
   - **Red Right Angle Bend:** The same L-shaped red trace as in Plot 1.
Green Circular Trace: A full circular trace drawn in green. Its geometry is based on the radius

$$ R_{\text{green}} = \frac{L\sqrt{2}}{2} $$

so that its (quarter‑circumference) lengths are computed as:

- **Center:** \( \frac{\pi}{2} \, R_{\text{green}} \)
- **Inner:** \( \frac{\pi}{2}\left(R_{\text{green}} - \frac{W}{2}\right) \)
- **Outer:** \( \frac{\pi}{2}\left(R_{\text{green}} + \frac{W}{2}\right) \)
   - **Text Labels:** Two separate text labels display the computed lengths: one (in red) for the right angle bend and one (in green) for the green circular trace.

3. **Plot 3: Right Angle Bend with Quarter Circle Matching Inner Length**  
   
   - **Red Right Angle Bend:** The same L-shaped red trace.
   - **Green Quarter Circle:** A quarter circle is drawn such that its arc length equals the inner length of the red right angle bend. Its radius is computed as  
     \[
     R_{\text{quarter}} = \frac{2}{\pi}(L - W)
     \]
   - **Text Labels:** A red text label displays the right angle bend’s centerline length, and a green text label shows the quarter circle’s arc length.

All three plots update interactively when you adjust the sliders.

## How to Run

### Requirements

- Python 3.x  
- NumPy  
- Matplotlib  

### Installation

Install the required packages using:

```bash
pip install numpy matplotlib
```

### Running the Script

1. Save the Python code in a file (e.g., `serpentine_routing.py`).

2. Open a terminal or command prompt.

3. Run the script:
   
   `python serpentine_routing.py`

An interactive window will appear showing three subplots and two sliders.

## Using the Sliders

- **Trace Length (mils):** Adjusts the overall length (L) of the trace. This affects the red right angle bend and the computed circular traces.
- **Trace Width (mils):** Adjusts the width (W) of the trace, which changes the offsets for the inner and outer boundaries.

As you adjust these sliders, all three plots and their text labels update automatically to display the new computed values.

## Code Structure

- **Plot 1:**  
  Displays a blue circular bend (using a quarter circle with radius L/2) and a red right angle bend (L-shaped). Text labels show their computed lengths.

- **Plot 2:**  
  Displays the same red right angle bend along with a green circular trace drawn with radius
  
  The green circular trace has a dotted centerline and solid inner/outer boundaries. Two separate text labels (one red, one green) show the computed lengths.

- **Plot 3:**  
  Displays the red right angle bend along with a green quarter circle whose arc length matches the inner length of the red trace. Text labels display the right angle bend centerline length and the quarter circle’s arc length.

All updates are handled via the slider callback function, which recalculates the geometries and updates the text labels accordingly.
