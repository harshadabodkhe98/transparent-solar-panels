print("TRANSPARENT SOLAR PANEL - ENERGY SIMULATION")

sunlight = float(input("Enter sunlight intensity (W/m²): "))
area = float(input("Enter panel area (m²): "))
efficiency = float(input("Enter estimated efficiency (%): "))

power = sunlight * area * (efficiency / 100)

print("\n--- Simulation Result ---")
print("Sunlight intensity:", sunlight, "W/m²")
print("Panel area:", area, "m²")
print("Estimated efficiency:", efficiency, "%")
print("Estimated electrical power:", round(power, 2), "W")
