import pandas as pd
import matplotlib.pyplot as plt
import os

# Check file size
if os.path.getsize('matches.csv') == 0:
    print("Error: matches.csv is empty. Please download correct dataset.")
    exit()

if os.path.getsize('deliveries.csv') == 0:
    print("Error: deliveries.csv is empty. Please download correct dataset.")
    exit()

# Load datasets
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

print("Files loaded successfully!")