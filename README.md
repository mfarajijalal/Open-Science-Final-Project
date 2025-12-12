# Open Science Final Project

This repository was created as part of the Open Science course final project.
It demonstrates how a small, real-world research dataset can be shared in a
responsible, transparent, and reproducible way.

## Project Overview

The dataset included in this repository contains a small, de-identified sample
of vibration and acceleration measurements collected from tree-shaking
experiments. Each CSV file corresponds to one individual tree.

Only a limited subset of the full research data is shared here. All identifying
information (e.g., GPS coordinates, timestamps, and experimental IDs) has been
removed to protect privacy and comply with responsible data-sharing practices.

## Repository Structure
```
Open-Science-Final-Project/
├── data/
│ ├── README.md
│ ├── tree_T01.csv
│ ├── tree_T02.csv
│ └── tree_T03.csv
├── code/
│ ├── README.md
│ └── load_and_plot.py
└── README.md
```
## Data Description

Each CSV file contains time-series sensor data with the following columns:

- `time_us`: Time in microseconds
- `ax`: Acceleration along the x-axis
- `ay`: Acceleration along the y-axis
- `az`: Acceleration along the z-axis
- `D`: Distance measurement associated with the experiment

The dataset is intended for demonstration and reproducibility purposes only.

## Reproducibility

A minimal Python script (`load_and_plot.py`) is provided to demonstrate how the
data can be loaded, explored, and visualized. The script is intentionally kept
simple to ensure that it can be easily understood and reused by others.

## Notes on Broader Research Context

The full machine learning models and analyses developed as part of the broader
PhD research project are not included in this repository. This repository
focuses on sharing a clean, well-documented sample dataset and a minimal example
workflow to support open science principles.
