import os
from pytube import YouTube
from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip  # Added this line

def download_video(url, index):
    try:
        yout = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        video_stream = yout.streams.get_highest_resolution()

        # Create the 'car_videos' directory if it doesn't exist
        output_dir = 'car_videos'
        os.makedirs(output_dir, exist_ok=True)

        # Save the video as 'video_{index}.mp4' in the 'car_videos' directory
        video_stream.download(output_dir, filename=f'video_{index-1}.mp4')
        # Get and print the name of the channel
        channel_name = yout.author
        print(f"Download successful! Video saved as video_{index-1}.mp4 from the channel: {channel_name}")
        video_title = yout.title if yout.title else "What do you think about this?"
        combined_string = (
            f"{video_title}\n\n\n\n"
            f"Source: YT//{channel_name}\n\n\n\n"
        )

        # Read hashtags from "car_hashtags.txt" and append to the combined string
        hashtags_file_path = 'car_hashtags.txt'
        if os.path.exists(hashtags_file_path):
            with open(hashtags_file_path, 'r') as hashtags_file:
                hashtags_content = hashtags_file.read()
                combined_string += f"{hashtags_content}\n"

        # Print the combined string
        print(combined_string)

        # Create a VideoFileClip object from the downloaded video
        video_path = os.path.join(output_dir, f'video_{index-1}.mp4')
        video_clip = VideoFileClip(video_path)
        # Create a TextClip with the specified text and settings
        text_clip = TextClip("@dumbd.drivers", fontsize=50, color='white', size=(video_clip.size[0], 30), transparent=True, stroke_color='red', stroke_width=1)


        # Set the duration of the TextClip to match the video_clip duration
        text_clip = text_clip.set_duration(video_clip.duration)
        # Overlay the text clip on the video clip
        video_with_text = CompositeVideoClip([video_clip, text_clip.set_position(('center', video_clip.size[1] - 150))])

        # Write the final video with text to a new file
        output_video_path = os.path.join(output_dir, f'video_{index-1}.mp4')
        video_with_text.write_videofile(output_video_path, codec='libx264', audio_codec='aac')  # Added this line

    except Exception as e:
        print(f"Download failed: {e}")

def get_next_link(file_path):
    try:
        # Read the current index and all links from the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # Extract the current index and URL
            current_index = int(lines[0].strip())
            next_url = lines[current_index].strip()

            # Increment the index for the next use
            current_index += 1

        # Update the index in the file
        with open(file_path, 'w') as file:
            # Write the updated index
            file.write(str(current_index) + '\n')

            # Write back all the links
            file.writelines(lines[1:])

        return next_url, current_index
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Replace 'your_file_path.txt' with the path to your text file
file_path = 'car_videos.txt'

# Read the next URL and index from the text file
url, index = get_next_link(file_path)

if url:
    # Download the video using the obtained URL and save it to the 'car_videos' directory
    download_video(url, index)
