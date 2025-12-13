# Open Science Final Project
This repository was created as part of the Open Science course final project. It demonstrates how a small, real-world research dataset can be shared in a responsible, transparent, and reproducible manner.

## Project Overview
This project is derived from my ongoing PhD research on vibration-based analysis of tree-shaking systems and was intentionally designed to apply open science principles, such as transparency, reproducibility, and responsible data sharing, to a real world research workflow. 

The dataset included in this repository contains a small, de-identified subset of vibration and acceleration measurements collected during controlled tree-shaking experiments. Each CSV file corresponds to an individual tree. Only a limited portion of the full research dataset is shared. All identifying information (e.g., GPS coordinates, precise timestamps, and experimental identifiers) has been removed to support ethical data governance and responsible reuse.

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
Each CSV file contains time-series sensor measurements with the following columns:

- `time_us`: Time in microseconds
- `ax`: Acceleration along the x-axis
- `ay`: Acceleration along the y-axis
- `az`: Acceleration along the z-axis
- `D`: Distance measurement associated with the experiment

The dataset is intended for demonstration and reproducibility purposes only.

## Reproducibility
A minimal Python script (`load_and_plot.py`) is provided to demonstrate how the data can be loaded, explored, and visualized. The script is intentionally lightweight and readable to ensure accessibility and ease of reuse by others.
This repository includes a minimal, self-contained Python script that demonstrates how to load, inspect, and visualize the shared dataset.

### Requirements

To run the example code, you need:
- Python 3.8 or later
- The following Python packages:
- `pandas`
- `matplotlib`






These packages can be installed using:

pip install pandas matplotlib

Running the Code

Clone the repository:

git clone https://github.com/<your-username>/Open-Science-Final-Project.git


Navigate to the code/ directory:

cd Open-Science-Final-Project/code


Run the example script:

python load_and_plot.py


The script automatically loads all CSV files matching tree_T*.csv from the data/ directory, prints basic summary statistics, and generates example plots of the acceleration signal.

Expected Output

Console output showing the first few rows and descriptive statistics for each dataset

Time-series plots of the vertical acceleration (az) signal for each tree

The script is intentionally lightweight and dependency-minimal to ensure accessibility and ease of reuse. Users may adapt or extend the script for additional analyses or modeling tasks.











## Broader Research Context
The full machine learning models and advanced analyses developed as part of the broader PhD research project are not included in this repository. Instead, this repository focuses on sharing a clean, well-documented sample dataset and a minimal example workflow that supports open science principles without introducing unnecessary complexity.

## Reflection
A written reflection on the design choices, ethical considerations, and lessons learned in this project is provided in [REFLECTION.md](REFLECTION.md).

## FAIR and CARE Principles
This project was designed with explicit attention to FAIR and CARE considerations. While the project follows FAIR data principles to support findability, accessibility, interoperability, and reuse, it also reflects CARE-aligned considerations by emphasizing responsible stewardship, transparency in decision-making, and awareness of potential impacts of data sharing. Together, these frameworks support both scientific reproducibility and ethical research practice.

### FAIR Principles

**Findable:**  
This repository is publicly available on GitHub with a clear directory structure, descriptive file names, and comprehensive documentation. The organized layout and README content support easy discovery and understanding of the dataset and code.

**Accessible:**  
All data and code in this repository are openly accessible without restrictions. The dataset is provided in standard CSV format, and the analysis code is written in Python using commonly available libraries, ensuring broad accessibility without the need for proprietary software.

**Interoperable:**  
The dataset is stored in non-proprietary CSV format with clearly defined column names and units. This enables straightforward use across different programming languages, platforms, and analysis environments.

**Reusable:**  
Detailed documentation and an example analysis script support reproducibility and responsible reuse. The repository structure and licensing further facilitate reuse within the documented scope.

### CARE Considerations
To ensure ethical and responsible data sharing, this repository includes only a carefully curated, de-identified subset of a larger research dataset. Potentially sensitive information (such as GPS coordinates, timestamps, and experimental identifiers) has been removed. This approach balances openness with ethical responsibility and respects the broader research context from which the data were derived. Course discussions on CARE data principles further shaped how I approached data sharing in this project. Although the dataset does not involve human subjects or Indigenous knowledge, the CARE framework encouraged me to think critically about power, potential harm, and responsibility in research. This perspective influenced my decision to remove detailed metadata, limit the scope of shared data, and clearly document appropriate use cases. Applying CARE principles beyond their original context reinforced the idea that ethical data governance is relevant to all research domains, not only those involving sensitive populations.

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

## Ethical and Legal Considerations
This project has been developed with explicit attention to ethical responsibility, data governance, and appropriate data reuse, in alignment with open science best practices.

**Licensing and Intellectual Property:**  
The repository is released under the MIT License, which clearly defines reuse permissions while protecting authorship and limiting liability.

**Scope and Nature of the Data**  
The shared dataset consists exclusively of non-human, non-personal time-series sensor measurements collected during controlled mechanical tree-shaking experiments. It does not contain human subject data, personal identifiers, or culturally sensitive knowledge. Precise timestamps, experimental identifiers, and location-specific metadata have been intentionally removed to reduce re-identification risk and prevent misuse.

**Responsible Data Governance and Access**  
The repository provides a curated, de-identified subset of a larger research dataset intended solely for demonstration, educational, and reproducibility purposes. The full experimental dataset is not publicly released due to ethical, contextual, and governance considerations. Requests for access to additional data would require appropriate justification and ethical review.

**Risk of Misuse and Mitigation**  
Although the data are not sensitive in a personal or cultural sense, inappropriate interpretation or reuse outside the documented experimental context could lead to misleading conclusions. To mitigate this risk, the dataset is accompanied by clear documentation, explicit limitations, and example analysis code. Users are encouraged to interpret results cautiously and within the stated scope.

**Ethics Beyond Minimum Compliance**  
Inspired by the CARE data principles, decisions about data sharing prioritize responsibility, transparency, and potential downstream impacts alongside openness. The goal is to balance reusability with accountability, ensuring that data sharing contributes positively to the broader research community.

## Citation
If you use this dataset or code in academic work, please cite the repository as:

Farajijalal, M. (2025). *Open Science Demonstration Dataset for Tree-Shaking Sensor Measurements*. GitHub repository.  
URL: https://github.com/<your-username>/<your-repository-name>

Please also reference the commit hash or release version used.

## References
Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018.
Global Indigenous Data Alliance. (2019). CARE Principles for Indigenous Data Governance. https://www.gida-global.org/care
United Nations. (2007). United Nations Declaration on the Rights of Indigenous Peoples (UNDRIP). https://www.un.org/development/desa/indigenouspeoples/declaration-on-the-rights-of-indigenous-peoples.html
