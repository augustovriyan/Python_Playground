import re
import urllib.request
import sys

def download_twitter_video(url, filename):
    # set the maximum resolution for the downloaded video (720p)
    max_resolution = 720

    # download the HTML source code of the tweet's page
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')

    # extract the video URL from the HTML source code
    pattern = re.compile(
        r'content="https://video.twimg.com/ext_tw_video/\d+/pu/vid/\d+x(\d+)')
    match = pattern.search(html)
    if not match:
        print('Error: could not find video URL in tweet.')
        return
    video_url = re.sub(r'\d+x(\d+)', f'{max_resolution}x\\1', match.group(0)[9:])

    # display a download progress bar
    print('Downloading...', end='')

    def report_hook(count, block_size, total_size):
        progress = count * block_size * 100 / total_size
        progress_bar_width = 50
        progress_bar = ('=' * int(progress / 2)).ljust(progress_bar_width)
        sys.stdout.write('\r[%s] %.1f%%' % (progress_bar, progress))
        sys.stdout.flush()

    # download the video
    urllib.request.urlretrieve(video_url, filename, report_hook)
    print('\nDownload complete.')

def main():
    print("Options:")
    print("1. Download Twitter video")
    print("2. Exit")

    while True:
        option = input("Enter your choice (1 or 2): ")
        if option == '1':
            url = input("Enter the Twitter video URL: ")
            filename = input("Enter the filename to save the video as: ")
            download_twitter_video(url, filename)
        elif option == '2':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
