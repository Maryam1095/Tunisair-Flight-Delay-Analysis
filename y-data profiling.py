# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:20:55 2024

@author: USER
"""

import pandas as pd
import warnings
from sklearn.impute import SimpleImputer
data = pd.read_csv("Tunisair_flights_dataset.csv")

# Display the first few rows using head() and information about the dataset using info()
data_head = data.head() 
data_information = data.info()

# Check for missing values in the dataset
missing_values = data.isnull().sum()

# Calculate summary statistics for numerical columns using describe()
data_statistics = data.describe()

#SECTION 2 PANDAS PROFILING

from ydata_profiling import ProfileReport
import pandas as pd

# Load the dataset into a pandas DataFrame
dataset = pd.read_csv("Tunisair_flights_dataset.csv")  

# Generate the profile report using pandas-profiling
profile = ProfileReport(df=dataset, dark_mode=True, explorative=True, title='Pandas Profiling Report')
profile.to_widgets()  
profile.to_file(output_file="data_exploration_report.html")  # Save the report as HTML file