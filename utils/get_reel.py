import requests
from bs4 import BeautifulSoup
import re
import instaloader
import os

def download_instagram_reel(url, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        # Verify URL format
        verify = re.match(r'^(https?://)?([a-z0-9.\-]+[.][a-z]{2,4}/)(.*)$', url)
        if not verify:
            raise ValueError("Invalid URL!")

        # Use instaloader to get post details
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])

        # Fetching details
        author = post.owner_username
        caption = post.caption

        # Download the video
        video_url = post.video_url
        file_name = ''.join(author.split()[:3]) + "_" + ''.join(caption.split()[:3]) + ".mp4"
        r = requests.get(video_url, stream=True)
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        print("Reel Download Complete")
        return file_name, author, caption

    except requests.RequestException as e:
        raise ValueError(str(e))

if __name__ == '__main__':
    # Example usage
    output_dir = 'car_videos'
    download_instagram_reel('https://www.instagram.com/reel/C0wS8scO0tB/?igsh=MzRlODBiNWFlZA%3D%3D', output_dir)
