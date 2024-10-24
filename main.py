from TikTokApi import TikTokApi
import requests

# Function to download TikTok videos by username
def download_tiktok_videos():
    api = TikTokApi()  # Correctly initialize TikTokApi

    # Search for videos by Andrew Tate's username or a specific hashtag
    username = "andrew.tate"  # Make sure this is correct
    user_videos = api.by_username(username, count=1)  # Fetch one video

    if user_videos:
        video_url = user_videos[0]['video']['playAddr']  # Get video URL
        return video_url  # Return the direct URL to the video
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
