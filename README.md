# pands-project

### This repository contains the solution to the project of the module: " Programming and Scripting" for the Higher Diploma in Computing in Data Analytics.
***
***

# 1. About this Repository
The purpose of this repository is to carry out an analysis of the well-known Fisher’s Iris data set as it is required for the Project on Programming and Scripting. In order to do that, this repository is made up of the following files and folders:
* A README file that contains how to run the code, a summary of the dataset and the explanation of the analysis performed.
* A images folder that contains .png files with the output obtained after running the code. This folder has been created to store the images that have been used in the README for a better explanation of the analysis done.
* The iris_data.csv file, which contains the dataset used during the analysis.
* Some generated .txt files, which are obtained by running the code (variables_summary.txt, variables_correlation.txt and variables_summary_by_class.txt)
* Some  generated .png files, which are obtained by running the code (box_plots.png, class_barplot.png, correlation_heatmap.png, heatmap_by_class.png, petal_lenght_hist.png, petal_lenght_width.png, scatter_plots.png, sepal_lenght_hist.png, sepal_width_hist.png and variables_histogram.png)
* The Python script containing the Python code used to investigate the Iris dataset, which is called analysis.py.   

I would like to point out that in order to run this code you will need the following requirements:
* You need to have installed on your pc Python 3 or greater.
* The analysis has been done using three different libraries: [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/). For that reason, you need to install them if you do not have them already using the `pip install` command following the name of the respective library. 
* Finally, you have to clone the repository and in the root directory run `python analysis.py`.

# 2. The Dataset
The objective of this project is about performing several analyses on the well-known Fisher’s Iris dataset. According to [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris) and [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set), this dataset quantifies the morphotic variation of 50 records for each of three Iris species:  Iris Setosa, Iris Virginica, and Iris Versicolor. Thus, the dataset is made of 150 samples which quantify the width and height of both the sepal and petal of each flower measured in centimetres. Thereby, The Fisher’s Iris dataset is composed of the following attributes: 
1. Sepal length in cm
2. Sepal width in cm
3. Petal length in cm
4. Petal width in cm
5. Class:  Iris Setosa, Iris Virginica, and Iris Versicolor

      <img src="images/iris_flowers.jpeg" alt="iris_flowers" width="800">

The dataset is named after a British statistician and biologist called Ronald Fisher, who introduced it in his 1936 paper about linear discriminant analysis called "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis". I would like to point out that this dataset is so popular that it has been used since its creation as a test case throughout the data analytics field, such as machine learning and data mining. 

