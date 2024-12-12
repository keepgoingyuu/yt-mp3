import os
import yt_dlp

def download_video(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Downloaded and converted to MP3 in {output_path}")

if __name__ == "__main__":
    output_path = "./downloads"
    os.makedirs(output_path, exist_ok=True)
    
    while True:
        url = input("Enter the YouTube URL (or type 'exit' to quit): ")
        if url.lower() == 'exit':
            break
        download_video(url, output_path)
