import time
import json

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import SpotifyException


def main():
    # Spotify API credentials
    client_id = ""
    client_secret = ""
    redirect_uri = 'http://localhost:8888/callback'

    # Initialize Spotify client with necessary scopes
    sp = Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read, playlist-read-private, playlist-modify-private, playlist-modify-public'))

    # Read track names from a JSON file
    tracks = read_array_from_json_file(r'D:\Users\Benutzer1\Downloads\akak')

    # Add tracks to a new Spotify playlist
    add_tracks(sp, tracks)


def read_array_from_json_file(file_path):
    # Open and load track names from the specified JSON file
    with open(file_path, 'r') as file:
        tracks = json.load(file)
        # Optional: Filter out track names with non-alphabetical symbols
        tracks = [track for track in tracks if isinstance(track, str) and all(char.isalpha() or char.isspace() for char in track)]

        print(tracks)  # Print the list of tracks for verification

    return tracks


def add_tracks(sp, tracks):
    # Define the name of the new playlist and retrieve the current user's ID
    playlist_name = "Lucas_fav_tracks"
    user_id = sp.me()["id"]

    try:
        # Create a new private playlist for the user
        playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
        playlist_id = playlist['id']
        print(f"Playlist '{playlist_name}' created with ID: {playlist_id}")

        # Search for each track by name to get its Spotify URI
        track_uris = []
        for track_name in tracks[:-1500]:  # Limit the number of tracks to avoid exceeding API rate limits
            try:
                results = sp.search(q=track_name, type='track', limit=1)
                if results['tracks']['items']:
                    track_uri = results['tracks']['items'][0]['uri']
                    track_uris.append(track_uri)
                    print(track_name)  # Print the track name for verification
                else:
                    print(f"Track not found: {track_name}")
            except Exception as e:
                print(f"Error getting track URI: {e}")

        # Add tracks to the playlist in batches of 100 to comply with API limits
        for i in range(0, len(track_uris), 100):
            batch = track_uris[i:i + 100]
            try:
                sp.user_playlist_add_tracks(user_id, playlist_id, batch)
            except SpotifyException as se:
                print(f"Error adding tracks to the playlist: {se}")
            time.sleep(0.1)  # Pause briefly to avoid hitting API rate limits

        print(f"All tracks added to playlist with ID: {playlist_id}")

    except SpotifyException as se:
        print(f"Error creating or adding tracks to the playlist: {se}")


if __name__ == "__main__":
    main()


