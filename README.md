# Open Science Final Project
This repository was created as part of the Open Science course final project.
It demonstrates how a small, real-world research dataset can be shared in a
responsible, transparent, and reproducible way.

## Project Overview
This project is directly derived from my ongoing PhD research on vibration-based analysis of tree-shaking systems and was intentionally designed to apply open science principles—such as transparency, reproducibility, and responsible data sharing—to a real-world research workflow. The dataset included in this repository contains a small, de-identified sample
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

## Reflection
A written reflection on the design choices, ethical considerations, and lessons learned in this project is provided in [REFLECTION.md](REFLECTION.md).

## FAIR and CARE Principles
This project was designed with explicit attention to FAIR (Findable, Accessible, Interoperable, Reusable) principles and, where applicable, CARE considerations.

### FAIR Principles

**Findable:**  
This repository is publicly available on GitHub with a clear directory structure, descriptive file names, and comprehensive documentation. The organized layout and README content support easy discovery and understanding of the dataset and code.

**Accessible:**  
All data and code in this repository are openly accessible without restrictions. The dataset is provided in standard CSV format, and the analysis code is written in Python using commonly available libraries, ensuring broad accessibility without the need for proprietary software.

**Interoperable:**  
The dataset is stored in non-proprietary CSV format with clearly defined column names and units. This enables straightforward use across different programming languages, platforms, and analysis environments.

**Reusable:**  
The dataset is accompanied by detailed documentation describing the experimental context, variables, and intended scope of use. An example analysis script (`load_and_plot.py`) is included to demonstrate how the data can be loaded, explored, and reused in future studies. The repository structure and documentation are designed to support reproducibility and responsible reuse.

### CARE Considerations
To ensure ethical and responsible data sharing, this repository includes only a carefully curated, de-identified subset of a larger research dataset. Potentially sensitive information (such as GPS coordinates, timestamps, and experimental identifiers) has been removed. This approach balances openness with ethical responsibility and respects the broader research context from which the data were derived.

## Technical Quality and Data Management
This repository was intentionally designed to ensure high technical quality, clarity, and practical usability.

### Repository Organization
The project follows a clear and logical directory structure that separates data, code, and documentation. Raw data files are stored in the `data/` directory, while analysis and visualization code is contained in the `code/` directory. This separation improves readability, maintainability, and reuse.

### Documentation and Clarity
Comprehensive documentation is provided through README files that explain the purpose of the project, the structure of the repository, and the contents of the dataset. Each data column is clearly described, including units and experimental meaning, enabling users unfamiliar with the original research context to understand and work with the data.

### Code Quality and Accessibility
The included Python script (`load_and_plot.py`) demonstrates a minimal but complete workflow for loading, inspecting, and visualizing the dataset. The code is intentionally kept simple, readable, and dependency-light to ensure accessibility and ease of reuse by others.

### Data Management Approach
The dataset shared in this repository represents a carefully curated, de-identified subset of a larger experimental dataset. This data management choice balances openness, reproducibility, and ethical responsibility. The use of standard CSV formats and clear documentation supports long-term usability and practical reuse while maintaining appropriate scope and data governance.

## License
This project is released under the MIT License. See the LICENSE file for details.
