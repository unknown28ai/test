from TikTokApi import TikTokApi
import requests

# TikTok API to download trending videos
def download_tiktok_videos():
    api = TikTokApi.get_instance()
    trending_videos = api.by_trending(count=1)  # Fetch one trending video

    video_url = trending_videos[0]['video']['playAddr']  # Get video URL
    return video_url  # Return the direct URL to the video


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
    caption = "Reposting TikTok video to Instagram #repost"
    post_to_instagram(video_url, caption)

if __name__ == "__main__":
    main()
