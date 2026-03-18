import argparse
import os
import time
from tqdm import tqdm

# Import your existing modules
from spotify import get_artist_and_track
from youtube_search import get_youtube_url
from downloader import download_audio


def process_link(spotify_url, output_dir):
    """
    Process a single Spotify link:
    - Get artist & track
    - Search YouTube
    - Download audio
    """
    try:
        artist, track = get_artist_and_track(spotify_url)
        print(f"🎵 {artist} - {track}")

        yt_url = get_youtube_url(artist, track)
        print(f"▶ {yt_url}")

        download_audio(yt_url, output_dir)
        print("✅ Done\n")

    except Exception as e:
        print(f"❌ Failed: {spotify_url}")
        print(f"   Error: {e}\n")


def process_file(file_path, output_dir, limit=None, sleep_time=0):
    """
    Process a file containing Spotify links.
    Supports limit and sleep between downloads.
    Uses tqdm progress bar.
    """
    with open(file_path, 'r') as f:
        links = [line.strip() for line in f if line.strip()]

    if limit:
        links = links[:limit]

    total = len(links)
    print(f"📂 Processing {total} links...\n")

    # Wrap links with tqdm progress bar
    for link in tqdm(links, desc="Downloading", unit="track"):
        process_link(link, output_dir)
        if sleep_time > 0:
            time.sleep(sleep_time)


def main():
    parser = argparse.ArgumentParser(
        description="Spotify → YouTube → M4A downloader",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-u', '--url', help="Single Spotify track URL")
    parser.add_argument('-f', '--file', help="File containing Spotify URLs")

    parser.add_argument('-l', '--limit', type=int, help="Limit number of links (for file input)")
    parser.add_argument('-s', '--sleep', type=int, default=0, help="Sleep time between downloads (seconds)")

    parser.add_argument('-o', '--output', default=".", help="Directory to save downloaded audio files")

    args = parser.parse_args()

    # Validate input
    if not args.url and not args.file:
        parser.print_help()
        return

    # Ensure output directory exists
    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)

    # Process input
    if args.url:
        process_link(args.url, output_dir)
    elif args.file:
        process_file(args.file, output_dir, limit=args.limit, sleep_time=args.sleep)


if __name__ == "__main__":
    main()
