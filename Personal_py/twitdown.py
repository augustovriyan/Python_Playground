import re
import urllib.request
import sys

TWEET_URL = 'https://twitter.com/MasterAlecsDOM/status/1670163475421712384'
DEFAULT_MAX_RESOLUTION = 720
VIDEO_FILENAME = 'test_1.mp4'

def fetch_html_content(url):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
    return html

def extract_video_url(html_content, max_resolution=DEFAULT_MAX_RESOLUTION):
    pattern = re.compile(r'content="https://video.twimg.com/ext_tw_video/\d+/pu/vid/(?P<resolution>\d+)x\d+')
    match = pattern.search(html_content)
    if not match:
        print('Error: could not find video URL in tweet.')
        return None
    resolution = match.group('resolution')
    video_url = match.group(0)[9:].replace(resolution, str(max_resolution))
    return video_url

def download_video(video_url, filename):
    def report_hook(count, block_size, total_size):
        progress = count * block_size * 100 / total_size
        progress_bar_width = 50
        progress_bar = ('=' * int(progress / 2)).ljust(progress_bar_width)
        sys.stdout.write('\r[%s] %.1f%%' % (progress_bar, progress))
        sys.stdout.flush()

    urllib.request.urlretrieve(video_url, filename, report_hook)
    print('\nDownload complete.')

if __name__ == "__main__":
    html_content = fetch_html_content(TWEET_URL)
    video_url = extract_video_url(html_content)

    if video_url:
        print('Downloading...')
        download_video(video_url, VIDEO_FILENAME)
