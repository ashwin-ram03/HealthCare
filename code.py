# import requisite libraries 
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

data = pd.read_csv("ntrarogyaseva.csv")
data.head()

# print summary statistics
data.describe()

# display all the column names in the data
data.columns

# Display the counts of each value in the SEX column
data['SEX'].value_counts()

# mappings to standardize and clean the values
mappings = {'MALE' : 'Male', 'FEMALE' : 'Female', 'Male(Child)' : 'Boy', 'Female(Child)' : 'Girl'}
# replace values using the defined mappings
data['SEX'] = data['SEX'].replace(mappings)
data['SEX'].value_counts()

# plot the value counts of sex 
data['SEX'].value_counts().plot.bar()

# print the mean, median and mode of the age distribution
print("Mean: {}".format(data['AGE'].mean()))
print("Median: {}".format(data['AGE'].median()))
print("Mode: {}".format(data['AGE'].mode()))

# print the top 10 ages
data['AGE'].value_counts().head(10)

# better looking boxplot (using seaborn) for age variable
sns.boxplot(data['AGE'])


# subset involving only records of Krishna district
data[data['DISTRICT_NAME']=='Krishna'].head()

# Most common surgery by district
for i in data['DISTRICT_NAME'].unique():
    print("District: {}nDisease and Count: {}".format(i,data[data['DISTRICT_NAME']==i]['SURGERY'].value
                                                      
                                                      # Average claim amount for surgery by district
for i in data['DISTRICT_NAME'].unique():
    print("District: {}nAverage Claim Amount: ₹{}".format(i,data[data['DISTRICT_NAME']==i]['CLAIM_AMOUNT'].mean()))
                                                      
 # group by surgery category to get mean statistics
data.groupby('CATEGORY_NAME').mean()                                                  
