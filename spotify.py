from urllib.parse import urlparse, urlunparse
import requests
from bs4 import BeautifulSoup


def clean_spotify_url(url):
    """
    Removes query parameters like ?si=... from Spotify URL
    """
    parsed = urlparse(url)
    clean_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))
    return clean_url


def get_artist_and_track(spotify_url):
    """
    Takes a Spotify track URL and returns artist name and track name.
    """
    # ✅ Clean the URL first
    spotify_url = clean_spotify_url(spotify_url)

    response = requests.get(spotify_url, timeout=10)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch Spotify page")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract track name
    track_tag = soup.find('meta', {'property': 'og:title'})
    track_name = track_tag.get('content') if track_tag else "Unknown track"
    
    # Extract artist info
    artist_tag = soup.find('meta', {'property': 'og:description'})
    artist_info = artist_tag.get('content') if artist_tag else "Unknown artist"
    
    # Split by middle dot to get artist
    artist_details = artist_info.replace('\u00b7', '·').split(' · ')
    artist_name = artist_details[0].strip() if len(artist_details) > 0 else "Unknown artist"
    
    return artist_name, track_name


# Optional test
if __name__ == "__main__":
    url = input("Spotify URL: ")
    artist, track = get_artist_and_track(url)
    print(f"Artist: {artist}")
    print(f"Track: {track}")
