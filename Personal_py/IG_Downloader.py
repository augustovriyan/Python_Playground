import os
import requests
from bs4 import BeautifulSoup
import re

def download_instagram_media(post_url, download_dir="./"):
    try:
        # Validate the Instagram URL
        if not re.match(r"https://www\.instagram\.com/p/[\w-]+/$", post_url):
            print("Invalid Instagram URL. Please provide a valid URL.")
            return

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

            # Create the download directory if it doesn't exist
            os.makedirs(download_dir, exist_ok=True)

            # Construct the full file path
            filename = os.path.join(download_dir, f"downloaded_media.{file_extension}")

            # Download the media to the specified directory
            response = requests.get(media_url)
            response.raise_for_status()  # Check for any HTTP errors

            # Save the downloaded media with a descriptive filename
            with open(filename, "wb") as outfile:
                outfile.write(response.content)

            print(f"Media successfully downloaded as '{filename}'")

        else:
            print("No media found on the given URL")

    except requests.exceptions.RequestException as e:
        print("Error occurred during the download:", str(e))

if __name__ == "__main__":
    post_url = input("Enter the Instagram post URL: ")
    download_dir = input("Enter the download directory (default is current directory): ")
    
    if not download_dir:
        download_dir = "./"

    download_instagram_media(post_url, download_dir)
