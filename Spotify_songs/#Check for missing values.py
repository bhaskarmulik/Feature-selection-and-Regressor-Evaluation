#Check for missing values
df.isnull().index
#Dealing with None or Missing values

df['parental level of education'] = df['parental level of education'].replace('some college', None)
df.head()
###### Now, here, Gender, Race, Parental level of education , lunch and test preparation course are all categorical values. However, Lunch feature is less likely to impact scores. So, we'll mostly deal with gender, race, parental level of education, test preparation.

###### Here, Gender and race can be included in the dataset using one hot encoding since they donot have a heirarchial or orderly structure. However, parental level of education is likely to be directly proportional to the scores since educated parents are more likely to push their children towards education. Also, test preparation course also affect the scores directly. Hence, these two will be ordinally encoded.
