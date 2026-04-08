The code is intended to support the research paper:  
*"Comparative Analysis of Cryogenic Hydrogen Storage and Combustion Stability in Mid-Range Commercial Aircraft"* by Abhijith Nair, Marquette High School.

## How to Run

1. Install Python 3.x if not already installed.
2. Install required packages:
3. Run the Python script: python hydrogen_vs_jetA.py

This will generate:
- Fuel mass and volume comparison graphs
- Specific impulse comparison graph
- Flame temperature vs NOx formation graph
- Simplified payload-range diagram
- A table of results printed in the console

If using this code, please reference the repository in your paper.
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("payload_range.png", dpi=300)
plt.show()

# =====================
# Results Table
# =====================
print("==== RESULTS TABLE ====")
print(f"{'Fuel':<10}{'Mass (kg)':<15}{'Volume (L)':<15}{'Isp (s)':<10}")
print(f"{'Jet-A':<10}{jetA_mass:<15.1f}{jetA_volume:<15.1f}{Isp_jetA:<10.1f}")
print(f"{'Hydrogen':<10}{H2_mass:<15.1f}{H2_volume:<15.1f}{Isp_H2:<10.1f}")

```bash
pip install numpy matplotlib
