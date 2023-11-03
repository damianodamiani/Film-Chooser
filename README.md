# Film-Chooser

A simple Python script designed to randomly select a movie from a specified directory (typically an external hard drive containing movie files) and retrieve detailed information about the selected movie from the OMDb API. It provides information such as the movie's title, year of release, genre, length, director, main cast, IMDb rating, Rotten Tomatoes rating, and a plot summary, and other.

## How to use

1. You need to first obtain an OMDb API key by registering on the OMDb API website (http://www.omdbapi.com/apikey.aspx). Replace 'YOUR_OMDB_API_KEY' in the script with your actual OMDb API key then -- just the key, not the key URL!
2. Set the `external_drive_path` variable to the path of the directory where your movie files are located. Make sure to specify the correct path to your external hard drive -- or anywhere else you might want to browse.
3. Ensure you have the required Python libraries installed (see below).
4. Save the script to a Python (.py) file on your computer.
5. Make sure to have an active internet connection as the script relies on external API calls to fetch movie information.
6. Run the script using a Python interpreter. It will randomly select a movie from the specified directory and retrieve detailed movie information from the OMDb API. The information will be displayed in the console.

## Requirements

The Python standard library includes two of the required libraries, os and random, but you need to install requests: `pip install requests`.

*Script written with the help of GPT-3.5.*
