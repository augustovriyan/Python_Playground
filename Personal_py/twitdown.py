import re
import urllib.request
import sys

def get_video_url(tweet_url, max_resolution=720):
    with urllib.request.urlopen(tweet_url) as response:
        html = response.read().decode('utf-8')

    pattern = re.compile(r'content="https://video.twimg.com/ext_tw_video/\d+/pu/vid/\d+x(\d+)')
    match = pattern.search(html)
    if not match:
        print('Error: could not find video URL in tweet.')
        return None
    video_url = re.sub(r'\d+x(\d+)', f'{max_resolution}x\\1', match.group(0)[9:])
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
    tweet_url = 'https://twitter.com/MasterAlecsDOM/status/1670163475421712384'
    video_url = get_video_url(tweet_url)
    
    if video_url:
        filename = 'test_1.mp4'
        print('Downloading...')
        download_video(video_url, filename)