The dataset has been added to the repository in a CSV file called "iris-data.csv", which has been downloaded from The UCI Machine Learning Repository website [link here](http://archive.ics.uci.edu/ml/machine-learning-databases/iris/). 


# 3. Analysis of The Iris Dataset
The analysis of the dataset has been split into two sections, which are clearly specified in the code. In the first section called "Analysis Per Variable", I realised some different analyses focus on each individual variable. On the other hand, the second section contains an analysis of each quantitative variable (sepal length, sepal width, petal length and petal width) grouped by the variable class. You can find this second section in the code by the name "Analysis of Each Quantitative Variable Grouped by Iris Species".

I would like to point out that within these sections the code has been organized into different subsections so I am going to follow the same structure throughout the explanation of the analysis in order to make it easier to follow. 

After this clarification, I proceed to expose the research carried out on the database and the insights obtained.

## 3.1. Analysis Per Variable
This section is divided into five subsections in which as a first step, a brief description of the dataset is made in order to obtain a better knowledge of the database that we have and the type of analyses suitable for it. In addition, we carry out a summary of each variable and different types of visualizations, which allow us to form hypotheses, uncover potential patterns in the data and identify strongly correlated variables.

Without further ado, I will present the insights obtained in this first section of the analysis.

### 3.1.1. Brief Description of The Dataset
 The very first step required in the data analysis process involves exploring the dataset we have for the purpose of getting a better understanding of the data that is going to be analysed. By getting to know the data better, we can become more efficient in navigating through the data and using them in our analysis([Pomiklo, 2021](https://dsstream.com/data-exploration-definition-and-techniques/)).

In this section, the Pandas library was used since it has many functions that can be used to explore a dataset. First of all, I used the `info()` method, which allows us to print out a piece of brief information about the Iris dataset such as the number of columns, column labels, column data types, memory usage, etc...

We can see that the dataset is composed of 150 records and there are no null values. Moreover, four variables are float data types (sepal length, sepal width, petal length and petal width) and the fifth column is an object data type (class). 

<img src="images/dataframe_info.png" alt=dataframe_info width="300">

To finish this section, the Pandas `head()` method has been used. This function is useful to take a quick look at how the database is structured. In this case, it displays the first ten rows of the dataset.

<img src="images/dataset_first_10_rows.png" alt=dataframe_info width="500">

I would like to point out that the two previous tables are printed out when you run the code so they are not saved into a file as all the next analyses ([Sharma, 2021](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda)).

### 3.1.2. Summary of Each Variable
As the next step in my exploratory data analysis, I have used the Pandas `describe()` method to obtain a statistical summary of each variable([InDeepData, 2021](https://indeepdata.com/blog/exploratory-data-analysis/)). This information is sent to a text file called "variables_summary" once you run the code.

<img src="images/variables_summary.png" alt="variables_summary" width="400">

From the previous table we can get the following insights:
* There are 50 observations for each Iris specie in the dataset.
* The sepal and petal are usually longer than they are wide. Also, we can see that the sepals are on average bigger than the petals.
* The standard deviation shows that there is more variability in the petal measurements than in the sepal ones.
* The maximum value in the sample is reached by the sepal length variable with 7.9 cm and the minimum is reached by the petal width variable with 0.1 cm. 

### 3.1.3. Histogram of Each Quantitative Variable
The histograms are the most commonly used plot to show how often each different value in a set of data occurs. That is, they are used to show frequency distribution in continuous variables.

For the purpose of analyzing how each quantitative variable is distributed, I have represented each continuous variable in one different histogram([Kumar, 2019](https://www.kaggle.com/code/rakesh6184/seaborn-plot-to-visualize-iris-data/notebook)).

<img src="images/variables_histogram.png" alt="variables_histogram" width="400">	

The histograms show that most of the petals of the sample are smaller than the sepals. Moreover, we can see that the sepals present a greater variability in the measurements than the petals. Lastly, I would like to highlight that the sepal width's histogram almost follows a normal distribution, which is also known as a Gaussian distribution or bell curve ([Sideroba, 2019](https://getnave.com/blog/histogram-diagram/)).

### 3.1.4. Bar Plot for The Variable "Class"
In this subsection, I have used a bar chart to compare the samples of each iris specie (Iris Setosa, Iris Virginica, and Iris Versicolor), since this type of plot is used when you need to represent categorical variables. 

<img src="images/class_barplot.png" alt="class_barplot" width="400">	

Analysing the bar plot, we can see that the dataset is well balanced since there are 50 samples of each species ([Kumar, 2022](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/#:~:text=Iris%20Dataset%20is%20considered%20as,flowers%20and%20recorded%20them%20digitally))

### 3.1.5. Correlation Between Variables
To finish with the analysis of this first section, in which I have been carrying out an analysis per variable, I am going to study the correlation between variables. The correlation is a statistical measure that shows if two variables are related. It takes values between -1 and 1 to show the level of correlation between variables ([McLeod, 2020](https://www.simplypsychology.org/correlation.html)).

In the table below, we can see that the variables petal length and petal width have a high positive correlation (0.96). Also, we can see that the petal length and the sepal length have a good positive correlation(0.87). 

A positive correlation means that one variable increases as the other variable increases, in the same way, when one variable decreases the other decreases.

<img src="images/variables_correlation.png" alt="variables_correlation" width="400">

The correlations can be visualised more easily on the below heatmap. A large amount of dark blue squares shows that the majority of variables are positively correlated with each other.  

<img src="images/correlation_heatmap.png" alt="correlation_heatmap" width="400">

## 3.2. Analysis of Each Quantitative Variable Grouped by Iris Species
This section is divided into five subsections, as the previous section is. As a first step, a summary of each quantitative variable grouped by Iris species is presented. In addition, I have made use of different types of visualizations to analyze the existing differences between the three species of Iris flowers. 

In the following lines, I will present the insights obtained in this section of the analysis.

### 3.2.1. Summary of Each Variable Grouped by Iris Species
We start the exploratory analysis of this new section with a statistical summary of each variable grouped by Iris species. This information is sent to a text file called "variables_summary_by_class.txt" once you run the code.

<img src="images/variables_summary_by_class.png" alt="variables_summary_by_class" width="400">

From the previous table we can get the following insights:
* The Iris Versicolor and the Iris Virginica are the most similar in measurements. That is, these two types of Iris species are the most similar to each other.
* The standard deviation shows that there is more variability in the Iris Virginia specie measurements than in the other ones.
* The maximum value in the sample is reached by the Iris Virginica with 7.9 cm of sepal length and the minimum is reached by the Iris Setosa with 0.1 cm of petal width.

### 3.2.2. Histogram of Each Quantitative Variable Grouped by Iris Species
To continue the analysis, I have made a histogram for each quantitative variable (sepal length, sepal width, petal length and petal width) broken down by iris species. Thus, we can analyze the differences in frequency distribution among iris species per attribute. I have decided to represent each feature in a different colour in order to make them more readable and understandable. 

Without further ado, I will present the insights obtained in this subsection of the analysis.

First of all, it is exposed the histograms for the variable sepal length.  We can see that the Iris Setosa present less variability in this measurement than the other two species. In addition, the histograms show that the Iris Virginica's sepal length measurements are greater in most of the samples than in the rest of the iris species. On the other hand, the Iris Setosa has more samples with the sepal length smaller than the rest of the species. 

<img src="images/sepal_lenght_hist.png" alt="sepal_lenght_hist" width="400">

Regarding the sepal width, the Iris Setosa is the one that reaches higher values in this attribute. Also, we can see that the vast majority of the samples are concentrated in values that oscillate between 2.5 and 3.5 centimetres.

<img src="images/sepal_width_hist.png" alt="sepal_width_hist" width="400">

The next histograms show the results for the variable petal length. In this case, we can see that the samples of the Iris Virginica's petal length measurements are greater in most of the samples than in the two other species. Moreover, the differences in this variable among iris species are more differentiated than in the rest of the variables. I would like to highlight that the Iris Setosa's histogram almost follows a normal distribution ([Sideroba, 2019](https://getnave.com/blog/histogram-diagram/)).

<img src="images/petal_lenght_hist.png" alt="petal_lenght_hist" width="400">

Finally, we have the histograms of the variable petal width. In the case of this variable, we can see that for the Iris Setosa most of the samples has around 0.2 cm. On the other hand, the other two species have greater variability of sizes. I would like to point out that the Iris Virginica is the specie with the greatest sepals width in the sample. 

<img src="images/petal_width_hist.png" alt="petal_width_hist" width="400">

The previous histograms illustrate how the frequency distributions present great differences between each iris species. 

###  3.2.3. Scatter Plot of Each Pair of Variables
At this stage in the analysis, I found it interesting to use scatter plots to determine if there are patterns or correlations between each pair of variables ([West, 2020](https://visme.co/blog/scatter-plot/)).

In order to do that, I have made use of Seaborn's function `pairplot()` , which is very useful to scatter plot all variables at once in a single figure. This function allows us to see both distributions of single variables and relationships between two variables. It is built on two basic figures, the histogram and the scatter plot. The histogram on the diagonal allows us to see the distribution of a single variable while the scatter plots on the upper and lower triangles show the relationship (or lack thereof) between two variables ([Koehrsen, 2018](https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166)). I would like to point out that each iris species has been assigned a colour with the aim of being able to make the comparison according to the iris species.

<img src="images/scatter_plots.png" alt="scatter_plots" width="750">

As per the previous plot ([InDeepData, 2021](https://indeepdata.com/blog/exploratory-data-analysis/)), we can see that the Iris Setosa seems to be clearly differentiated from the other two iris species. These other two iris species (Iris Versicolor and Iris Virginica)
even tend to overlap with each other. However, the plots illustrated that the Iris Virginica usually has longer and wider petals than the Iris Versicolor.  

###  3.2.4. Box Plot of Each Quantitative Variable Grouped by Iris Species
Following the analysis, I have made use of a box plot per variable grouped by iris species. This type of visualization displays different useful information about a dataset ([Galarnyk, 2018](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51)): 
* The distribution of the data based on a five-number summary (minimum value, first quartile, median, third quartile and maximum value).
* The presence or lack of outliers.
* It can also tell you if the data is symmetrical and how the data is skewed.

<img src="images/box_plots.png" alt="box_plots" width="750">

From the above plot, we can see that Iris Setosa is the specie with the presence of more outliers. In addition, for most of the attributes the Iris Setosa is the specie less distributed and with smaller measures except for the variable sepal width. Another aspect to highlight is that most of the maximum values are reached for the Iris Virginica ([Sarma, 2021](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda)). 

###  3.2.5. Correlation Between Variables Grouped by Iris Species
I finish the study by analysing the correlation between variables grouped by iris species. In order to do that, I have used a heatmap visualization, since this is an easy way to show the correlation. In the next figure, we can find a heatmap for each of the iris species.

<img src="images/heatmap_by_class.png" alt="heatmap_by_class" width="750">

The previous heatmaps show that the higher correlation is reached by the Iris Virginica (0.86) between the variables sepal length and petal length. On the other hand, the lowest correlation corresponds to the Iris Setosa (0.18) for the variables petal length and sepal width.

In an overview, the Iris Versicolor is the specie with the greatest correlation between the variables and the Iris Setosa is the one that presents variables with the lowest correlation coefficient between them.

# 4. Conclusions
We have reached the last section of this analysis, where the conclusions will be exposed. Throughout the exploratory data analysis performed many interesting insights have been obtained about the famous Fisher’s Iris dataset. In the following lines, I will present the insights that I found more relevant: 
* The sepal and petal are usually longer than they are wide. Also, the sepals are on average bigger than the petals.
* We have a well-balanced dataset since there are 50 samples of each iris species.
* The Iris Versicolor and the Iris Virginica are the most similar in measurements. That is, these two types of Iris species are the most similar to each other. On the other hand, the Iris Setosa seems to be clearly differentiated from the other two iris species.
* The standard deviation shows that there is more variability in the Iris Virginia specie measurements than in the other ones.
* The Iris Versicolor is the specie with the greatest correlation between the variables and the Iris Setosa is the one that presents variables with the lowest correlation coefficient between them.

# 5. References
Code Grepper. (2021, April 05). *Pandas Read Csv Without Index Code Example*. [online] Available at: <https://www.codegrepper.com/code-examples/python/pandas+read+csv+without+index>

*Pandas. n.d. IO Tools (Text, CSV, HDF5, …)*. [online] Available at: <https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table>

Smith, A., n.d. *How To Set Column Names When Importing A CSV Into A Pandas DataFrame In Python*. [online] Adam Smith. Available at: <https://www.adamsmith.haus/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python#:~:text=Call%20pandas.,order%20they%20appear%20in%20names%20.>

Ebner, J., (2021, July 13). *Pandas Describe, Explained*. [online] Sharp Sight. Available at: <https://www.sharpsightlabs.com/blog/pandas-describe/>

Pandas. n.d. *Pandas.DataFrame.Describe*. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>

Beatty, A., (2022, February 28). [online] GitHub. Available at: <https://github.com/andrewbeattycourseware/pands2022/blob/main/jupyternotebooks/Topic07%20files.ipynb>

Pandas. n.d. *Pandas.DataFrame.To_String*. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html>

W3schools. n.d. *Pandas DataFrame Info() Method*. [online] Available at: <https://www.w3schools.com/python/pandas/ref_df_info.asp#:~:text=The%20info()%20method%20prints,method%20actually%20prints%20the%20info>

W3resource. n.d. *Pandas DataFrame: Head() Function*. [online] Available at: <https://www.w3resource.com/pandas/dataframe/dataframe-head.php>

H.G. Marchant, B., (2020, December 17). *How To Create A Histogram From A Dataframe Using Pandas In Python ?*. [online] Moonbooks. Available at: <https://moonbooks.org/Articles/How-to-create-an-histogram-from-a-dataframe-using-pandas-in-python-/>

Li, J., (2015, July 23). *Save Dataframe.Hist() To A File*. [online] Stack Overflow. Available at: <https://stackoverflow.com/a/31596130>

Marsja, E., (2020, February 12). *How To Plot A Histogram With Pandas In 3 Simple Steps*. [online] Erik Marsja. Available at: <https://www.marsja.se/how-to-plot-a-histogram-with-pandas-in-3-simple-steps/>

Machine Learning Plus. (2021, September 13). *Pandas Histogram - Machine Learning Plus*. [online] Available at: <https://www.machinelearningplus.com/pandas/pandas-histogram/>

Datagy. (2020, June 22). *Creating a Histogram With Python (Matplotlib, Pandas)*. [online] Available at: <https://datagy.io/histogram-python/>

Pandas. n.d. *Pandas.DataFrame.Hist*. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html>

Wang, E., (2016, June 19). *Add Title To Collection Of Pandas Hist Plots*. [online] Stack Overflow. Available at: <https://stackoverflow.com/a/37907287>

IncludeHelp. n.d. *Bold Text Label In Python Plot*. [online] Available at: <https://www.includehelp.com/python/bold-text-label-in-plot.aspx>.

O’Reilly Online Learning. n.d. *Python Data Science Handbook*. [online] Available at: <https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html>

Matplotlib. n.d. *Title Positioning*. [online] Available at: <https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html>

Koehrsen, W., (2018, April 6). *Visualizing Data With Pairs Plots In Python*. [online] Medium. Available at: <https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166>

Kumar Rishi, R., (2021, April 9). *Increase The Distance Between The Title And The Plot In Matplotlib*. [online] Tutorialspoint. Available at: <https://www.tutorialspoint.com/increase-the-distance-between-the-title-and-the-plot-in-matplotlib>

Seaborn. n.d. *Seaborn.Pairplot*. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.pairplot.html>

Seaborn. n.d. *Seaborn.Set_Style*. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.set_style.html>

Seaborn. n.d. *Seaborn.Heatmap*. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.heatmap.html>

Seaborn. n.d. *Seaborn.Color_Palettes*. [online] Available at: <https://seaborn.pydata.org/tutorial/color_palettes.html>

Seaborn. n.d. *Seaborn.Countplot*. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.countplot.html>

Pandas. n.d. *Pandas.DataFrame.Boxplot*. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html>

Pandas. n.d. *Pandas.DataFrame.Groupby*. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html>

Pandas. n.d. *Pandas.DataFrame.Transpose*. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html>

Jupyter, C., (2020, June 27). *Customizing Seaborn Plots*. [online] Chan's Jupyter. Available at: <https://goodboychan.github.io/python/datacamp/visualization/2020/06/27/01-Customizing-Seaborn-Plots.html>

Malik, U., (2020, January 17). *Making Seaborn Scatter Plots With Sns.Scatterplot*. [online] wellsr. Available at: <https://wellsr.com/python/seaborn-scatter-plot-with-sns-scatterplot/>

Matplotlib. n.d. *Choosing Colormaps in Matplotlib*. [online] Available at: <https://matplotlib.org/stable/tutorials/colors/colormaps.html>

Serenity, (2016, June 9). *Savefig Loop Adds Previous Plots To Figure*. [online] Stack Overflow. Available at: <https://stackoverflow.com/a/37736370>

Smith, A., n.d. *How To Find The Correlation Between Two Pandas DataFrame Columns In Python*. [online] Adam Smith. Available at: <https://www.adamsmith.haus/python/answers/how-to-find-the-correlation-between-two-pandas-dataframe-columns-in-python>

Mccullum, N., n.d. *How To Create Boxplots In Python Using Matplotlib*. [online] Nick Mccullum. Available at: <https://nickmccullum.com/python-visualization/boxplot/>

Carvalho, T., (2020, June 29). *Heatmap Basics With Python’s Seaborn*. [online] Medium. Available at: <https://towardsdatascience.com/heatmap-basics-with-pythons-seaborn-fb92ea280a6c>

Zach, V., (2021, September 28). *How To Create Subplots In Seaborn (With Examples)*. [online] Statology. Available at: <https://www.statology.org/seaborn-subplots/>

tmdavison, (2018, September 11). *Figsize In Matplotlib Is Not Changing The Figure Size?*. [online] Stack Overflow. Available at: <https://stackoverflow.com/a/52274849>

Gazar, M., (2018, October 31). *Matplotlib/Seaborn Basics*. [online] Medium. Available at: <https://towardsdatascience.com/matplotlib-seaborn-basics-2bd7b66dbee2>

Chris, (2012, April 5). *How Can I Make A Blank Subplot In Matplotlib?*. [online] Stack Overflow. Available at: <https://stackoverflow.com/a/10035974>

areuexperienced, (2015, September 22). *How Do I Add A Title And Axis Labels To Seaborn Heatmap?*. [online] Stack Overflow. Available at: <https://stackoverflow.com/a/32724156>

beardc, (2013, February 6). *How To Access Pandas Groupby Dataframe By Key*. [online] Stack Overflow. Available at: <https://stackoverflow.com/a/14734627>

Polla, M., (2018, April 10). *Markdown - Resize Pictures In GitHub*. [online] Github. Available at: <https://gist.github.com/MichaelPolla/a65ac84286ab523603e64549f9850223>

W3schools. n.d. *HTML Img Tag*. [online] Available at: <https://www.w3schools.com/tags/tag_img.asp>

Sharma, P., (2021, April 3). *Exploratory Data Analysis: Iris Dataset*. [online] Medium. Available at: <https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda>

Columbia College. n.d. *LibGuides: APA Citation Guide (7th edition)*: In-Text Citation. [online] Available at: <https://columbiacollege-ca.libguides.com/c.php?g=713274&p=5082934>

Kumar, R., (2018, September 14). *Seaborn Plot To Visualize Iris Data*. [online] Kaggle. Available at: <https://www.kaggle.com/code/rakesh6184/seaborn-plot-to-visualize-iris-data/notebook>

GeeksforGeeks. (2022, April 26). *Exploratory Data Analysis on Iris Dataset*. [online] Available at: <https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/#:~:text=Iris%20Dataset%20is%20considered%20as,flowers%20and%20recorded%20them%20digitally>

West, C., (2020, July 10). *What Is A Scatter Plot And When To Use One*. [online] Visme. Available at: <https://visme.co/blog/scatter-plot/>

Koehrsen, W., (2018, April 6). *Visualizing Data with Pairs Plots in Python*. [online] Medium. Available at: <https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166>

Pomiklo, M., (2021, October 8). *What Is Data Exploration? Definition And Techniques*. [online] Data Analytics. Available at: <https://dsstream.com/data-exploration-definition-and-techniques/>

Siderova, S., n.d. *Frequency Distribution: Histogram Diagrams*. [online] Nave. Available at: <https://getnave.com/blog/histogram-diagram/>
