import numpy as np
import matplotlib.pyplot as plt

# Constants & Fuel Properties
g0 = 9.81  # m/s^2, gravity
mission_energy = 1e9  # J, example mission energy requirement

# Jet-A properties
jetA_energy_density = 43e6  # J/kg
jetA_density = 0.8  # kg/L

# Hydrogen properties (liquid)
H2_energy_density = 120e6  # J/kg
H2_density_L = 0.0708  # kg/L

# Example thrust and mass flow assumptions
thrust = 100000  # N
jetA_mass_flow = 50  # kg/s
# H2 mass flow scaled by energy content
H2_mass_flow = jetA_mass_flow * (jetA_energy_density / H2_energy_density)

# Functions for fuel calculations
def fuel_mass_and_volume(energy_required, specific_energy, density):
    mass = energy_required / specific_energy
    volume = mass / density
    return mass, volume

# Fuel calculations
jetA_mass, jetA_volume = fuel_mass_and_volume(mission_energy, jetA_energy_density, jetA_density)
H2_mass, H2_volume = fuel_mass_and_volume(mission_energy, H2_energy_density, H2_density_L)

# Specific Impulse calculation
Isp_jetA = thrust / (jetA_mass_flow * g0)
Isp_H2 = thrust / (H2_mass_flow * g0)

# Graph 1: Fuel Mass Comparison
plt.figure(figsize=(7,5))
plt.bar(['Jet-A', 'Hydrogen'], [jetA_mass, H2_mass], color=['blue','green'])
plt.ylabel('Fuel Mass (kg)')
plt.title('Fuel Mass Required for Mission')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("fuel_mass_comparison.png", dpi=300)
plt.show()

# Graph 2: Fuel Volume Comparison
plt.figure(figsize=(7,5))
plt.bar(['Jet-A', 'Hydrogen'], [jetA_volume, H2_volume], color=['orange','red'])
plt.ylabel('Fuel Volume (L)')
plt.title('Fuel Volume Required for Mission')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("fuel_volume_comparison.png", dpi=300)
plt.show()

# Graph 3: Specific Impulse Comparison
plt.figure(figsize=(7,5))
plt.bar(['Jet-A', 'Hydrogen'], [Isp_jetA, Isp_H2], color=['purple','cyan'])
plt.ylabel('Specific Impulse (s)')
plt.title('Specific Impulse Comparison')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("isp_comparison.png", dpi=300)
plt.show()

# Graph 4: Flame Temperature vs NOx Formation
temperatures = np.linspace(1500, 3500, 50)  # K
NOx_JetA = 1e-5 * (temperatures - 1500)**1.8
NOx_H2 = 1e-6 * (temperatures - 1500)**2

plt.figure(figsize=(7,5))
plt.plot(temperatures, NOx_JetA, label='Jet-A', linewidth=2)
plt.plot(temperatures, NOx_H2, label='Hydrogen', linewidth=2)
plt.xlabel('Flame Temperature (K)')
plt.ylabel('NOx Formation (kg/s equivalent)')
plt.title('Flame Temperature vs NOx Formation')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("flame_temp_nox.png", dpi=300)
plt.show()

# Graph 5: Simplified Payload-Range Diagram
payloads = np.linspace(0, 20000, 50)  # kg
range_jetA = 3500 - (payloads / 20000) * 300  # nmi
range_H2 = 3500 - (payloads / 20000) * 450   # nmi

plt.figure(figsize=(7,5))
plt.plot(payloads, range_jetA, label='Jet-A', linewidth=2)
plt.plot(payloads, range_H2, label='Hydrogen', linewidth=2)
plt.xlabel('Payload (kg)')
plt.ylabel('Range (nmi)')
plt.title('Simplified Payload-Range Diagram')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("payload_range.png", dpi=300)
plt.show()

# Results Table
print("==== RESULTS TABLE ====")
print(f"{'Fuel':<10}{'Mass (kg)':<15}{'Volume (L)':<15}{'Isp (s)':<10}")
print(f"{'Jet-A':<10}{jetA_mass:<15.1f}{jetA_volume:<15.1f}{Isp_jetA:<10.1f}")
print(f"{'Hydrogen':<10}{H2_mass:<15.1f}{H2_volume:<15.1f}{Isp_H2:<10.1f}")
