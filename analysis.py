# PROGRAMMING AND SCRIPTING PROJECT: ANALYSIS OF THE FISHER’S IRIS DATASET
# Author: Rita Ortega

# Imports all the libraries used in the project:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Reads the CSV file contains on the repository using pandas and sets the name of the columns:

column_name = ['sepal_length', 'sepal_width',
               'petal_length', 'petal_width', 'class']
df = pd.read_csv('iris_data.csv', names=column_name)


# SECTION 1: Analysis Per Variable 

# SECTION 1.1: Brief Description of The Dataset

# Prints out a brief information about the dataset:
print(df.info())

# Prints out the first 10 rows of the dataset:
print(df.head(10))


# SECTION 1.2: Summary of Each Variable

# Creates a txt file called "variables_summary.txt" and writes a summary of each variable in it using pandas
# Also, it converts the summary statistics of the dataframe into a string in order to be able to save it into the file:

filename = "variables_summary.txt"

variables_summary = df.describe(include='all', percentiles=[
                                0.05, 0.25, 0.75, 0.95]).to_string()
with open(filename, 'wt') as f:
    f.write(variables_summary)


# SECTION 1.3: Histogram of Each Quantitative Variable 

variables_histogram = df.hist(bins=15, color='blue', edgecolor='black', grid = False, xlabelsize=8, ylabelsize=8)
plt.suptitle('Variables Histogram',
             fontsize=12.0, fontweight='bold', y=0.99)
plt.savefig("variables_histogram.png")
plt.close()


# SECTION 1.4: Bar Plot for The Variable "Class"

class_barplot = sns.countplot(x='class', data=df )
plt.savefig("class_barplot.png")
plt.close()


# SECTION 1.5: Correlation Between Variables

# Creates a txt file called "variables_correlation.txt" and writes a correlation table of each variable in it.
# Also, it converts the correlation table into a string in order to be able to save it into the file.

filename = "variables_correlation.txt"

variables_correlation = df.corr().to_string()
with open(filename, 'wt') as f:
    f.write(variables_correlation)


# Creates a correlation heatmap using seaborn library:
heatmap_correlation = sns.heatmap(
    df.corr(), vmin=-1, vmax=1, annot=True, linecolor='white', linewidth=1, cmap='GnBu')
heatmap_correlation.set_title(
    'Correlation Heatmap', fontsize=12.0, fontweight='bold')
plt.savefig("correlation_heatmap.png")
plt.close()

# --------------------------------------------------

# SECTION 2: Analysis of Each Quantitative Variable Grouped by Iris Species

# SECTION 2.1: Summary of Each Variable Grouped by Iris Species

filename = 'variables_summary_by_class.txt'
variables_summary_by_class = df.groupby(['class']).describe(percentiles=[
    0.05, 0.25, 0.75, 0.95]).transpose().to_string()

with open(filename, 'wt') as f:
    f.write(variables_summary_by_class)


# SECTION 2.2: Histogram of Each Quantitative Variable Grouped by Iris Species

# Creates four files with histograms by species for each quantitative variable (sepal length, sepal width, petal_length and petal_width):
sepal_lenght_hist = df.hist(column='sepal_length', by='class', bins=15,
                            xlabelsize=8, ylabelsize=8, xrot=360, color='green', edgecolor='black')
plt.suptitle('Sepal Length Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)
plt.savefig("sepal_lenght_hist.png")
plt.close()

sepal_width_hist = df.hist(column='sepal_width', by='class', bins=15,
                           xlabelsize=8, ylabelsize=8, xrot=360, color='pink', edgecolor='black')
plt.suptitle('Sepal Width Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)
plt.savefig("sepal_width_hist.png")
plt.close()

petal_lenght_hist = df.hist(column='petal_length', by='class', bins=15,
                            xlabelsize=8, ylabelsize=8, xrot=360, color='yellow', edgecolor='black')
plt.suptitle('Petal Length Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)
plt.savefig("petal_lenght_hist.png")
plt.close()

petal_width_hist = df.hist(column='petal_width', by='class', bins=15,
                           xlabelsize=8, ylabelsize=8, xrot=360, color='orange', edgecolor='black')
plt.suptitle('Petal Width Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)
plt.savefig("petal_width_hist.png")
plt.close()


# SECTION 2.3: Scatter Plot of Each Pair of Variables

# It has been used the Seaborn library in order to perform this analysis. The result is saved to a png file.

sns.set_style("whitegrid")
sns.set_palette(["g", "m", "c"])
scattter_plots = sns.pairplot(df, hue='class')
plt.suptitle('Pair Plot of Each Pair of Quantitative Variables',
             fontsize=12.0, fontweight='bold', y=1)
plt.savefig("scatter_plots.png")
plt.close()


# SECTION 2.4: Box Plot of Each Quantitative Variable Grouped by Iris Species

# Sets seaborn plotting aesthetics as default
sns.set(style='ticks', palette= 'colorblind')

# Defines plotting region (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2)
plt.gcf().set_size_inches(20, 10)

# Creates boxplot in each subplot for the four quantitative variables by class:
sns.boxplot(data=df, x='class', y='sepal_length', ax=axes[0, 0])
sns.boxplot(data=df, x='class', y='sepal_width', ax=axes[0, 1])
sns.boxplot(data=df, x='class', y='petal_length', ax=axes[1, 0])
sns.boxplot(data=df, x='class', y='petal_width', ax=axes[1, 1])
plt.savefig("box_plots.png")
plt.close()


# SECTION 2.5: Correlation Between Variables Grouped by Iris Species


sns.set(style='ticks')

#  Defines plotting region (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2)
plt.gcf().set_size_inches(20, 10)

df_groupby_class = df.groupby(['class'])

iris_virginica_heatmap_axes = axes[0, 0]
iris_virginica_heatmap_axes.set(title="Correlation Heatmap for Iris Virginica")

iris_setosa_heatmap_axes = axes[0, 1]
iris_setosa_heatmap_axes.set(title="Correlation Heatmap for Iris Setosa")

iris_versicolor_heatmap_axes = axes[1, 0]
iris_versicolor_heatmap_axes.set(title="Correlation Heatmap for Iris Versicolor")

sns.heatmap(df_groupby_class.get_group('Iris-virginica').corr(), vmin=-1, vmax=1, annot=True,
            linecolor='white', linewidth=1, cmap='GnBu', ax=iris_virginica_heatmap_axes)
sns.heatmap(df_groupby_class.get_group('Iris-setosa').corr(), vmin=-1, vmax=1, annot=True,
            linecolor='white', linewidth=1, cmap='GnBu', ax=iris_setosa_heatmap_axes)
sns.heatmap(df_groupby_class.get_group('Iris-versicolor').corr(), vmin=-1, vmax=1, annot=True,
            linecolor='white', linewidth=1, cmap='GnBu', ax=iris_versicolor_heatmap_axes)
axes[1, 1].axis('off')

plt.savefig("heatmap_by_class.png")
plt.close()



