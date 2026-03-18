import yt_dlp
import os

def download_audio(url, output_dir="."):
    """
    Download YouTube audio as M4A to the specified output directory.
    Defaults to current directory if output_dir not given.
    """
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'no_overwrites': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
