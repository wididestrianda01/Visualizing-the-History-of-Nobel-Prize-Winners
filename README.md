# Visualizing the History of Nobel Prize Winners

A comprehensive data analysis and visualization project exploring the Nobel Prize dataset from 1901 to present. This project analyzes patterns, trends, and insights from over a century of Nobel Prize awards across all categories.

## Project Overview

This project examines the Nobel Prize dataset to uncover interesting patterns and trends in the awards given across different categories (Physics, Chemistry, Medicine, Literature, Peace, and Economics). The analysis includes visualizations of gender distribution, geographical patterns, age demographics, and temporal trends.

## Dataset

The project uses the Nobel Prize dataset (`data/raw/nobel.csv`) which contains comprehensive information about:
- **1,000+ Nobel Prize records** from 1901 onwards
- **Award categories**: Physics, Chemistry, Medicine, Literature, Peace, and Economics
- **Laureate information**: Names, birth/death dates, countries, organizations
- **Award details**: Years, motivations, prize shares

## Key Analysis Areas

- **Temporal Trends**: How Nobel Prize patterns have changed over time
- **Gender Analysis**: Distribution of awards by gender across categories and decades
- **Geographic Distribution**: Which countries have produced the most laureates
- **Age Demographics**: Age patterns of laureates at the time of award
- **Category Insights**: Differences between scientific and non-scientific categories
- **Organizational Affiliations**: Most represented institutions and universities

## Project Structure

```
Visualizing the History of Nobel Prize Winners/
├── data/              # Data storage and documentation
│   ├── raw/           # Original Nobel Prize dataset
│   ├── processed/     # Cleaned and transformed data
│   └── cleaned/       # Final analysis-ready datasets
├── notebooks/         # Jupyter notebooks for analysis
│   └── project answer.ipynb  # Main analysis notebook
├── src/               # Core source code modules
├── scripts/           # Standalone analysis scripts
├── tests/             # Test suite
├── config/            # Configuration files
├── reports/           # Generated analysis reports
├── docs/              # Project documentation
├── logs/              # Analysis logs
├── environment.yml    # Conda environment specification
├── requirements.txt   # Python dependencies
├── README.md          # This file
└── setup.py           # Package configuration
```

## Getting Started

### Prerequisites
- Python 3.7+
- Conda or pip for package management

### Installation

1. **Clone the repository** (if applicable)
   ```bash
   git clone <repository-url>
   cd "Visualizing the History of Nobel Prize Winners"
   ```

2. **Create and activate environment**
   ```bash
   # Using conda (recommended)
   conda env create -f environment.yml
   conda activate nobel-analysis

   # Or using pip
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

4. **Open the main analysis notebook**
   - Navigate to `notebooks/project answer.ipynb`
   - Run all cells to reproduce the analysis

## Key Findings

The analysis reveals several fascinating insights about Nobel Prize trends:

- **Gender representation** has improved significantly over time, though disparities remain
- **Geographic concentration** shows certain countries dominating in specific categories
- **Age patterns** vary significantly between different prize categories
- **Institutional affiliations** highlight the role of major research universities
- **Temporal trends** show how global events have influenced prize patterns

## Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Data visualization
- **Jupyter Notebooks**: Interactive analysis environment
- **NumPy**: Numerical computations

## Contributing

This project was developed as part of a DataCamp analysis project. Feel free to:
- Explore the data with your own questions
- Suggest additional visualizations
- Improve the analysis methodology
- Add new insights or findings

## Data Source

The Nobel Prize dataset is publicly available and contains official information about all Nobel Prize awards. The data includes both individual laureates and organizations that have received Nobel Prizes.

## License

This project is for educational and research purposes. The Nobel Prize data is publicly available, and visualizations are created for analytical insights.
