import requests
from gtts import gTTS
import os
from bs4 import BeautifulSoup

def get_reddit_post_info(post_url):
    response = requests.get(post_url)
    soup = BeautifulSoup(response.text, 'html.parser')


    # Extract body from the Reddit post
    body_element = soup.find('div', {'class': 'md'})
    body = body_element.get_text().strip() if body_element else "Body not found"

    return body

def text_to_speech(text, output_file='reddit_post.wav', lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    os.system(f'open {output_file}')  # Open the generated audio file
  # Open the generated audio file

if __name__ == "__main__":
    reddit_post_url = input("Enter the Reddit post URL: ")

    try:
        body = get_reddit_post_info(reddit_post_url)

        # Use the first three words of the title as the filename
        filename = "reddit_post.wav"
        text_to_speech(f"{body}", output_file=filename)

    except Exception as e:
        print(f"Error: {e}")
