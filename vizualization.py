# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:41:06 2023

@author: Anuhya
"""
import pandas as pd  # Inputing file (eg, pd.read_csv), Data-processing
import numpy as np  # Linear Algebra
import matplotlib.pyplot as plt  # Visualisation
import warnings  # Supress warnings
import seaborn as sns  # getting seaborn

data = pd.read_csv("Tuberculosis.csv", index_col=0)  # reading the data

# line plot function


def linePlot(linePlotData):
    sns.set_style("whitegrid")  # seaborn style

    # Listing countries to plot
    countries = ["Algeria", "Egypt,Arab Rep.", "Iran,Islamic Rep.",
                 "Iraq", "Israel", "Kuwait", "Saudi Arabia"]

    # Create DataFrame for plotting
    plot_df = linePlotData[['year'] + countries]

    # Visualizing through line plot
    plot_df.set_index('year').plot(marker='o').figsize = (20, 10)

    plt.title('Tuberculosis case detection rate of Middle east and south africa')
    plt.xlabel('Years')  # setting x label
    plt.ylabel('Tuberculosis case detection rate')  # setting y label
    plt.legend(countries, loc='best', fontsize='small')


# bar plot function
def barPlot(barData):

    sns.set_style("whitegrid")  # seaborn style
    barData.plot(x='year', y=['Algeria', 'Israel'], kind='bar', 
                 title='Comparison of Algeria and Israel Case Detection',
                 xlabel='Years', ylabel='Cases Detected', 
                 color=('red', 'green'), legend=True, 
                 figsize=(16, 6), width=0.65)
    plt.show()


def boxPlot(df):
    # Melt the DataFrame to create a suitable format for the box plot
    melted_df = pd.melt(df, id_vars='year', var_name='Country',
                        value_name='Case Detection')

    # Set seaborn style
    sns.set(style="whitegrid")

    # Create a box plot using seaborn
    plt.figure(figsize=(12, 6))
    plt.boxplot(x='Country', y='Case Detection',
                data=melted_df, showfliers=False)
    plt.title('Box Plot of Case Detection by Country')
    plt.xlabel('Country')
    plt.ylabel('Case Detection')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility


# deleting the country_code column
data_frame = data.drop(['Country Code'], axis='columns')

df = data_frame.reset_index(drop=True)  # reseting the index

df_t = data_frame.transpose()  # transposing for better clarity
print(df_t)
df2 = df_t.reset_index(drop=True)  # reseting the data
df2 = df2.shift(-1)  # getting one row above
print(df2)

# year values
year = pd.Series([2013, 2014, 2015,
                  2016, 2017, 2018, 2019, 2020, 2021], dtype=object)

df2['year'] = year  # creating the year column
# adding the countries to data set
df2.columns = pd.Series(["Algeria", "Egypt,Arab Rep.", "Iran,Islamic Rep.",
                        "Iraq", "Israel", "Kuwait", "Saudi Arabia", "year"],
                        dtype=object)

# removing the nan values
final_Data_frame = df2.dropna()

# final data frame
df_final = pd.concat([final_Data_frame.iloc[:, -1:],
                     final_Data_frame.iloc[:, :-1]], axis=1)
print(df_final)

# plotting for df_final
linePlot(df_final)

barPlot(df_final)

boxPlot(df_final)
