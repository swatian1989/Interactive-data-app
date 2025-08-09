# Enhanced Data Analysis Platform

## Overview

This is a comprehensive Streamlit-based data analysis platform that provides end-to-end data analytics capabilities including data upload, exploration, visualization, statistical testing, machine learning, and automated reporting. The application features a multi-page architecture with specialized modules for different analytical workflows, from basic data profiling to advanced machine learning and statistical hypothesis testing.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit multi-page application with wide layout configuration
- **Navigation**: Page-based structure with 8 specialized modules accessible via sidebar navigation
- **Session Management**: Streamlit session state for persistent data storage across page transitions
- **UI Components**: Metrics dashboards, interactive forms, configuration panels, and responsive column layouts

### Application Structure
- **Main Entry Point**: `app.py` serves as the landing page with overview metrics and navigation guidance
- **Modular Page Architecture**: Eight specialized pages for different analytical functions:
  - Data Upload (`01_📁_Data_Upload.py`) - File handling and dataset management
  - Data Exploration (`02_🔍_Data_Exploration.py`) - Interactive data filtering and basic analysis
  - Visualizations (`03_📈_Visualizations.py`) - Interactive chart creation with Plotly
  - Dashboard (`04_📊_Dashboard.py`) - Multi-component dashboard builder
  - Data Entry (`05_✏️_Data_Entry.py`) - Manual data input and dataset creation
  - Advanced Analytics (`06_🧪_Advanced_Analytics.py`) - Machine learning and predictive modeling
  - Statistical Tests (`07_📋_Statistical_Tests.py`) - Comprehensive hypothesis testing
  - Data Profiling (`08_🔎_Data_Profiling.py`) - Automated data quality assessment

### Data Management Layer
- **DataHandler Class**: Core data operations including multi-format file loading, encoding detection, and metadata tracking
- **File Format Support**: CSV, Excel (.xlsx, .xls), and JSON with automatic encoding detection for robust parsing
- **In-Memory Storage**: Session-based storage using pandas DataFrames with comprehensive metadata tracking
- **Data Validation**: Built-in error handling, duplicate detection, and data type inference

### Analytics Engine
- **StatisticsManager**: Comprehensive descriptive statistics, correlation analysis, and distribution testing
- **AdvancedAnalytics**: Machine learning capabilities including regression, classification, clustering, PCA, and time series analysis
- **StatisticalTests**: Hypothesis testing suite with normality tests, two-sample tests, ANOVA, and non-parametric alternatives
- **DataProfiler**: Automated data quality assessment with missing value analysis and distribution profiling
- **OutlierDetector**: Multiple outlier detection methods including IQR, Z-score, Modified Z-score, and Isolation Forest

### Visualization System
- **VisualizationManager**: Plotly-based interactive visualization creation with customizable themes and layouts
- **Chart Types**: Scatter plots, line charts, histograms, box plots, heatmaps, correlation matrices, and distribution comparisons
- **Dashboard Builder**: Multi-component dashboard creation with flexible grid layouts and auto-refresh capabilities

### Statistical Testing Framework
- **Normality Testing**: Shapiro-Wilk, Kolmogorov-Smirnov, Anderson-Darling, and D'Agostino tests
- **Hypothesis Testing**: T-tests, chi-square tests, ANOVA, Kruskal-Wallis, and Wilcoxon tests
- **Multiple Comparison Corrections**: Bonferroni, Benjamini-Hochberg, and other p-value adjustment methods

### Machine Learning Pipeline
- **Preprocessing**: StandardScaler integration, automatic categorical encoding, and feature selection
- **Model Support**: Linear/Logistic regression, Random Forest, Decision Trees with cross-validation
- **Clustering**: K-means clustering with silhouette analysis and optimal cluster determination
- **Dimensionality Reduction**: PCA with explained variance analysis and component interpretation
- **Model Evaluation**: Comprehensive metrics including R², RMSE, accuracy, classification reports

### Report Generation
- **Automated Reporting**: Comprehensive data profiling reports with quality metrics and recommendations
- **Export Capabilities**: Multiple output formats for analysis results and visualizations
- **Quality Assessment**: Data completeness, consistency checks, and outlier identification

## External Dependencies

### Core Framework
- **Streamlit**: Web application framework for the entire user interface and page routing
- **Pandas**: Primary data manipulation and analysis library for DataFrame operations
- **NumPy**: Numerical computing foundation for statistical calculations and array operations

### Visualization Libraries
- **Plotly Express & Graph Objects**: Interactive visualization creation with customizable themes
- **Plotly Subplots**: Multi-panel dashboard and comparison chart creation

### Statistical Computing
- **SciPy**: Statistical functions, hypothesis testing, and probability distributions
- **Statsmodels**: Advanced statistical modeling, multiple comparisons, and regression analysis

### Machine Learning
- **Scikit-learn**: Complete machine learning pipeline including preprocessing, modeling, and evaluation
- **StandardScaler & LabelEncoder**: Data preprocessing and categorical variable handling
- **Cross-validation & Metrics**: Model evaluation and performance assessment tools

### Data Processing
- **OpenPyXL**: Excel file reading and processing capabilities
- **JSON**: Built-in JSON file handling for structured data import
- **IO Libraries**: Stream processing for file uploads and encoding detection

### Development Tools
- **Warnings**: Error suppression for cleaner user experience during statistical computations
- **Datetime**: Timestamp handling for data profiling and metadata tracking
- **Typing**: Type hints for improved code maintainability and IDE support