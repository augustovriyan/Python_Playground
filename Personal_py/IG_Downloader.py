import requests
from bs4 import BeautifulSoup

# URL of the Instagram post or story
post_url = "https://www.instagram.com/p/ABC123/"

try:
    # Get the source page of the Instagram post or story
    response = requests.get(post_url)
    response.raise_for_status()  # Check for any HTTP errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the video or image element
    media_element = soup.find("meta", property="og:video") or soup.find("meta", property="og:image")

    if media_element:
        media_url = media_element.get("content")

        # Determine the file extension based on the media URL
        file_extension = "mp4" if "video" in media_url else "jpg"

        # Download the media to the specified directory
        response = requests.get(media_url)
        response.raise_for_status()  # Check for any HTTP errors

        # Save the downloaded media with a descriptive filename
        filename = f"downloaded_media.{file_extension}"
        with open(filename, "wb") as outfile:
            outfile.write(response.content)

        print(f"Media successfully downloaded as '{filename}'")

    else:
        print("No media found on the given URL")

except requests.exceptions.RequestException as e:
    print("Error occurred during the download:", str(e))
