import re

def identify_media_type(url):
    # Instagram reels URL pattern
    reels_pattern = r'^https?://www\.instagram\.com/reel/'

    # YouTube shorts URL pattern
    shorts_pattern = r'^https?://www\.youtube\.com/shorts/'

    # Check if the URL matches the reels pattern
    if re.match(reels_pattern, url):
        return "Instagram Reels"
    # Check if the URL matches the shorts pattern
    elif re.match(shorts_pattern, url):
        return "YouTube Shorts"
    else:
        return "Unknown Media Type"