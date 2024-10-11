import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the provided files
output_columns = ['est_px', 'est_py', 'est_vx', 'est_vy', 'meas_px', 'meas_py', 'gt_px', 'gt_py', 'gt_vx', 'gt_vy']
input_columns = ['sensor_type', 'meas_px', 'meas_py', 'timestamp', 'gt_px', 'gt_py', 'gt_vx', 'gt_vy']

# Load the output.txt and input.txt
output_df = pd.read_csv('EKF_Python/Output/output.txt', delim_whitespace=True, names=output_columns)
input_df = pd.read_csv('EKF_Python/data/Input.txt', delim_whitespace=True, names=input_columns)

# Plot est_px vs est_py, gt_px vs gt_py, and meas_px vs meas_py
plt.figure(figsize=(10, 7))

# Plot for estimated positions
plt.plot(output_df['est_px'], output_df['est_py'], label='Estimated Position', marker='o', linestyle='-', color='blue')

# Plot for ground truth positions
plt.plot(output_df['gt_px'], output_df['gt_py'], label='Ground Truth Position', marker='x', linestyle='-', color='green')

# Plot for measured positions (Lidar or Radar)
#plt.scatter(output_df['meas_px'], output_df['meas_py'], label='Measured Position', marker='s', color='red')

# Labels and title
plt.xlabel('Position X', fontweight='bold', color='red')
plt.ylabel('Position Y', fontweight='bold', color='red')
plt.title('Comparison of Estimated and Ground Truth Positions', fontweight='bold')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
