import re
import urllib.request
import sys

def fetch_video_url_from_tweet_page(url):
    """Fetch the video URL from the given Twitter tweet URL."""
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')
        
    pattern = re.compile(r'content="https://video.twimg.com/ext_tw_video/\d+/pu/vid/\d+x(\d+)')
    match = pattern.search(html_content)
    
    if not match:
        print('Error: Could not find video URL in the tweet.')
        return None
    
    max_resolution = 720
    video_url = re.sub(r'\d+x(\d+)', f'{max_resolution}x\\1', match.group(0)[9:])
    return video_url

def download_video(video_url, filename):
    """Download the video from the provided URL and save it with the given filename."""
    print('Downloading...', end='')
    
    def report_hook(count, block_size, total_size):
        """Display download progress."""
        progress = count * block_size * 100 / total_size
        progress_bar_width = 50
        progress_bar = ('=' * int(progress / 2)).ljust(progress_bar_width)
        sys.stdout.write('\r[%s] %.1f%%' % (progress_bar, progress))
        sys.stdout.flush()

    urllib.request.urlretrieve(video_url, filename, report_hook)
    print('\nDownload complete.')

def main():
    """Main function to handle user inputs and operations."""
    print("Options:")
    print("1. Download Twitter video")
    print("2. Exit")
    
    while True:
        option = input("Enter your choice (1 or 2): ")
        
        if option == '1':
            url = input("Enter the Twitter video URL: ")
            filename = input("Enter the filename to save the video as: ")
            
            video_url = fetch_video_url_from_tweet_page(url)
            
            if video_url:
                download_video(video_url, filename)
        elif option == '2':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
