import os
from pytube import YouTube

def download_short(url, output_dir):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        yout = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        video_stream = yout.streams.get_highest_resolution()

        # Save the video with the specified file name in the specified output directory
        channel_name = yout.author
        video_title = yout.title if yout.title else "What do you think about this?"
        file_name = ''.join(channel_name.split()[:3]) + "_" + ''.join(video_title.split()[:3]) + ".mp4"
        video_stream.download(output_dir, filename=file_name)

        # Get and print the name of the channel
    
        print("Short download complete")
        return file_name, channel_name, video_title

    except Exception as e:
        print(f"Download failed: {e}")

# Example usage
if __name__ == '__main__':
    # Replace 'your_file_path.txt' with the path to your text file
    file_name = 'test_vid.mp4'
    output_dir = 'car_videos'  # Adjust this to your desired output directory

    # Read the next URL and index from the text file
    url = "https://www.youtube.com/shorts/ltHAa1qQrFU"

    if url:
        # Specify the output file path directly
        download_short(url, output_dir)
