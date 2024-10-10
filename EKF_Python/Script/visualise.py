import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the output.txt file
# Adjust the path if necessary
data = pd.read_csv('EKF_Python/Output/output.txt', delim_whitespace=True, header=None)

# Assign columns based on your format
data.columns = ['est_px', 'est_py', 'est_vx', 'est_vy', 'meas_px', 'meas_py', 'gt_px', 'gt_py', 'gt_vx', 'gt_vy']

# Extract relevant data
time_steps = data.index  # Using row index as time steps (or use your own time vector if available)
est_px = data['est_px']
est_py = data['est_py']
est_vx = data['est_vx']
est_vy = data['est_vy']
meas_px = data['meas_px']
meas_py = data['meas_py']
gt_px = data['gt_px']
gt_py = data['gt_py']
gt_vx = data['gt_vx']
gt_vy = data['gt_vy']

# Plotting estimated vs ground truth positions (X and Y)
plt.figure(figsize=(12, 6))

# X Position Plot
plt.subplot(2, 1, 1)
plt.plot(time_steps, est_px, label='Estimated X Position')
plt.plot(time_steps, gt_px, label='Ground Truth X Position', linestyle='dashed')
plt.plot(time_steps, meas_px, label='Measured X Position', linestyle='dotted')
plt.title('X Position Over Time')
plt.xlabel('Time Steps')
plt.ylabel('X Position')
plt.legend()

# Y Position Plot
plt.subplot(2, 1, 2)
plt.plot(time_steps, est_py, label='Estimated Y Position')
plt.plot(time_steps, gt_py, label='Ground Truth Y Position', linestyle='dashed')
plt.plot(time_steps, meas_py, label='Measured Y Position', linestyle='dotted')
plt.title('Y Position Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Y Position')
plt.legend()

plt.tight_layout()
plt.show()

# Plotting estimated vs ground truth velocities (VX and VY)
plt.figure(figsize=(12, 6))

# VX Velocity Plot
plt.subplot(2, 1, 1)
plt.plot(time_steps, est_vx, label='Estimated VX')
plt.plot(time_steps, gt_vx, label='Ground Truth VX', linestyle='dashed')
plt.title('VX Velocity Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Velocity (VX)')
plt.legend()

# VY Velocity Plot
plt.subplot(2, 1, 2)
plt.plot(time_steps, est_vy, label='Estimated VY')
plt.plot(time_steps, gt_vy, label='Ground Truth VY', linestyle='dashed')
plt.title('VY Velocity Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Velocity (VY)')
plt.legend()

plt.tight_layout()
plt.show()

# (Optional) Plotting errors for further analysis
error_px = np.abs(est_px - gt_px)
error_py = np.abs(est_py - gt_py)

plt.figure(figsize=(12, 6))

plt.plot(time_steps, error_px, label='Position Error X')
plt.plot(time_steps, error_py, label='Position Error Y')
plt.title('Position Error Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Error (Position)')
plt.legend()

plt.tight_layout()
plt.show()
