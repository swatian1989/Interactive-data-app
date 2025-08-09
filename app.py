import streamlit as st
import pandas as pd
import numpy as np
from utils.data_handler import DataHandler
import warnings

warnings.filterwarnings('ignore')

# Configure page
st.set_page_config(
    page_title="Interactive Data App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'data_handler' not in st.session_state:
    st.session_state.data_handler = DataHandler()

# Sidebar navigation info
with st.sidebar:
    st.markdown("### Navigation")
    st.markdown("Use the pages in the sidebar to:")
    st.markdown("- 📁 **Data Upload**: Upload and manage your datasets")
    st.markdown("- 🔍 **Data Exploration**: Explore and filter your data")
    st.markdown("- 📈 **Visualizations**: Create interactive charts and graphs")
    st.markdown("- 📊 **Dashboard**: Build custom dashboards")
    st.markdown("- ✏️ **Data Entry**: Add new data manually")
    st.markdown("- 🧪 **Advanced Analytics**: Machine learning and predictive modeling")
    st.markdown("- 📋 **Statistical Tests**: Comprehensive hypothesis testing")
    st.markdown("- 🔎 **Data Profiling**: Automated data quality assessment")

# Main page content
st.title("📊 Interactive Data App")
st.markdown("### Welcome to your comprehensive data analysis workspace")

# Overview metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Datasets Loaded",
        value=len(st.session_state.data_handler.datasets),
        help="Number of datasets currently loaded in the session"
    )

with col2:
    total_rows = sum(len(df) for df in st.session_state.data_handler.datasets.values())
    st.metric(
        label="Total Rows",
        value=f"{total_rows:,}",
        help="Total number of rows across all loaded datasets"
    )

with col3:
    total_cols = sum(len(df.columns) for df in st.session_state.data_handler.datasets.values())
    st.metric(
        label="Total Columns",
        value=total_cols,
        help="Total number of columns across all loaded datasets"
    )

with col4:
    memory_usage = sum(df.memory_usage(deep=True).sum() for df in st.session_state.data_handler.datasets.values()) / 1024 / 1024
    st.metric(
        label="Memory Usage",
        value=f"{memory_usage:.1f} MB",
        help="Total memory usage of loaded datasets"
    )

# Quick start guide
st.markdown("### Quick Start Guide")

with st.expander("🚀 Getting Started", expanded=True):
    st.markdown("""
    **Step 1: Upload Your Data**
    - Navigate to the "Data Upload" page
    - Upload CSV, Excel, or JSON files
    - Preview and validate your data
    
    **Step 2: Explore Your Data**
    - Use the "Data Exploration" page to filter and examine your data
    - View statistics and data quality information
    
    **Step 3: Create Visualizations**
    - Go to "Visualizations" to create charts and graphs
    - Choose from multiple chart types and customize as needed
    
    **Step 4: Build Dashboards**
    - Combine multiple visualizations in the "Dashboard" page
    - Create comprehensive views of your data
    
    **Step 5: Advanced Analysis**
    - Use "Statistical Tests" for hypothesis testing
    - Apply "Advanced Analytics" for machine learning
    - Generate automated reports with "Data Profiling"
    
    **Step 6: Add New Data**
    - Use "Data Entry" to manually add new records to your datasets
    """)

# Show current datasets if any exist
if st.session_state.data_handler.datasets:
    st.markdown("### Current Datasets")
    
    for name, df in st.session_state.data_handler.datasets.items():
        with st.expander(f"📋 {name}", expanded=False):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Rows", f"{len(df):,}")
            with col2:
                st.metric("Columns", len(df.columns))
            with col3:
                st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
            with col4:
                if st.button(f"Remove {name}", key=f"remove_{name}"):
                    del st.session_state.data_handler.datasets[name]
                    st.rerun()
            
            st.markdown("**Column Types:**")
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.astype(str),
                'Non-Null Count': df.count(),
                'Null Count': df.isnull().sum()
            })
            st.dataframe(col_info, use_container_width=True)

else:
    st.info("👆 Start by uploading some data using the 'Data Upload' page in the sidebar!")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit for interactive data analysis*")
