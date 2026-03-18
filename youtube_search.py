from youtubesearchpython import VideosSearch


def get_youtube_url(artist, song):
    query = f"{artist} {song}"

    try:
        videos_search = VideosSearch(query, limit=1)
        result = videos_search.result()
    except Exception:
        raise Exception("YouTube search failed")

    if 'result' in result and len(result['result']) > 0:
        return result['result'][0]['link']
    else:
        raise Exception("No YouTube results found")


# Optional: test standalone
if __name__ == "__main__":
    artist = input("Artist: ")
    song = input("Song: ")

    url = get_youtube_url(artist, song)
    print(url)
