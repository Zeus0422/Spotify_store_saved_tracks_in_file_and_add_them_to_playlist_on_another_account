import json
import webbrowser
import time

# Define the Spotify API callback URI
redirect_uri = 'http://localhost:8888/callback'


def main():
    try:
        # Attempt to import the Spotipy library
        import spotipy
    except ImportError:
        # If Spotipy isn't installed, install it using pip
        print("Module not found. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "spotipy"])

    # Import the Spotipy library and necessary components again after ensuring it's installed
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth

    # Instructions for the user to obtain Spotify API credentials
    print('\n' + "to start go to https://developer.spotify.com/, than pls login, go to dashboad (top right corner), now type in your cliend_id (without the quotation marks) followed by an enter and then your cliend_secret followed by an enter")
    url = "https://developer.spotify.com/"
    webbrowser.open(url)  # Opens the Spotify Developer Dashboard in a web browser

    # Collect Spotify API credentials from user input
    client_id = input("client_id: ")
    client_secret = input("client_secret: ")
    # Initialize Spotipy client with user credentials and required scopes
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read, playlist-read-private'))

    # Fetch saved tracks from Spotify
    tracks = spotify_saved_tracks(sp)

    # Instruction for the user in case of a file path error
    print('\n' * 2 + r'should there be an error check if the folder with this path exists: D:\Users\Benutzer1\Downloads\, if not pls change the path underneath with the right one followed by fav_tracks')
    # Save the fetched tracks into a file
    save = save_array_to_file(r'D:\Users\Benutzer1\Downloads\fav_tracks', tracks)


def spotify_saved_tracks(sp):
    print('\n' + "Your saved tracks:")
    tracks = []
    results = sp.current_user_saved_tracks(limit=50)  # Fetch the first 50 saved tracks
    items = results['items']

    # Loop to fetch all saved tracks if more than 50 exist
    while results['next']:
        results = sp.next(results)
        items.extend(results['items'])

    # Extract and print the name and artist of each track
    for item in items:
        track_name = item['track']['name']
        artist_name = item['track']['artists'][0]['name']
        formatted_track = f"{track_name} {artist_name}"
        tracks.append(formatted_track)
        time.sleep(0.1)  # Slight delay to avoid spamming the console
        print(track_name)

    return tracks


def save_array_to_file(file_path, data):
    # Convert the list of tracks to JSON format
    json_data = json.dumps(data)

    # Save the JSON data to the specified file path
    with open(file_path, 'w') as file:
        file.write(json_data)

    # Confirmation message for the user
    print("thank you, all your saved tracks were successfully added to a file and stored in your downloads folder")


# Ensure the main function runs only if the script is executed directly
if __name__ == "__main__":
    main()