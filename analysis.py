# PROGRAMMING AND SCRIPTING PROJECT
# Author: Rita Ortega

# SECTION 1: Outputs a summary of each variable to a single text file

# Imports all the modules used in the project:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Reads the CSV file using pandas and sets the name of the columns:

column_name = ['sepal_length','sepal_width','petal_length','petal_width','class']
df = pd.read_csv('iris_data.csv', names = column_name) 

# Creates a txt file called "variables_summary.txt" and writes a summary of each variable in it.
# Also, it converts the Summary statistics of the Dataframe into a string in order to be able to save it into the file:

filename = "variables_summary.txt"
variables_summary = df.describe(include = 'all', percentiles = [0.05, 0.25, 0.75, 0.95]).to_string()
with open(filename, 'wt') as f:
    f.write(variables_summary)



"""

REFERENCES:

https://www.codegrepper.com/code-examples/python/pandas+read+csv+without+index
https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table
https://www.adamsmith.haus/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python#:~:text=Call%20pandas.,order%20they%20appear%20in%20names%20.
https://www.sharpsightlabs.com/blog/pandas-describe/
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
https://github.com/andrewbeattycourseware/pands2022/blob/main/jupyternotebooks/Topic07%20files.ipynb
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html


"""


# SECTION 2: Saves a histogram of each variable to png files

# Creates four files with histograms by class for each quantitative variable (sepal length, sepal width, petal_length and petal_width):
sepal_lenght_hist = df.hist(column ='sepal_length', by= 'class', bins = 15, xlabelsize=8, ylabelsize=8, xrot=360, color='green', edgecolor='black')
plt.suptitle('Sepal Length Histograms by Class', fontsize= 12.0, fontweight= 'bold', y = 0.99)
plt.savefig("sepal_lenght_hist.png")


sepal_width_hist = df.hist(column ='sepal_width', by= 'class', bins = 15, xlabelsize=8, ylabelsize=8, xrot=360, color='blue', edgecolor='black')
plt.suptitle('Sepal Width Histograms by Class', fontsize= 12.0, fontweight= 'bold', y = 0.99)
plt.savefig("sepal_width_hist.png")


petal_lenght_hist = df.hist(column ='petal_length', by= 'class', bins = 15, xlabelsize=8, ylabelsize=8, xrot=360, color='yellow', edgecolor='black')
plt.suptitle('Petal Length Histograms by Class', fontsize= 12.0, fontweight= 'bold', y = 0.99)
plt.savefig("petal_lenght_hist.png")


petal_width_hist = df.hist(column ='petal_width', by= 'class', bins = 15, xlabelsize=8, ylabelsize=8, xrot=360, color='orange', edgecolor='black')
plt.suptitle('Petal Width Histograms by Class', fontsize= 12.0, fontweight= 'bold', y = 0.99)
plt.savefig("petal_width_hist.png")




"""

REFERENCES:
https://moonbooks.org/Articles/How-to-create-an-histogram-from-a-dataframe-using-pandas-in-python-/
https://stackoverflow.com/questions/31596084/save-dataframe-hist-to-a-file
https://www.marsja.se/how-to-plot-a-histogram-with-pandas-in-3-simple-steps/
https://www.machinelearningplus.com/pandas/pandas-histogram/
https://datagy.io/histogram-python/
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
https://stackoverflow.com/questions/19614400/add-title-to-collection-of-pandas-hist-plots
https://www.includehelp.com/python/bold-text-label-in-plot.aspx
https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html



"""


# SECTION 3: Outputs a scatter plot of each pair of variables

# It has been used the Seaborn library in order to perform this analysis. The result is saved to a png file. 
sns.set_style("whitegrid")
sns.set_palette(["g", "m", "c"])
scattter_plots = sns.pairplot(df, hue = 'class')
plt.suptitle('Pair Plot of Each Pair of Quantitative Variables', fontsize = 12.0, fontweight = 'bold', y = 1)
plt.savefig("scatter_plots.png")




"""

REFERENCES:
https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
https://www.tutorialspoint.com/increase-the-distance-between-the-title-and-the-plot-in-matplotlib
https://seaborn.pydata.org/generated/seaborn.pairplot.html
https://seaborn.pydata.org/generated/seaborn.set_style.html
https://goodboychan.github.io/python/datacamp/visualization/2020/06/27/01-Customizing-Seaborn-Plots.html
https://wellsr.com/python/seaborn-scatter-plot-with-sns-scatterplot/





"""


# SECTION 4: Additional analysis that I think is appropriate for this case







