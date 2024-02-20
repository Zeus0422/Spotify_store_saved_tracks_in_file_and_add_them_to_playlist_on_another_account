# Spotify Playlist Management - README

## Project Overview
This project comprises two Python scripts utilizing the Spotipy library to interact with Spotify's Web API. The first script, `save_tracks.py`, saves the user's Spotify saved tracks into a file. The second script, `add_tracks_to_playlist.py`, reads track names from a file and creates a new Spotify playlist, adding those tracks to the user's account.

### Scripts Description
- **save_tracks.py**: Extracts saved tracks from the user's Spotify library and saves them into a file.
- **add_tracks_to_playlist.py**: Creates a new Spotify playlist from saved track names in a file and adds them to the user's Spotify account.

## Environment Setup
### Prerequisites
- Python and Pip installation.
- Spotipy library installation via `pip install spotipy`.
- Spotify Developer credentials (`client_id` and `client_secret`) obtained from [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

## Detailed Function Descriptions

### save_tracks.py
#### `main()`
Initializes Spotipy client with user credentials, retrieves saved tracks, and saves them to a JSON file.

#### `spotify_saved_tracks(sp)`
Fetches user's saved Spotify tracks, iterating through paginated results, and returns a list of track names with primary artists.

#### `save_array_to_file(file_path, data)`
Serializes the track list to JSON and saves it to the specified file path.

### add_tracks_to_playlist.py
#### `main()`
Sets up Spotipy client for reading library and modifying playlists, reads track names from a file, and adds them to a new playlist.

#### `read_array_from_json_file(file_path)`
Reads and returns track names from a JSON file, applying filters to ensure data accuracy for Spotify searches.

#### `add_tracks(sp, tracks)`
Creates a new playlist, searches for each track's Spotify URI, and adds tracks to the playlist in batches.

## Usage Instructions

### Saving Spotify Tracks
1. Run `save_tracks.py`.
2. Enter Spotify `client_id` and `client_secret` when prompted.
3. Saved tracks are stored in the designated file.

### Creating a Playlist from Saved Tracks
1. Prepare a JSON file with track names (via `save_tracks.py` or manually).
2. Execute `add_tracks_to_playlist.py`.
3. A new playlist is created and tracks are added to the user's Spotify account.

## Conclusion
These scripts automate the process of backing up Spotify tracks and creating playlists, showcasing effective use of the Spotipy library and Spotify API endpoints for personalized Spotify data management.

## Credits
This Blackjack game was developed by Carlos Eckert, a passionate programmer with a keen interest in creating engaging and interactive gaming experiences. For more information on the developer or to explore other projects, visit https://github.com/Zeus0422 or contact via email: carloseckert05coding@gmail.com.