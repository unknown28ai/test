from TikTokApi import TikTokApi
import requests

# Function to download TikTok videos by hashtags
def download_tiktok_videos():
    api = TikTokApi()

    hashtags = ["therealworld", "hu", "hustlersuniversity", "matrix"]
    videos = []

    # Fetch videos for each hashtag
    for hashtag in hashtags:
        hashtag_videos = api.by_hashtag(hashtag, count=1)  # Fetch one video per hashtag
        videos.extend(hashtag_videos)  # Collect videos from all hashtags

    if videos:
        # Get the URL of the first video found
        video_url = videos[0]['video']['playAddr']  # Assuming 'playAddr' contains the video URL
        return video_url
    else:
        return None  # Return None if no videos found

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
    video_url = download_tiktok_videos()
    if video_url:
        caption = "Reposting Andrew Tate's video to Instagram #AndrewTate #Repost"
        post_to_instagram(video_url, caption)
    else:
        print("No videos found.")

if __name__ == "__main__":
    main()
