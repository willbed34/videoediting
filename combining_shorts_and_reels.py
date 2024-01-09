from utils import get_reel, get_short, get_media_type
from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip  # Added this line
import os
from utils.hashtags import CAR_HASHTAGS

def download_video(url, output_dir = "test_vids"):
    #find out which service it is
    media_type = get_media_type.identify_media_type(url)
    if media_type == "Instagram Reels":
       file_name, channel_name, video_title = get_reel.download_instagram_reel(url, output_dir)
    elif media_type == "YouTube Shorts":
        file_name, channel_name, video_title = get_short.download_short(url, output_dir)
    else:
        print("link not supported")
        return

    cleaned_title_with_hashtag = video_title.split('#')[0].strip()
    # Read hashtags from "car_hashtags.txt" and append to the combined string
    combined_string = (
        f"{cleaned_title_with_hashtag}\n\n\n\n"
        f"From {media_type}://{channel_name}\n\n\n\n"
    )
    if CAR_HASHTAGS:
        combined_string += ' '.join(CAR_HASHTAGS)
    
    # Print the combined string
    print(combined_string)

    # Create a VideoFileClip object from the downloaded video
    video_path = os.path.join(output_dir, file_name)
    video_clip = VideoFileClip(video_path)
    # Create a TextClip with the specified text and settings
    text_clip = TextClip("@dumbd.drivers", fontsize=50, color='white', size=(video_clip.size[0], 30), transparent=True, stroke_color='red', stroke_width=1)


    # Set the duration of the TextClip to match the video_clip duration
    text_clip = text_clip.set_duration(video_clip.duration)
    # Overlay the text clip on the video clip
    video_with_text = CompositeVideoClip([video_clip, text_clip.set_position(('center', video_clip.size[1] - 150))])

    # Write the final video with text to a new file
    output_video_path = os.path.join(output_dir, file_name)
    video_with_text.write_videofile(output_video_path, codec='libx264', audio_codec='aac')  # Added this line



if __name__ == "__main__":
    shorts_link = "https://www.youtube.com/shorts/ltHAa1qQrFU"
    reels_link = "https://www.instagram.com/reel/C0wS8scO0tB/?igsh=MzRlODBiNWFlZA%3D%3D"
    download_video(shorts_link, "test_vids")
    download_video(reels_link, "test_vids")
    