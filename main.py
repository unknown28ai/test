from pytube import YouTube
import requests
import random

# Function to download a YouTube Short video
def download_youtube_short(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()  # Choose an mp4 stream
        return stream.url if stream else None
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

# Function to get a random YouTube Short
def get_random_youtube_short():
    shorts_urls = [
        "https://www.youtube.com/shorts/dQw4w9WgXcQ",  # Replace with actual YouTube Shorts URLs
        "https://www.youtube.com/shorts/abcdefghijk",  # Add more valid URLs
        "https://www.youtube.com/shorts/12345678901",
    ]
    return random.choice(shorts_urls)

# Instagram API to post the video
def post_to_instagram(video_url, caption):
    access_token = 'your-instagram-access-token'
    instagram_account_id = 'your-instagram-account-id'

    # Upload video to Instagram
    endpoint = f'https://graph.facebook.com/v14.0/{instagram_account_id}/media'
    data = {
        'access_token': access_token,
        'video_url': video_url,
        'caption': caption
    }
    response = requests.post(endpoint, data=data)
    print(response.json())

# Main function to download and post video
def main():
    video_url = download_youtube_short(get_random_youtube_short())
    
    if video_url:
        caption = "Reposting a video to Instagram #Repost"
        post_to_instagram(video_url, caption)
    else:
        print("No videos found.")

if __name__ == "__main__":
    main()
