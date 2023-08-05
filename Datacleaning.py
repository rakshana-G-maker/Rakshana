import pandas as pd

# Assuming you already have the movie_ratings_data from the data collection step
# movie_ratings_data = [...], where each element is a dictionary containing movie details
file_path = '''C\\Users\\Admin\\PycharmProjects\\EDAMovieRatings\\dataset\\IMDBTop250Movies.csv'''

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)


# Print the initial summary of the dataset
print("Initial Summary:")
print(df.info())

# Data Cleaning Steps

# 1. Handling Missing Values (if any)
# Check for missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# If there are missing values, you can choose to drop rows with missing values or impute them with appropriate values.

# Example: Drop rows with any missing value
df.dropna(inplace=True)

# 2. Formatting Data (if needed)
# If any columns have inconsistent formats, you can format them appropriately.
# For example, converting strings to numeric values, removing unnecessary characters, etc.


# 3. Handling Duplicates (if any)
# Check for and remove duplicates, if present.
print("\nDuplicates:")
print(df.duplicated().sum())

# Example: Remove duplicates
df.drop_duplicates(inplace=True)




# Print the final summary of the dataset after cleaning
print("\nFinal Summary:")
print(df.info())