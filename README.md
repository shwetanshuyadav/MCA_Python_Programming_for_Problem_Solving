# MCA Python Programming for Problem Solving

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive collection of Python programming experiments and examples designed for MCA (Master of Computer Applications) students. This repository covers fundamental to advanced Python concepts through practical problem-solving exercises.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Experiments Overview](#experiments-overview)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## ✨ Features

- **19 Comprehensive Experiments**: From basic syntax to advanced OOP concepts
- **Modular Package Structure**: Custom shapes package demonstrating package organization
- **File Handling Examples**: CSV and text file processing
- **Exception Handling**: Robust error management techniques
- **Jupyter Notebooks**: Interactive learning environment
- **Educational Focus**: Designed for MCA curriculum

## 📋 Prerequisites

- **Python 3.7+**: Ensure Python is installed on your system
- **Jupyter Notebook**: For running interactive experiments
- **Git**: For cloning and version control

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/MCA_Python_Programming_for_Problem_Solving.git
   cd MCA_Python_Programming_for_Problem_Solving
   ```

2. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

## 📁 Project Structure

```
MCA_Python_Programming_for_Problem_Solving/
├── experiments/              # Jupyter notebooks (exp_1.ipynb to exp_19.ipynb)
│   ├── exp_1.ipynb          # Basic Python programs
│   ├── exp_2.ipynb          # Control structures
│   └── ...                  # Additional experiments
├── packages/
│   └── shapes/              # Custom shapes package
│       ├── __init__.py
│       ├── circle.py        # Circle class implementation
│       ├── rectangle.py     # Rectangle class implementation
│       └── point.py         # Point class for coordinates
├── data/                    # Sample data files
│   ├── employees.csv        # Employee data for file handling
│   └── sample.txt           # Text file examples
├── main.py                  # Main script demonstrating key concepts
├── plan.md                  # Project planning documentation
└── README.md                # Project documentation
```

## 🧪 Experiments Overview

| Experiment | Topic | Description |
|------------|-------|-------------|
| exp_1 | Python Basics | Leap year checker, basic syntax |
| exp_2-5 | Control Structures | Loops, conditionals, basic algorithms |
| exp_6-9 | Functions | Function definitions, parameters, return values |
| exp_10 | Modules | Using math module for calculations |
| exp_11-14 | File Handling | Reading/writing files, CSV processing |
| exp_15 | Exceptions | Error handling and exception management |
| exp_16-19 | Advanced Topics | OOP concepts, packages, modules |

## 💻 Usage

### Running Experiments
1. Open Jupyter Notebook in your browser
2. Navigate to the `experiments/` directory
3. Open any `exp_*.ipynb` file
4. Run cells sequentially to see outputs

### Running Main Script
```bash
python main.py
```

### Using Custom Packages
```python
from packages.shapes.circle import Circle
from packages.shapes.point import Point

# Create a circle
center = Point(0, 0)
circle = Circle(center, 5)
print(f"Area: {circle.area()}")
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Keerti**


---

⭐ If you find this repository helpful, please give it a star!
