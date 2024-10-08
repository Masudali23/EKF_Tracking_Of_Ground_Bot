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
- [Results](#results)
- [Future Aspects](#future-aspects)
- [References](#references)

## Introduction

The Extended Kalman Filter (EKF) is a powerful algorithm used for state estimation in systems characterized by non-linear dynamics. In the context of robotics, it is particularly useful for tracking moving objects, such as a ground bot navigating through an environment. The EKF operates by fusing noisy measurements from various sensors—specifically Lidar and Radar to produce a more accurate estimate of the bot's position and velocity.

Lidar provides high-resolution distance measurements that are essential for accurate spatial awareness, while Radar excels in detecting the relative motion of nearby objects. Given the inherent noise in these sensor readings, the EKF employs a two-step process: prediction and update. During the prediction step, the EKF uses the current state of the bot and the dynamics of the environment to forecast its next state. In the update step, it refines this prediction based on the new sensor measurements, adjusting the state estimates to account for uncertainties.

This project aims to demonstrate the efficacy of the EKF in processing sensor data in real-time. By comparing the EKF's output with ground truth values, we can evaluate its performance in accurately estimating the ground bot's state, even in the presence of sensor noise and other environmental challenges. The insights gained from this implementation can be valuable for applications in autonomous navigation, robotics, and sensor fusion.

## Features
- Fusion of Radar and Lidar sensor data.
- Non-linear state estimation using the Extended Kalman Filter.
- Comparison of estimated values against ground truth data.
  
  ## Folder Structure
  ```bash
  EKF_Tracking_Of_Ground_Bot/
  ├── EKF_Cpp/                  # C++ implementation
  │   ├── build/                # You need to build this directory for compilation of all C++ files
  │   └── data/                 # Contains the input files
  │   └── Docs/                 # Contains information about the input and output files
  │   └── src/                  # All C++ code and header files
  
  ├── EKF_Python/               # Python implementation
  │   ├── Script/               # Python code
  │   └── data/                 # Input files for the Python version
  │   └── Output/               # Output folder for results

## Prerequisites

### Python Implementation:
•⁠  ⁠Python 3.6+

•⁠  ⁠Install necessary packages using:
 
    pip install -r requirements.txt


### C++ Implementation:
- C++11 or higher
- cmake
- g++ or clang++

## Usage

### C++ Version
1. Navigate to `EKF_Cpp/`.
2. Build the project:
   ```bash
   mkdir build
   cd build
   cmake ..
   make
   ./EKF_Tracking ../data/input.txt ./output.txt

 ### Python Version
1.⁠ ⁠Navigate to ⁠ `EKF_Python/Script/` ⁠.
2.⁠ ⁠Run the Python script:
    
    python3 main.py
•⁠  ⁠Ensure that the Input.txt is present in EKF_Python/data/


## Results
The output of the EKF will be saved in ⁠ Output/output.txt ⁠. The results will include the estimated position and velocity alongside the ground truth for evaluation.

## Future Aspects
- **GPS Integration:** Enhance geolocation and navigation through GPS fusion with Lidar and Radar.
- **Machine Learning:** Use algorithms to adaptively refine EKF parameters based on environmental conditions.
- **Additional Sensors:** Incorporate cameras for visual tracking and IMUs for improved motion estimation.
- **Comprehensive System:** Develop a multi-sensor fusion system for advanced autonomous navigation and tracking applications.

## References
•⁠  ⁠[Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter)
•⁠  ⁠[Radar vs Lidar](https://spectrum.ieee.org/radar-vs-lidar)
