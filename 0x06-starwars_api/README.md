# Star Wars Characters Script

This script fetches and prints the names of characters from a specified Star Wars movie using the Star Wars API (SWAPI). The character names are printed in the order they appear in the movie data.

## Requirements

- Node.js
- The `request` module

## Installation

1. Ensure you have [Node.js](https://nodejs.org/) installed on your system.
2. Install the `request` module by running the following command:

```sh
npm install request
Usage
To use the script, provide the Movie ID as a command-line argument. The script will then fetch and print the names of the characters in that movie.

Example
To fetch and print the characters in "Return of the Jedi" (Movie ID 3), run the following command:

sh
Copier le code
./0-starwars_characters.js
Script Explanation

Request Movie Data:

The script sends a request to the SWAPI to get the movie data using the provided film ID.
If an error occurs, it throws an error.
Parse and Process Characters:

The exactOrder function is called with the list of character URLs and an initial index of 0.
The exactOrder function recursively processes each character URL in the order they appear.
Fetch and Print Character Names:

For each character URL, a request is sent to fetch the character's data.
The character's name is printed, and the function recursively calls itself with the next index.