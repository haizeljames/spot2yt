# Spotify to YouTube M4A Downloader

A Python tool to download Spotify tracks as **M4A audio** from YouTube.  
Supports **single track**, **batch processing from a text file**, custom output folders, sleep intervals, and download limits.  

---

## Features

- Extracts **artist** and **track name** from Spotify links.  
- Searches YouTube for the track and picks the most relevant result.  
- Downloads **M4A audio only** (no conversion).  
- Supports **batch downloads** from a text file with multiple Spotify links.  
- Specify **output folder** (`-o`). Default is current directory.  
- Optionally add **sleep between downloads** to avoid being flagged.  
- Optionally **limit number of tracks** from a batch file.  
- **Skip existing files** to avoid duplicates.  
- **TQDM progress bar** for batch downloads.

---

## Installation

1. **Python 3.8+ required**
2. Clone the repository or download the code.  
3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements
```bash
requests>=2.30.0
beautifulsoup4>=4.12.2
youtubesearchpython>=1.6.8
yt-dlp>=2026.3.18
tqdm>=4.66.1
```

---

## Usage
### Download a single track

```bash
python main.py -u "https://open.spotify.com/track/6b37xrsNCWYIUphFBazqD6" -o /path/to/output
```

---

Output:
```bash
🎵 Manu Chao - Me Gustas Tu
▶ https://www.youtube.com/watch?v=rs6Y4kZ8qtw
Downloading: Manu Chao - Me Gustas Tu.m4a
100% Done
```

---

Download multiple tracks from a file
### tracks.txt example:

```bash
https://open.spotify.com/track/6b37xrsNCWYIUphFBazqD6
https://open.spotify.com/track/1u45nqhOI1QXjoCm1x4KPL
https://open.spotify.com/track/6K4t31amVTZDgR3sKmwUJJ
```

Command:

```bash
python main.py -f tracks.txt -o /path/to/output -s 15 -l 50
```

## Parameters:

```bash
Options:
  -f FILE       Path to text file containing Spotify links
  -u URL        Single Spotify track URL
  -o DIR        Output directory (default: current folder)
  -s SECONDS    Sleep time between downloads (default: 0)
  -l LIMIT      Maximum number of tracks to process from file
  -h, --help    Show all options
```

### Examples

**Single download:**
```bash
python main.py -u "https://open.spotify.com/track/6b37xrsNCWYIUphFBazqD6"
```

**Batch download:**
```bash
python main.py -f tracks.txt
```

**Batch with custom folder:**
```bash
python main.py -f tracks.txt -o "/home/linux/Downloads/spo/dwn"
```

**Batch with all options:**
```bash
python main.py -f tracks.txt -l 20 -s 10 -o "/home/linux/Downloads/spo/dwn"
```
### Notes

- Spotify links are automatically cleaned (removes `?si=...`)
- Existing files are skipped (no duplicates)
- Works on Linux, Windows, and macOS
- This tool works best with **popular or widely available songs that also exist on YouTube**
- If a track is not available on YouTube, the closest match (may be remix/cover) is downloaded
- Cookies are not required for normal usage.  
- In some cases (age-restricted or region-blocked videos), yt-dlp supports cookies via browser export, but this may cause format issues depending on the environment.

## Project Structure
```bash
main.py              # CLI entry point  
spotify.py           # Spotify scraping  
youtube_search.py    # YouTube search  
downloader.py        # yt-dlp audio download  
```
