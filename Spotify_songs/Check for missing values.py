#Check for missing values
df.isnull().index
#Dealing with None or Missing values

df['parental level of education'] = df['parental level of education'].replace('some college', None)
df.head()
###### Now, here, Gender, Race, Parental level of education , lunch and test preparation course are all categorical values. However, Lunch feature is less likely to impact scores. So, we'll mostly deal with gender, race, parental level of education, test preparation.

###### Here, Gender and race can be included in the dataset using one hot encoding since they donot have a heirarchial or orderly structure. However, parental level of education is likely to be directly proportional to the scores since educated parents are more likely to push their children towards education. Also, test preparation course also affect the scores directly. Hence, these two will be ordinally encoded.


#For time series


#Now we drop the date and merge the month and year
df.drop('release_date', inplace=True, axis=1)
# Convert release_month and release_year into date format
df['release-date'] = df['release_month'].astype(str) + '-' + df['release_year'].astype(str)
df['release-date'] = pd.to_datetime(df['release-date'].astype(str), format='%m-%Y', errors='coerce')

#'release_month', 'release_year',
dropped_features = [ 'track_album_release_date']
df.drop(dropped_features, inplace=True, axis=1)
df.head()





#Now we analyze the relationship between release month/year wid track_popularity
# Replace empty values with 0 and convert to integers
# Replace empty values with 0 in 'release_month' column
df['release_month'].replace('', 0, inplace=True)

# Replace empty values with 0 in 'release_year' column
df['release_year'].replace('', 0, inplace=True)

# Convert columns to integers
df['release_month'] = df['release_month'].astype(int)
df['release_year'] = df['release_year'].astype(int)

print(plt.scatter(df['release_year'], df['track_popularity'], s=10))
plt.figure(figsize=(12,8), dpi= 800)
plt.show()

print(plt.scatter(df['release_month'], df['track_popularity'], s=10))
plt.yticks
plt.figure(figsize=(12,8), dpi= 800)
plt.show()

# Plotting
plt.scatter(df['release-date'], df['track_popularity'], s=20)   #'s' parameter reduces the scale
plt.show()

#Thus, the DATE feature plays an important part in model training