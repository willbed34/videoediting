import requests
import re

def download_tiktok_video(url, filename):
    try:
        verify = re.match(r'^(https?://)?(www\.)?tiktok\.com/.+', url)
        if not verify:
            raise ValueError("Invalid TikTok URL!")

        print("URL Verified:", url)

        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        video_url_match = re.search(r'"playAddr":"(https://[^"]+)"', response.text)

        if video_url_match:
            video_url = video_url_match.group(1)
            print('Video URL:', video_url)

            # Download the video
            with requests.get(video_url, stream=True) as r:
                r.raise_for_status()  # Check if the request was successful
                with open(filename, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)
            print("Download Complete")
        else:
            raise ValueError("Video URL not found in the HTML")

    except requests.RequestException as e:
        raise ValueError(f"Error during request: {str(e)}")

if __name__ == '__main__':
    download_tiktok_video('https://www.tiktok.com/@woudlerfn/video/7313011961128668449?_r=1&_t=8iFKV5H0igU', 'video.mp4')
