import requests

# URL of the Twitter video to be downloaded
video_url = "https://twitter.com/i/status/1670163475421712384"

try:
    # Get the source page of the Twitter video
    response = requests.get(video_url)
    response.raise_for_status()  # Check for any HTTP errors

    # Find the video URL with a simple resolution
    start = response.text.find('https://video.twimg.com/')
    end = response.text.find('.mp4', start) + 4
    video_link = response.text[start:end]

    # Download the video to the F:\ directory
    response = requests.get(video_link)
    response.raise_for_status()  # Check for any HTTP errors

    with open(r"F:\twitter_video.mp4", "wb") as outfile:
        outfile.write(response.content)

    print("Video successfully downloaded to F:\twitter_video.mp4")

except requests.exceptions.RequestException as e:
    print("Error occurred during the download:", str(e))
