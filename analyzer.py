import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
data = pd.read_csv('data/fuel_log.csv')

# Extract columns
time = np.array(data['time'])
speed = np.array(data['speed'])
fuel_used = np.array(data['fuel_used'])
fuel_total = np.array(data['fuel_total'])

# --- Moving average smoothing function ---
def moving_average(data, window_size=51):
    return np.convolve(data, np.ones(window_size)/window_size, mode='same')

# Apply smoothing to speed
smoothed_speed = moving_average(speed, window_size=51)

# Create one figure with 2 subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12), sharex=True)

# Speed plot (smoothed)
axs[0].plot(time, smoothed_speed, color='blue', label='Speed (km/h)', linewidth=2)
axs[0].set_ylabel('Speed (km/h)')
axs[0].set_title('Vehicle Speed over Time (Smoothed)')
axs[0].legend()
axs[0].grid(True)

# Fuel Level plot (unchanged)
axs[1].plot(time, fuel_total, color='orange', label='Fuel Total (L)', linewidth=2)
axs[1].set_ylabel('Fuel (L)')
axs[1].set_title('Fuel Level over Time')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

