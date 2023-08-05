import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\Admin\\PycharmProjects\\EDAMovieRatings\\dataset\\imdb_movies.csv"
df = pd.read_csv(file_path)

# Data Cleaning
# Checking the first few rows of the dataset
print(df.head())

# Checking the data types of columns and missing values
print(df.info())

# Handling missing values (if any)
# Example: If you have missing values in the "Rating" column, you can fill them with the mean value
mean_Rating = df['Rating'].mean()
df['Rating'].fillna(mean_Rating, inplace=True)
# Handling duplicates (if any)
df.drop_duplicates(inplace=True)

# Handling outliers (if any)
# You can use statistical methods like z-scores to detect and remove outliers

# Checking for any remaining missing values after cleaning
print(df.isnull().sum())

# Exploring basic statistics of numerical columns
print(df.describe())

# Checking unique values in categorical columns (if any)
# Example: Checking unique Genres of movies
print(df['Genre'].unique())
# Univariate Analysis
# Plotting a histogram of movie Ratings
plt.figure(figsize=(8, 6))
plt.hist(df['Rating'], bins=30, color='lightgreen', edgecolor='black')
plt.xlabel('Movie Rating')
plt.ylabel('Frequency')
plt.title('Histogram of Movie Ratings')
plt.show()

# Plotting a bar plot of movie Genres
plt.figure(figsize=(10, 6))
sns.countplot(x='Genre', data=df, palette='Set1')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Movie Genre')
plt.ylabel('Count')
plt.title('Number of Movies in Each Genre')
plt.show()

# Bivariate Analysis
# Scatter plot of movie Rating vs. Runtime (Minutes)
plt.figure(figsize=(8, 6))
plt.scatter(df['Rating'], df['Runtime (Minutes)'], alpha=0.5)
plt.xlabel('Movie Rating')
plt.ylabel('Runtime (Minutes)')
plt.title('Scatter plot of Movie Rating vs. Runtime (Minutes)')
plt.show()

# Box plot of movie Ratings for different Genres
plt.figure(figsize=(10, 6))
sns.boxplot(x='Genre', y='Rating', data=df, palette='Pastel2')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Movie Genre')
plt.ylabel('Movie Rating')
plt.title('Box plot of Movie Ratings across Genres')
plt.show()

