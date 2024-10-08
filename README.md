# Extended Kalman Filter (EKF) for Ground Bot Tracking

This repository contains both C++ and Python implementations for tracking a ground bot using the Extended Kalman Filter (EKF). It fuses Lidar and Radar sensor data to estimate the bot’s position and velocity.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [C++ Version](#cpp-version)
  - [Python Version](#python-version)
- [Results](#results)
- [References](#references)

## Introduction
The Extended Kalman Filter (EKF) is used for state estimation in non-linear systems. In this project, the EKF processes noisy sensor data from Lidar and Radar to track the position and velocity of a ground bot, comparing the results with the ground truth.

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