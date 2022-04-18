# PROGRAMMING AND SCRIPTING PROJECT
# Author: Rita Ortega

# SECTION 1: Outputs a summary of each variable to a single text file

import pandas as pd

# Reads the CSV file using pandas and sets the name of the columns:

column_name = ['sepal_length','sepal_width','petal_length','petal_width','class']
df = pd.read_csv('iris_data.csv', names = column_name) 

# Creates a txt file called "variables_summary.txt" and writes a summary of each variable in it.
# Also, it converts the Summary statistics of the Dataframe into a string in order to be able to save it into the file
filename = "variables_summary.txt"
with open(filename, 'wt') as f:
    f.write(df.describe(include = 'all', percentiles = [0.05, 0.25, 0.75, 0.95]).to_string())



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


# SECTION 3: Outputs a scatter plot of each pair of variables


# SECTION 4: Additional analysis that I think is appropriate for this case







