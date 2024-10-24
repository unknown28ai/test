from pytube import YouTube
import requests
import random

# Function to download a YouTube Short video
def download_youtube_short(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()  # Choose an mp4 stream
    return stream.url if stream else None

# Function to download TikTok videos by hashtags (or implement this if still needed)
def download_tiktok_videos():
    # Existing TikTok fetching logic here (if needed)
    return None  # Adjust as necessary

# Function to get a random YouTube Short
def get_random_youtube_short():
    shorts_urls = [
        "https://www.youtube.com/watch?v=shorts1",  # Replace with actual YouTube Shorts URLs
        "https://www.youtube.com/watch?v=shorts2",
        "https://www.youtube.com/watch?v=shorts3",
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
    # Try to download TikTok videos first
    video_url = download_tiktok_videos()
    if not video_url:
        # Fallback to YouTube Shorts if no TikTok video is found
        video_url = download_youtube_short(get_random_youtube_short())
    
    if video_url:
        caption = "Reposting a video to Instagram #Repost"
        post_to_instagram(video_url, caption)
    else:
        print("No videos found.")

if __name__ == "__main__":
    main()
