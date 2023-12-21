import requests
import re

def get_random_twitter_video_url():
    """
    Fetch a random Twitter video URL.
    Note: This is a placeholder function and requires additional logic to fetch a random URL dynamically.
    For simplicity, we'll use a static random video URL for demonstration purposes.
    """
    return "https://twitter.com/i/status/1670163475421712384"  # Placeholder for demonstration

def download_video(video_url, save_path):
    """
    Download a video from the provided URL and save it to the specified path.
    """
    try:
        # Fetch the source page of the Twitter video
        response = requests.get(video_url)
        response.raise_for_status()  # Check for any HTTP errors

        # Extract the video URL using regular expressions (more robust than string search)
        match = re.search(r'(https://video.twimg.com[^"]+)', response.text)
        if not match:
            print("Video URL not found.")
            return

        video_link = match.group(0)

        # Download the video
        response = requests.get(video_link)
        response.raise_for_status()  # Check for any HTTP errors

        with open(save_path, "wb") as outfile:
            outfile.write(response.content)

        print(f"Video successfully downloaded to {save_path}")

    except requests.exceptions.RequestException as e:
        print("Error occurred during the download:", str(e))

if __name__ == "__main__":
    # Get a random Twitter video URL (for demonstration purposes)
    random_video_url = get_random_twitter_video_url()

    # Define the path to save the downloaded video
    save_path = r"F:\twitter_video.mp4"

    # Download the video
    download_video(random_video_url, save_path)
