# Sample movie data with genres
movies = {
    'Movie1': {'Genre': 'Comedy', 'Rating': 5},
    'Movie2': {'Genre': 'Action', 'Rating': 4},
    'Movie3': {'Genre': 'Comedy', 'Rating': 3},
    'Movie4': {'Genre': 'Drama', 'Rating': 5},
    'Movie5': {'Genre': 'Action', 'Rating': 4},
    'Movie6': {'Genre': 'Comedy', 'Rating': 2},
    'Movie7': {'Genre': 'Drama', 'Rating': 3},
}

# Function to get movie recommendations within a genre for a user
def get_genre_recommendations(user_genre, num_recommendations=3):
    genre_movies = {movie: details for movie, details in movies.items() if details['Genre'] == user_genre}
    sorted_movies = sorted(genre_movies, key=lambda movie: genre_movies[movie]['Rating'], reverse=True)
    return sorted_movies[:num_recommendations]

# Get user's preferred genre
user_preferred_genre = input("Enter your preferred genre: ")

# Get recommendations for the preferred genre
genre_recommendations = get_genre_recommendations(user_preferred_genre)

if genre_recommendations:
    print(f"Recommended {user_preferred_genre} movies: {', '.join(genre_recommendations)}")
else:
    print("No recommendations available for the selected genre.")
