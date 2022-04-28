# PROGRAMMING AND SCRIPTING PROJECT: ANALYSIS OF THE FISHER’S IRIS DATASET
# Author: Rita Ortega

# Imports all the libraries used in the project (Pandas, Matplotlib and Seaborn):
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Reads the CSV file contains on the repository (iris_data.csv) into a Dataframe. Also, it sets the name of the columns:
column_name = ['sepal_length', 'sepal_width',
               'petal_length', 'petal_width', 'class']
df = pd.read_csv('iris_data.csv', names=column_name)


# SECTION 1: Analysis Per Variable
# This section is divided into five subsections in which I use python to perform an analysis per variable.

# SECTION 1.1: Brief Description of The Dataset

# Prints out a brief information of the DataFrame:
df.info()

# Prints out the first 10 rows of the DataFrame:
print(df.head(10))


# SECTION 1.2: Summary of Each Variable

# Creates a txt file called "variables_summary.txt" and writes in it a statistical summary of each variable using Pandas describe() method.
# Also, it converts the statistical summary of the DataFrame into a string in order to be able to save it into the file:
filename = "variables_summary.txt"

variables_summary = df.describe(include='all', percentiles=[
                                0.05, 0.25, 0.75, 0.95]).to_string()
with open(filename, 'wt') as f:
    f.write(variables_summary)


# SECTION 1.3: Histogram of Each Quantitative Variable

# Creates a histogram for each quantitative variable by calling the Pandas hist() method. I set the histogram to contain
# 15 bins whose colour is blue with black edges. Also, I hid the grid and set the x and y axes label size to 8:
df.hist(
    bins=15, color='blue', edgecolor='black', grid=False, xlabelsize=8, ylabelsize=8)

# Adds a title to the plot whose font size is 12 and bold. The vertical position is also set, which is 0.99:
plt.suptitle('Variables Histogram',
             fontsize=12.0, fontweight='bold', y=0.99)

# Saves the figure to a .png file called "variables_histogram.png":
plt.savefig("variables_histogram.png")

# Closes the current figure so that not subsequent plots are added to this figure:
plt.close()


# SECTION 1.4: Bar Plot for The Variable "Class"

# Uses the countplot() method of the Seaborn library to count the observations of each iris species (class variable) and it plots them in bars:
sns.countplot(x='class', data=df)

# Saves the bar plot to a .png file called "class_barplot.png":
plt.savefig("class_barplot.png")

# Closes the current figure so that not subsequent plots are added to this figure:
plt.close()


# SECTION 1.5: Correlation Between Variables

# Creates a txt file called "variables_correlation.txt" and writes in it a correlation matrix of each variable using Pandas corr() method.
# Also, it converts the correlation table into a string in order to be able to save it into the file:
filename = "variables_correlation.txt"

variables_correlation = df.corr().to_string()
with open(filename, 'wt') as f:
    f.write(variables_correlation)

# Creates a correlation heatmap by calling the heatmap() method of the Seaborn library and the corr() method of the Pandas library.
# I also adjust the colourmap to the interval [-1, 1] as the correlation doesn't go beyond those limits.
# Lastly, I customized the line colour, line width and the colourmap:
heatmap_correlation = sns.heatmap(
    df.corr(), vmin=-1, vmax=1, annot=True, linecolor='white', linewidth=1, cmap='GnBu')

# Adds a title to the heatmap whose font size is 12 and font weight is bold:
heatmap_correlation.set_title(
    'Correlation Heatmap', fontsize=12.0, fontweight='bold')

# Saves the heatmap to a .png file called "correlation_heatmap.png":
plt.savefig("correlation_heatmap.png")

# Closes the current figure so that not subsequent plots are added to this figure:
plt.close()

# --------------------------------------------------

# SECTION 2: Analysis of Each Quantitative Variable Grouped by Iris Species
# This section is divided into five subsections in which I use python to perform an analysis to study
# the existing differences between the three species of Iris flowers.


# SECTION 2.1: Summary of Each Variable Grouped by Iris Species

# Creates a txt file called 'variables_summary_by_class.txt' and writes in it a statistical summary of each quantitative variable grouped by class
# using Pandas describe() method. Also, the statistical summary is transposed for better readability. Lastly, it converts the statistical summary of
# the DataFrame into a string in order to be able to save it into the file:
filename = 'variables_summary_by_class.txt'
variables_summary_by_class = df.groupby(['class']).describe(percentiles=[
    0.05, 0.25, 0.75, 0.95]).transpose().to_string()

