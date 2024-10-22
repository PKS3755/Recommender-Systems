import pandas as pd

# Load movies and ratings datasets
movies = pd.read_csv('movie.csv')
ratings = pd.read_csv('rating.csv')

# Inspect the datasets
print(movies.head())
print(ratings.head())
