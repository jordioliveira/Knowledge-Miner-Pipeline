import os
import yt_dlp

def download_audio(url):
    video_id = url.split("v=")[-1].split("&")[0]
    audio_file = f"audio_{video_id}.webm"

    ydl_opts = {
        'format': 'bestaudio[ext=webm]/bestaudio/best',
        'outtmpl': f'audio_{video_id}.%(ext)s',
        'quiet': False,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    titulo = info.get("title", "Video")
    autor = info.get("uploader", "Autor desconhecido")

    if not os.path.exists(audio_file):
        raise RuntimeError("Falha no download do áudio.")

    return audio_file, titulo, autor