with open(filename, 'wt') as f:
    f.write(variables_summary_by_class)


# SECTION 2.2: Histogram of Each Quantitative Variable Grouped by Iris Species

# The code of this section creates four .png files with histograms grouped by species for each quantitative variable
# (sepal length, sepal width, petal_length and petal_width). Thus, each file will have:
# - A histogram for each specie available (in this case, there will be 3 of them).
# - A title which will be based on the quantitative variable in hand.
# - The colour for the histograms of each variable will be different to make them more readable and understandable.

# As a next step, I continue with the explanation of the code:

# Creates a histogram grouped by iris species for the variable sepal length by calling the Pandas hist() method. I set the histogram to contain
# 15 bins whose colour is green with black edges. Also, I set the x and y axes label size to 8 and set the rotation of the x axis label to 0:
df.hist(column='sepal_length', by='class', bins=15,
        xlabelsize=8, ylabelsize=8, xrot=0, color='green', edgecolor='black')

# Adds a title to the plot whose font size is 12 and bold. The vertical position is also set, which is 0.99:
plt.suptitle('Sepal Length Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)

# Saves the histograms to a .png file called "sepal_lenght_hist.png":
plt.savefig("sepal_lenght_hist.png")

# Closes the current figure so that not subsequent plots are added to this figure:
plt.close()


# Creates a histogram grouped by iris species for the variable sepal width by calling the Pandas hist() method. I set the histogram to contain
# 15 bins whose colour is pink with black edges. Also, I set the x and y axes label size to 8 and set the rotation of the x axis label to 0:
df.hist(column='sepal_width', by='class', bins=15,
        xlabelsize=8, ylabelsize=8, xrot=0, color='pink', edgecolor='black')

# Adds a title to the plot whose font size is 12 and bold. The vertical position is also set, which is 0.99:
plt.suptitle('Sepal Width Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)

# Saves the histograms to a .png file called "sepal_width_hist.png":
plt.savefig("sepal_width_hist.png")

# Closes the current figure so that not subsequent plots are added to this figure:
plt.close()


# Creates a histogram grouped by iris species for the variable petal length by calling the Pandas hist() method. I set the histogram to contain
# 15 bins whose colour is yellow with black edges. Also, I set the x and y axes label size to 8 and set the rotation of the x axis label to 0:
df.hist(column='petal_length', by='class', bins=15,
        xlabelsize=8, ylabelsize=8, xrot=0, color='yellow', edgecolor='black')

# Adds a title to the plot whose font size is 12 and bold. The vertical position is also set, which is 0.99:
plt.suptitle('Petal Length Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)

# Saves the histograms to a .png file called "petal_lenght_hist.png":
plt.savefig("petal_lenght_hist.png")

# Closes the current figure so that not subsequent plots are added to this figure:
plt.close()

# Creates a histogram grouped by iris species for the variable petal width by calling the Pandas hist() method. I set the histogram to contain
# 15 bins whose colour is orange with black edges. Also, I set the x and y axes label size to 8 and set the rotation of the x axis label to 0:
df.hist(column='petal_width', by='class', bins=15,
        xlabelsize=8, ylabelsize=8, xrot=0, color='orange', edgecolor='black')

# Adds a title to the plot whose font size is 12 and bold. The vertical position is also set, which is 0.99:
plt.suptitle('Petal Width Histograms by Class',
             fontsize=12.0, fontweight='bold', y=0.99)

# Saves the histograms to a .png file called "petal_width_hist.png":
plt.savefig("petal_width_hist.png")

# Closes the current figure so that not subsequent plots are added to this figure:
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
sns.set(style='ticks', palette='colorblind')

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
iris_versicolor_heatmap_axes.set(
    title="Correlation Heatmap for Iris Versicolor")

sns.heatmap(df_groupby_class.get_group('Iris-virginica').corr(), vmin=-1, vmax=1, annot=True,
            linecolor='white', linewidth=1, cmap='GnBu', ax=iris_virginica_heatmap_axes)
sns.heatmap(df_groupby_class.get_group('Iris-setosa').corr(), vmin=-1, vmax=1, annot=True,
            linecolor='white', linewidth=1, cmap='GnBu', ax=iris_setosa_heatmap_axes)
sns.heatmap(df_groupby_class.get_group('Iris-versicolor').corr(), vmin=-1, vmax=1, annot=True,
            linecolor='white', linewidth=1, cmap='GnBu', ax=iris_versicolor_heatmap_axes)
axes[1, 1].axis('off')

plt.savefig("heatmap_by_class.png")
plt.close()
