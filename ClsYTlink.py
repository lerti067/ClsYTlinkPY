import re

def clean_youtube_url(url):
    video_id = re.search(r'(?:v=|/)([0-9A-Za-z_-]{11})', url)
    
    return f'https://www.youtube.com/watch?v={video_id.group(1)}' if video_id else None

def clean_playlist_url(url):
    playlist_id_match = re.search(r'list=([0-9A-Za-z_-]+)', url)
    
    return f'https://www.youtube.com/playlist?list={playlist_id_match.group(1)}' if playlist_id_match else None
   
while True:  
    youtube_link = input("paste here youtube link: ")

    links = re.split(r',\s*|\s+', youtube_link.strip())

    for link in links:
        clean_link = clean_youtube_url(link)
        clean_playlist_link = clean_playlist_url(link)
        if clean_link:
            print(f'url on video: {clean_link}')
            print(f'url on playlist: {clean_playlist_link}')
