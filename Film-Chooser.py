import os
import random
import requests

# Replace 'YOUR_OMDB_API_KEY' with your actual OMDb API key (optional but recommended)
omdb_api_key = 'YOUR_OMDB_API_KEY'

# Replace 'YOUR_EXTERNAL_DRIVE_PATH' with the actual path to your external hard drive
external_drive_path = '/Volumes/YOUR_EXTERNAL_DRIVE_NAME'  # For example, '/Volumes/MyDrive'

# Define a list of common movie file extensions
movie_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']

def get_random_movie(directory):
    movie_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in movie_extensions):
                movie_files.append(os.path.join(root, file))

    if not movie_files:
        return None  # No movie files found
    
    random_movie = random.choice(movie_files)
    
    return random_movie

def extract_movie_title_from_filename(filename):
    # Extract the movie title from the filename following the "Film Title (Year)" pattern
    # You can use regular expressions for more complex filename patterns if needed
    name, _ = os.path.splitext(os.path.basename(filename))
    title = name.split('(')[0].strip()
    
    return title

def search_movie_info_using_omdb(movie_title):
    omdb_url = f'http://www.omdbapi.com/?t={movie_title.replace(" ", "+")}&apikey={omdb_api_key}'

    response = requests.get(omdb_url)

    if response.status_code == 200:
        movie_data = response.json()

        if movie_data.get('Response') == 'True':
            # Extract the main cast as a list with a maximum of 5 actors (if available)
            main_cast = movie_data['Actors'].split(', ')[:5]

            return {
                'title': movie_data['Title'],  # Title
                'country': movie_data.get('Country', 'N/A'),  # Country
                'language': movie_data.get('Language', 'N/A'),  # Language
                'original_title': movie_data.get('Title', 'N/A'),  # Handle missing Original Title
                'english_title': movie_data.get('Title', 'N/A'),  # Handle missing English Title
                'year': movie_data['Year'],  # Year
                'genre': movie_data['Genre'],  # Genre
                'length': movie_data['Runtime'],  # Length
                'production': movie_data.get('Production', 'N/A'),  # Production
                'budget': movie_data.get('Budget', 'N/A'),  # Budget
                'box_office': movie_data.get('BoxOffice', 'N/A'),  # Box Office
                'director': movie_data.get('Director', 'N/A'),  # Handle missing Director
                'writer': movie_data.get('Writer', 'N/A'),  # Writer
                'main_cast': main_cast,  # Cast
                'imdb_rating': movie_data['imdbRating'],
                'rotten_tomatoes_rating': movie_data['Ratings'][1]['Value'] if len(movie_data['Ratings']) > 1 else 'N/A',
                'plot_summary': movie_data['Plot'],
            }
        else:
            print(f"OMDb API Error: {movie_data.get('Error')}")

    else:
        print(f"OMDb API Request Error: {response.status_code}")

    return None

# Call the function with the external hard drive path
random_movie = get_random_movie(external_drive_path)

if random_movie:
    print("Randomly selected movie:", random_movie)
    
    # Extract the movie title from the filename using the specified pattern
    movie_title = extract_movie_title_from_filename(os.path.basename(random_movie))
    print("Extracted Movie Title:", movie_title)
    
    movie_info = search_movie_info_using_omdb(movie_title)

    if movie_info:
        print("Title:", movie_info['title'])
        print("Country:", movie_info['country'])
        print("Language:", movie_info['language'])
        print("Original Title:", movie_info['original_title'])
        print("English Title:", movie_info['english_title'])
        print("Year:", movie_info['year'])
        print("Genre:", movie_info['genre'])
        print("Length:", movie_info['length'])
        print("Production:", movie_info['production'])
        print("Budget:", movie_info['budget'])
        print("Box Office:", movie_info['box_office'])
        print("Director:", movie_info['director'])
        print("Writer:", movie_info['writer'])
        print("Main Cast:", ', '.join(movie_info['main_cast']))
        print("IMDb Rating:", movie_info['imdb_rating'])
        print("Rotten Tomatoes Rating:", movie_info['rotten_tomatoes_rating'])
        print("Plot Summary:", movie_info['plot_summary'])        

    else:
        print("Failed to fetch movie information using OMDb.")
else:
    print("No movie files found on the external hard drive.")
