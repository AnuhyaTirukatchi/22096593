#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
from scipy.stats import norm

warnings.filterwarnings("ignore")


# In[24]:


# Specify the path to your CSV file
file_path = 'data3-2_-959907583.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path,  names=['Salaries'])


# In[25]:


# Define the normal_pdf function
def normal_pdf(x, mean, std_dev):
    """
    Calculate the probability density function (PDF) for a normal distribution.

    Parameters:
    - x: The variable for which the PDF is calculated.
    - mean: The mean of the distribution.
    - std_dev: The standard deviation of the distribution.

    Returns:
    - The PDF value for the given x.
    """
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -((x - mean) ** 2) / (2 * std_dev ** 2)
    pdf_value = coefficient * np.exp(exponent)
    return pdf_value


# In[34]:



# Calculate mean and standard deviation from the sample
mean_salary = df['Salaries'].mean()
std_dev_salary = df['Salaries'].std()

# Create a range of values for the x-axis
x_vals = np.linspace(df['Salaries'].min(), df['Salaries'].max(), 1000)

# Calculate the PDF using the normal_pdf function
pdf_vals = normal_pdf(x_vals, mean_salary, std_dev_salary)


# Calculate the salary value below which 33% have a salary using the CDF
percentile_33_salary = norm.ppf(0.33, loc=mean_salary, scale=std_dev_salary)




# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot histogram with PDF
sns.histplot(data=df, x='Salaries',  kde=True, color='skyblue', bins=30, stat='density', label='Histogram & KDE')

# Plot the PDF calculated using the normal_pdf function
sns.lineplot(x_vals, pdf_vals, label='PDF(normal distribution)', color='blue')

# Mark the mean salary on the graph
plt.axvline(mean_salary, color='red', linestyle='--', label=f'Mean Salary ($\widetilde{{W}}$): {mean_salary:.2f}')


# Mark the salary value below which 33% have a salary
plt.axvline(percentile_33_salary, color='green', linestyle='--', label=f'33% Below ($X$): {percentile_33_salary:.2f}')

# Add labels and title
plt.title('Salaries Distribution with PDF and Mean Salary')
plt.xlabel('Salaries')
plt.ylabel('Density')
plt.legend()

# Show the plot
plt.show()
