from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import speech_recognition as sr

# Function to transcribe audio using SpeechRecognition
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as audio_file:
        audio_data = recognizer.record(audio_file)
        text = recognizer.recognize_google(audio_data)
    return text

# Function to create a text clip at a specific time
def create_text_clip(text, start_time, end_time, fontsize=24, color='white', bg_color='black'):
    return TextClip(text, fontsize=fontsize, color=color, bg_color=bg_color).set_pos('bottom').set_start(start_time).set_end(end_time)

# Input paths
video_path = 'reddit_videos/cropped_video.mp4'
audio_path = 'reddit_post.wav'  # Make sure it's in a compatible format

# Load video and audio clips
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)

# Transcribe audio
transcribed_text = transcribe_audio(audio_path)

# Split the text into lines
text_lines = transcribed_text.split('\n')

# Create text clips and overlay them on the video
clips_with_text = []
start_time = 0
for line in text_lines:
    end_time = start_time + audio_clip.duration / len(text_lines)
    text_clip = create_text_clip(line, start_time, end_time)
    clips_with_text.append(text_clip)
    start_time = end_time

# Composite the text clips on the video
video_with_text = CompositeVideoClip([video_clip, *clips_with_text])

# Export the final video
video_with_text.write_videofile('output_video.mp4', codec='libx264', audio_codec='aac')
