# Importing essential packages
# imported packages for data analysis 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read excel file.
# Skipped first 2 rows because they are irrelevant for data
dirtydata = pd.read_excel("employee.xlsx", skiprows = 2)

# Check first 5 row 
dirtydata.head()


# Check last 5 row 
dirtydata.tail()



# summary of data

dirtydata.describe()

# First exploration of the data is mandatory
for i in dirtydata.select_dtypes(include = 'object').columns:
  print(dirtydata[i].value_counts())

# Fixed the titles and made them easier to read and understand
dirtydata = dirtydata.rename(columns={'GENDER': 'Gender', '#Age': 'Age', 'Employee_ID': 'Employee ID',
                                    
                                       'SALARY': 'Salary',
                                      'WORK HOURS': 'Work Hours', '#Year' : "Year", "#Month": "Month"})


# .str_strip() removes unccessary white spaces .lower() corrects capitalized data and .capitalize() makes first letter upper case.
dirtydata['Gender'] = dirtydata['Gender'].str.lower().str.strip().str.capitalize() 

# Replaced  M with Male and F with Female
dirtydata['Gender'] = dirtydata['Gender'].replace({'M': 'Male', 'F': 'Female'}) 

# Corrected spelling mistakes
dirtydata['Education_Level'] = dirtydata['Education_Level'].replace({"Bachelor's": 'Bachelor', "Master's": 'Master', 'Ph.D': 'PhD'}) 

# Corrected spelling mistakes and deleted unneccessary spaces with .strip()
dirtydata['Position'] = dirtydata['Position'].str.strip()
dirtydata['Position'] = dirtydata['Position'].replace({'Software_Engineer': 'Software Engineer', '"Data Scientist"': 'Data Scientist','"HR Manager"':'HR Manager','"Data Analyst"':"Data Analyst" })

# .str_strip() removes unccessary white spaces .lower() corrects capitalized data and .capitalize() makes first letter upper case.
dirtydata['Performance_Rating'] = dirtydata['Performance_Rating'].str.strip().str.lower().str.capitalize()

# Create a new Date column with only Year and Month
dirtydata['Date'] = pd.to_datetime(dirtydata['Year'].astype(str) + '-' + dirtydata['Month'].astype(str), format='%Y-%m').dt.to_period('M')
dirtydata = dirtydata.drop(['Year', 'Month'], axis=1)

desired_column_order = ['Employee ID', 'Age', 'Gender', 'Education_Level', 'Position', 'Years_Experience', 'Salary', 'Performance_Rating', 'Work Hours',"Date"]
dirtydata = dirtydata[desired_column_order]

# analysis of na values according to columns
dirtydata.isnull().sum()

# fill na values according to variable type 

dirtydata["Gender"].fillna(dirtydata["Gender"].mode()[0], inplace = True)

dirtydata["Education_Level"].fillna(dirtydata["Education_Level"].mode()[0],  inplace = True)

dirtydata["Position"].fillna(dirtydata["Position"].mode()[0], inplace = True)

mean_exp = dirtydata["Years_Experience"].mean()
dirtydata["Years_Experience"].fillna(value = mean_exp, inplace = True)

dirtydata["Performance_Rating"].fillna(dirtydata["Performance_Rating"].mode()[0], inplace = True)

mean_work = dirtydata["Work Hours"].mean()
dirtydata["Work Hours"].fillna(mean_work, inplace = True)

# duplicated row analysis with pandas
dirtydata.duplicated().sum()


# outlier value fixing for age variable 

for ages in dirtydata["Age"]:
    if int(ages)<0:
      dirtydata["Age"] = dirtydata["Age"].replace({ages:int(ages)*-1})

# outlier analysis with boxplot 


sns.boxplot(dirtydata["Age"])

sns.boxplot(dirtydata["Years_Experience"])

sns.boxplot(dirtydata["Salary"])

sns.boxplot(dirtydata["Work Hours"])


# outlier analysis with IQR method 

def outlier_treatment(datacolumn):
 sorted(datacolumn)
 Q1,Q3 = np.percentile(datacolumn , [25,75])
 IQR = Q3 - Q1
 lower_range = Q1 - (1.5 * IQR)
 upper_range = Q3 + (1.5 * IQR)
 return lower_range,upper_range


lower_sal , upper_sal = outlier_treatment(dirtydata["Salary"])

dirtydata[(dirtydata["Salary"] < lower_sal) | (dirtydata["Salary"] > upper_sal)]


lower_work , upper_work = outlier_treatment(dirtydata["Work Hours"])

dirtydata[(dirtydata["Work Hours"] < lower_work) | (dirtydata["Work Hours"] > upper_work)]

lower_age , upper_age = outlier_treatment(dirtydata["Age"])

dirtydata[(dirtydata["Age"] < lower_age) | (dirtydata["Age"] > upper_age)]

lower_year , upper_year = outlier_treatment(dirtydata["Years_Experience"])

dirtydata[(dirtydata["Years_Experience"] < lower_year) | (dirtydata["Years_Experience"] > upper_year)]

# data viz for exploratory data analysis

sns.set_style("whitegrid")

# Boxplot for Salary
sns.boxplot(dirtydata["Salary"])

# Salary and Work Hour
sns.scatterplot(x="Salary",y="Work Hours",data=dirtydata)

# Age and Salary
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', data=dirtydata, color='green')
plt.title('Relationship between Age and Salary')
plt.xlabel('Age')
plt.ylabel('Salary')


# data viz for research questions 


# q1 

# gender and salary relationship 

sns.boxplot(x = "Gender", y = "Salary", data = dirtydata).set_title('Gender and Salary Relationship')


# q2 

# education level and salary relationship 

sns.boxplot(x = "Education_Level", y = "Salary", data = dirtydata).set_title("Education Level and Salary Relationship")


# q3 

#  gender and education level relationship

dirtydata.groupby(["Gender", "Education_Level"]).size().unstack().plot(kind = "bar", stacked = True, title = "Gender and Education Level Relationship")


# q4 


# years experience and work hours relationship and their correlation value 

sns.scatterplot(x = "Years_Experience", y = "Work Hours", data = dirtydata).set_title("Years Experience and Work Hours Relationship")
r = np.corrcoef(dirtydata["Years_Experience"], y = dirtydata["Work Hours"])
r



# years experience and salary relationship and correlation value 

sns.scatterplot(data = dirtydata,  x = "Years_Experience", y = "Salary").set_title("Years Experience and Salary Relationship")
np.corrcoef(dirtydata["Years_Experience"], dirtydata["Salary"])



# distribution of salary variable 

sns.histplot(dirtydata['Salary'], bins=20, kde=True, color='skyblue')
