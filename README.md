# Extended Kalman Filter (EKF) for Ground Bot Tracking

This repository contains both C++ and Python implementations for tracking a ground bot using the Extended Kalman Filter (EKF). It fuses Lidar and Radar sensor data to estimate the bot’s position and velocity.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [C++ Version](#c-version)
  - [Python Version](#python-version)
- [File Format](#file-format)
- [Results](#results)
- [Visualizing the Results](#visualizing-the-results)
- [Code Explanation](#code-explanation)
- [Future Aspects](#future-aspects)
- [References](#references)
- [Collaboration](#collaboration)

## Introduction

- **Algorithm**: Extended Kalman Filter (EKF) for state estimation in non-linear systems.
- **Application**: Tracking moving objects like ground bots in various environments.
- **Data Fusion**: Combines noisy Lidar (distance measurements) and Radar (motion detection) data.
- **Process**: 
  - **Prediction**: Forecasts the next state based on current state and dynamics.
  - **Update**: Refines predictions with new measurements to minimize uncertainties.
- **Objective**: Evaluate EKF performance against ground truth for improved autonomous navigation and robotics.


## Features
- Fusion of Radar and Lidar sensor data.
- Non-linear state estimation using the Extended Kalman Filter.
- Comparison of estimated values against ground truth data.
  
## Folder Structure
    
    EKF_Tracking_Of_Ground_Bot/
    ├── EKF_Cpp/                  # C++ implementation
    │   ├── build/                # You need to build this directory for compilation of all C++ files
    │   └── data/                 # Contains the input files
    │   └── src/                  # All C++ code and header files
    
    ├── EKF_Python/               # Python implementation
    │   ├── Script/               # Python code
    │   └── data/                 # Input files for the Python version
    │   └── Output/               # Output folder for results

## Prerequisites

### Python Implementation:
- **Python version**: Python 3.6 or higher is required.
- **Necessary libraries**: You will need the following Python libraries for the EKF implementation:
  - `numpy` for matrix operations and numerical computations.
  - `matplotlib` for plotting results (optional, if you want to visualize the tracking performance).
  - `pandas` (optional, for handling data input/output in a structured way).

- To install these packages, run the following commands:

    ```bash
    pip install numpy
    pip install matplotlib     # Optional, for visualizing tracking results
    pip install pandas         # Optional, for data handling


### C++ Implementation:
- **C++ version**: C++11 or higher.
- **Build system**: You need `cmake` to configure the project.
- **Compiler**: Use `g++` or `clang++` for compilation.

- To ensure your system meets these requirements, you can install `cmake` and the compiler using the following commands (for **Ubuntu/Debian-based systems**):

    ```bash
    sudo apt-get update
    sudo apt-get install cmake g++
- For other operating systems, use the equivalent package manager (e.g., **brew for macOS**, **choco for Windows**).

## Usage

### C++ Version
1. Navigate to `EKF_Cpp/`.
2. Build the project:
   ```bash
   mkdir build
   cd build
   cmake ..
   make                # This command will compile all the C++ files
   ./EKF_Tracking ../data/input.txt ./output.txt

- This command `make` triggers the build system to compile all the C++ source files located in the src/ directory. It will generate an executable file that runs the Extended Kalman Filter (EKF) for ground bot tracking. The make process ensures that all necessary object files are created, linked, and optimized according to the CMake configuration. After compiling, the resulting executable can be run with the input data to perform state estimation using fused Lidar and Radar measurements.

### Python Version
1.⁠ ⁠Navigate to ⁠ `EKF_Python/Script/`⁠

2.⁠ ⁠Run the Python script:
    
    python3 main.py
•⁠  ⁠Ensure that the Input.txt is present in EKF_Python/data/

## File Format:
### The Input file format is:
     L(for laser) meas_px meas_py timestamp gt_px gt_py gt_vx gt_vy
     R(for radar) meas_rho meas_phi meas_rho_dot timestamp gt_px gt_py gt_vx gt_vy

     Example:
        R	8.60363	0.0290616	-2.99903	1477010443399637	8.6	0.25	-3.00029	0
        L	8.45	0.25	1477010443349642	8.45	0.25	-3.00027	0
### The Output file format is:
    est_px est_py est_vx est_vy meas_px meas_py gt_px gt_py gt_vx gt_vy

    Example:
        4.53271	0.279	-0.842172	53.1339	4.29136	0.215312	2.28434	0.226323
        43.2222	2.65959	0.931181	23.2469	4.29136	0.215312	2.28434	0.226323
- Here
    - est_px, est_py: Estimated x and y positions.
    - est_vx, est_vy: Estimated velocities in x and y directions.
    - meas_px, meas_py: Measured x and y positions (from sensors like Lidar or Radar).
    - gt_px, gt_py: Ground truth x and y positions.
    - gt_vx, gt_vy: Ground truth velocities in x and y directions.

## Results
The output of the EKF will be saved in ⁠ Output/output.txt for python and build/output.txt for C++ ⁠. The results will include the estimated position and velocity alongside the ground truth for evaluation.

### Output Comparison: Estimated vs Ground Truth Positions

![position](EKF_Python/data/comparison.png)

The included graph illustrates the performance of the Extended Kalman Filter (EKF) by comparing the estimated positions to the ground truth values, while measured positions from Lidar or Radar sensors are omitted for clarity.

**Estimated Positions:** Calculated by the EKF using sensor inputs and prediction models.
**Ground Truth Positions:** Actual positions of the object, serving as a reference for EKF accuracy.
**Measured Positions:** Raw sensor readings inputted into the EKF.

The graph shows that the estimated trajectory closely follows the ground truth, demonstrating the EKF's effectiveness in filtering noise and providing accurate state estimations. Minor deviations between estimated and ground truth values highlight areas for potential refinement of the EKF implementation.
## Visualizing the Results

We use `matplotlib` to visualize the EKF's performance by plotting estimated positions, velocities, and errors against ground truth and sensor measurements. Follow the steps below to generate these plots.

### Position Visualization

The plots illustrate **X** and **Y** positions and velocities over time, featuring:

![position](EKF_Python/data/Position.png)

The plot shows **Noisy Sensor Data (green dotted line)** from Lidar and Radar, reflecting fluctuations due to sensor noise, alongside the **Ground Truth (orange dashed line)** as the actual positions and velocities. The **Estimated Position (blue solid line)** represents the EKF-computed values that closely follow the ground truth while filtering out noise.

### Velocity Visualization

![Velocity](EKF_Python/data/Velocity.png)

This plot includes the **Estimated Velocity (blue solid line)**, closely following the **Ground Truth Velocity (orange dashed line)**, and the **Measured Velocity (green dotted line)**, which shows the noisy sensor measurements.

### Error Visualization

![Error](EKF_Python/data/Error.png)
- Error plots illustrate discrepancies between estimated and ground truth values (position)

## Code Explanation
### KalmanFilter Class:
Implements the core EKF logic: prediction, standard and extended update (for non-linear radar data).
#### Key Methods:
- **predict():** Advances state based on transition model.
- **update():** Updates state with Lidar data.
- **update_ekf():** Updates state with non-linear Radar data.
### Tools Class:
Contains utilities for computing Jacobians and RMSE.
### FusionEKF Class:
Manages sensor fusion: initialization, prediction, and processing of sensor measurements (Lidar/Radar). It initializes based on the first measurement, updates the state transition matrix with time dt, and applies the appropriate update method depending on sensor type.

## Future Aspects
- **GPS Integration:** Enhance geolocation and navigation through GPS fusion with Lidar and Radar.
- **Machine Learning:** Use algorithms to adaptively refine EKF parameters based on environmental conditions.
- **Additional Sensors:** Incorporate cameras for visual tracking and IMUs for improved motion estimation.
- **Comprehensive System:** Develop a multi-sensor fusion system for advanced autonomous navigation and tracking applications.

## References
-  ⁠[Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter)
-  ⁠[Radar vs Lidar](https://spectrum.ieee.org/radar-vs-lidar)

## Collaboration:
Contributions to enhance the EKF implementation are welcome! Feel free to collaborate by reaching out!