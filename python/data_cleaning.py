"""
Automotive Powertrain Reliability Analysis

Data Cleaning Script

Author: Rohith T
"""

import pandas as pd

# Load datasets
vehicle_master = pd.read_csv("vehicle_master.csv")
failure_profile = pd.read_csv("powertrain_failure_profile.csv")

print(vehicle_master.head())
print(failure_profile.head())
