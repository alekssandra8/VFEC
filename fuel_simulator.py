import pandas as pd
import numpy as np

duration = 5 * 60
fuel_total = 30 #liters

fuel_data = []

def calc_fuel(speed):
	return 0.0005 * speed 



for t in range(duration):
	speed = np.random.randint(0, 120)
	fuel_used = calc_fuel(speed)
	fuel_total -= fuel_used
	if fuel_total < 0:
		fuel_total = 0


	fuel_data.append([t, speed, fuel_used, fuel_total])




df = pd.DataFrame(fuel_data, columns = ['time', 'speed', 'fuel_used', 'fuel_total'])
df.to_csv('data/fuel_log.csv', index = False)












